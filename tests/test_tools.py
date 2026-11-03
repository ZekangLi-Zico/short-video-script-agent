import copy
import unittest

from src.mock import example_script
from src.tools import ToolBox, speech_units


class ToolTests(unittest.TestCase):
    def setUp(self):
        self.tools = ToolBox()

    def test_search_has_real_source_and_product_isolation(self):
        result = self.tools.search_materials("字幕功能", "demo-editor")
        self.assertEqual(result["materials"][0]["id"], "P01")
        self.assertTrue(all(m["product_id"] == "demo-editor" for m in result["materials"]))

    def test_search_can_return_no_results(self):
        self.assertEqual(self.tools.search_materials("量子计算芯片", "demo-editor")["count"], 0)

    def test_changed_query_changes_result(self):
        self.assertEqual(self.tools.search_materials("剪辑裁剪", "demo-editor")["materials"][0]["id"], "P02")

    def test_overlong_hold_is_detected_even_if_speech_is_short(self):
        result = self.tools.estimate_duration(example_script(long=True), 30)
        self.assertEqual(result["total_seconds"], 38)
        self.assertFalse(result["passed"])

    def test_boundary_duration_is_allowed(self):
        self.assertTrue(self.tools.estimate_duration(example_script(long=True), 38)["passed"])

    def test_cannot_fake_duration_by_zeroing_holds(self):
        result = self.tools.estimate_duration(example_script(), 1)
        self.assertGreater(result["total_seconds"], 1)
        self.assertFalse(result["passed"])

    def test_citation_with_real_id_and_fake_text_is_rejected(self):
        result = self.tools.check_rules(example_script(bad_claim=True), ["P01"])
        self.assertFalse(result["passed"])
        codes = [i["code"] for i in result["issues"]]
        self.assertIn("unsupported_claim", codes)
        self.assertIn("brand_rule_violation", codes)

    def test_fact_is_not_accepted_without_retrieval(self):
        result = self.tools.check_rules(example_script(), [])
        self.assertIn("source_not_retrieved", [i["code"] for i in result["issues"]])

    def test_no_fact_script_is_rejected(self):
        script = example_script()
        script["shots"] = script["shots"][:1]
        self.assertFalse(self.tools.check_rules(script, ["P01"])["passed"])

    def test_source_update_invalidates_old_statement(self):
        materials = copy.deepcopy(self.tools.materials)
        materials[0]["facts"][0]["text"] = "字幕功能暂不可用。"
        result = ToolBox(materials=materials).check_rules(example_script(), ["P01"])
        self.assertFalse(result["passed"])

    def test_fact_in_creative_block_is_rejected(self):
        script = example_script()
        script["shots"][0]["blocks"][0]["text"] = "自动完成剪辑，支持一键发布。"
        result = self.tools.check_rules(script, ["P01"])
        self.assertIn("unapproved_copy", [i["code"] for i in result["issues"]])

    def test_claim_in_title_or_visual_cannot_bypass_rules(self):
        for target in ["title", "visual"]:
            script = example_script()
            if target == "title":
                script["title"] = "免费提升80%效率"
            else:
                script["shots"][0]["visual"] = "展示自动识别所有语言的界面"
            self.assertFalse(self.tools.check_rules(script, ["P01"])["passed"])

    def test_successful_quotes_are_exact(self):
        result = self.tools.check_rules(example_script(), ["P01"])
        self.assertTrue(result["passed"])
        self.assertEqual(result["citations"][0]["quote"], "剪影练习版支持为视频添加字幕。")

    def test_fault_injection_only_changes_requested_count(self):
        tools = ToolBox(failures={"search_materials": 1})
        args = {"query": "字幕", "product_id": "demo-editor"}
        self.assertFalse(tools.call("search_materials", args)["ok"])
        self.assertTrue(tools.call("search_materials", args)["ok"])

    def test_malformed_tool_arguments_are_errors(self):
        self.assertFalse(self.tools.call("estimate_duration", {"script": {}, "target_seconds": 30})["ok"])
        self.assertFalse(self.tools.call("delete_files", {})["ok"])

    def test_chinese_and_english_units(self):
        self.assertEqual(speech_units("你好 world 30！"), 4)

    def test_duplicate_source_and_malformed_data_are_rejected(self):
        materials = copy.deepcopy(self.tools.materials)
        materials.append(copy.deepcopy(materials[0]))
        with self.assertRaisesRegex(ValueError, "ID 必须唯一"):
            ToolBox(materials=materials)
        with self.assertRaises(ValueError):
            ToolBox(materials=[{"id": "broken"}])

    def test_custom_materials_are_not_assumed_synthetic(self):
        self.assertFalse(ToolBox(materials=self.tools.materials).synthetic_data)

    def test_invalid_estimator_configuration_is_rejected(self):
        rules = copy.deepcopy(self.tools.rules)
        rules["speech_units_per_second"] = 0
        with self.assertRaises(ValueError):
            ToolBox(rules=rules)


if __name__ == "__main__":
    unittest.main()
