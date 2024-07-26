import os
from to_task import to_task
import config_positions
from utils import game_double_tap, game_go_back_then_double_tap, game_daily_weekly_tap

# Define the mapping from class name to adb command
class_to_adb = {
    'menu': {'func': game_double_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},
    'task_daily': {'func': game_daily_weekly_tap, 'params': config_positions.task_daily},
    'task_weekly': {'func': game_daily_weekly_tap, 'params': config_positions.task_weekly},
}

class_order = ["menu", "task_daily", "task_weekly"]
finish_class = ["task_daily", "task_weekly"]

print("*="*20)
print(f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
