# systemArmorExplosiveResistance
#
# Used by:
# Celestials named like: Incursion Effect (2 of 2)
# Celestials named like: Pulsar Effect Beacon Class (6 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, beacon, context):
    fit.ship.boostItemAttr("armorExplosiveDamageResonance", beacon.getModifiedItemAttr("armorExplosiveDamageResistanceBonus"),
                           stackingPenalties=True)
