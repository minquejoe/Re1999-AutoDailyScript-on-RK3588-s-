import os
import time
from to_task import to_task
import config_positions
from utils import game_one_tap, game_double_tap, game_go_back_then_double_tap, game_tap_sleep_X2_ShortInv, game_one_tap_LongSleep

# Define the mapping from class name to adb command
class_to_adb = {
    'menu': {'func': game_double_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},
    'battle_story': {'func': game_one_tap, 'params': config_positions.battle_story},
    'battle_resource_01': {'func': game_one_tap, 'params': config_positions.battle_resource_01[os.path.basename(__file__)]},
    'battle_resource_02': {'func': game_one_tap, 'params': config_positions.battle_resource_02},
    'battle_resource_gold': {'func': game_tap_sleep_X2_ShortInv, 'params': config_positions.battle_resource_gold},
    'battle_entry': {'func': game_tap_sleep_X2_ShortInv, 'params': config_positions.battle_entry},
    'battle_confirm': {'func': game_one_tap_LongSleep, 'params': config_positions.battle_confirm},
    'battle_win': {'func': game_go_back_then_double_tap, 'params': config_positions.battle_win},
    'levelup': {'func': game_one_tap, 'params': config_positions.levelup},
}

class_order = ["menu", "battle_story", "battle_resource_01", "battle_resource_02", "battle_resource_gold", "battle_entry", "battle_confirm", "battle_ongoing", "battle_win"]
finish_class = ["battle_win", "low_vitality"]

print("*="*20)
print(f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
