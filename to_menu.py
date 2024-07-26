import os
from to_task import to_task
import config_positions
from utils import game_double_tap, game_go_back_then_double_tap

# Define the mapping from class name to adb command
class_to_adb = {
    'login_update': {'func': game_double_tap, 'params': config_positions.login_update},
    'login_error': {'func': game_double_tap, 'params': config_positions.login_error},
    'login_quit': {'func': game_double_tap, 'params': config_positions.login_quit},
    'menu': {'func': game_double_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},
}

class_order = ["waiting", "login_update", "menu"]
finish_class = ["menu", "menu_quit"]

print("*="*20)
print(f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
