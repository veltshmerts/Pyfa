# minerCpuUsageMultiplyPercent2
#
# Used by:
# Variations of module: Mining Laser Upgrade I (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                  "cpu", module.getModifiedItemAttr("cpuPenaltyPercent"))