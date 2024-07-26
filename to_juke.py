import os
from to_task import to_task
import config_positions
from utils import game_double_tap, game_go_back_then_double_tap, game_juke_tap, game_one_tap, game_tap_sleep_X2_ShortInv

# Define the mapping from class name to adb command
class_to_adb = {
    'menu': {'func': game_double_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},
    'juke_box_point': {'func': game_juke_tap, 'params': config_positions.juke_box_point},
    'juke_box_calim': {'func': game_tap_sleep_X2_ShortInv, 'params': config_positions.juke_box_calim},
    'juke_box_calim_finish': {'func': game_one_tap, 'params': config_positions.juke_box_calim_finish},
}

class_order = ["menu", "juke_box_point", "juke_box_calim", "juke_box_calim_finish"]
finish_class = ["juke_box_calim", "juke_box_calim_finish"]

print("*="*20)
print(f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
