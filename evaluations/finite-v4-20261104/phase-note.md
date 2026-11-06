首轮核心修复的V26、V27、V29真实结果保留在live/，源码边界为tested-source.json。随后在记录恢复层增加活跃进程保护及保存失败标记，未改时长审核实现。最终源码边界为tested-source-final.json；后续完整真实复测独立保存在live-final/及web/，不把首轮结果冒充最终版本。自动测试由94项增加为95项。
