#!/usr/bin/env python3

from ex0 import creature_factory as cf

def battle() -> None:
    flameling = cf.FlameFactory()
    aquabub = cf.AquaFactory()
    print("Testing factory")
    flameling.create_base()
