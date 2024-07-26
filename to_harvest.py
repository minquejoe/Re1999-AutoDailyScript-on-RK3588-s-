import os
from to_task import to_task
import config_positions
from utils import game_double_tap, game_go_back_then_double_tap, game_sleep_tap_X2_LongInv

# Define the mapping from class name to adb command
class_to_adb = {
    'menu': {'func': game_double_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},
    'wilders_fullview': {'func': game_double_tap, 'params': config_positions.wilders_fullview},
    'wilders_harvest': {'func': game_sleep_tap_X2_LongInv, 'params': config_positions.wilders_harvest},
}

class_order = ["menu", "wilders_fullview", "wilders_harvest"]
finish_class = ["wilders_harvest"]

print("*="*20)
print(f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
