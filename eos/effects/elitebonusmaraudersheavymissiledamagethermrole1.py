# eliteBonusMaraudersHeavyMissileDamageThermRole1
#
# Used by:
# Ships named like: Golem (4 of 4)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "thermalDamage", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))
