from battle_details import *
from tank_specifications import *

coin_flip()

if coin_flip() == "Panzer":
    if hit_chance() is True:
        item_hit_1st = target_choice(t34_defensive_stats)
        item_hit_1st -= panzer_damage
    else:
        print("MISS")
    if hit_chance() is True:
        item_hit_2nd = target_choice(panzer_defensive_stats)
        item_hit_2nd -= t34_damage
    else:
        print("Miss")
elif coin_flip() == "T34:":
    if hit_chance() is True:
        item_hit_1st = target_choice(panzer_defensive_stats)
        item_hit_1st -= t34_damage
    else:
        print("MISS")
    if hit_chance() is True:
        item_hit_2nd = target_choice(t34_defensive_stats)
        item_hit_2nd -= panzer_damage
    else:
        print("Miss")
