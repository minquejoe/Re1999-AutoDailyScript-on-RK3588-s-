import os
import time
from once_infer import once_infer
from datetime import datetime
import shutil

import config
from utils import game_go_back

PIC_SAVE_FLAG = config.PIC_SAVE_FLAG
PIC_SAVE_PATH = config.PIC_SAVE_PATH
PIC_SAVE_MAX = config.PIC_SAVE_MAX

def save_pic(PIC_SAVE_FLAG):
    if PIC_SAVE_FLAG:
        # Check the number of pictures already saved
        num_pics = len([name for name in os.listdir(PIC_SAVE_PATH) if os.path.isfile(os.path.join(PIC_SAVE_PATH, name))])
        
        # If the number of pictures is less than the maximum, save the picture
        if num_pics < PIC_SAVE_MAX:
            # Move and rename the screenshot
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            new_screenshot_name = f"screenshot{timestamp}.jpg"
            shutil.move("screenshot.jpg", os.path.join(PIC_SAVE_PATH, new_screenshot_name))
            print(f'{new_screenshot_name} - pic saved!')
        else:
            print('Maximum number of pics reached, not saving any more pics.')
    else:
        print('Not saving pic, set [PIC_SAVE_FLAG]')

class OrderChecker:
    def __init__(self, class_order):
        self.class_order = class_order
        self.current_class_index = None

    def check(self, class_name):
        if class_name in self.class_order:
            if self.current_class_index is None or self.class_order.index(class_name) == self.current_class_index or self.class_order.index(class_name) == self.current_class_index + 1:
                pass
            else:
                print(f"Wrong class order! Save pic to {PIC_SAVE_PATH}")
                save_pic(PIC_SAVE_FLAG)
            # 只纠错一次，防止重复纠错
            self.current_class_index = self.class_order.index(class_name)

def to_task(class_to_adb, finish_class, class_order):
    oc = OrderChecker(class_order)

    while True:
        # Run the rknn_mobilenet_demo command and capture its output
        scores, idx_sorted, labels = once_infer()
        output = labels[idx_sorted[0]]
        print("*="*20)
        print('recogition: P %.2f LABEL %s' % (scores[idx_sorted[0]], output))

        # Extract the class name from the output
        class_name = output.split()[-1].strip()

        # check class order
        oc.check(class_name)

        # check if waiting
        if class_name == "waiting":
            print(f"Wating ... Sleep {config.next_task_interval} seconds")
            time.sleep(config.next_task_interval)
            continue

        # Check if the class_name exists
        if (class_name not in class_to_adb.keys()) or (class_name in ["others", "battle_ongoing"]):
            print(f"Not defined class or [others, battle_ongoing]: {class_name}")
            print(f"Save pic to {PIC_SAVE_PATH}, GO BACK ... ... Sleep {config.next_task_interval} seconds")
            
            save_pic(PIC_SAVE_FLAG)
            game_go_back()   # 回退
            time.sleep(config.next_task_interval)   # 重新开始了循环，休眠n秒
                                                    # 先返回，再休眠，防止截图截到中途的变化
            continue

        # Execute the adb func
        func = class_to_adb[class_name]['func']
        pos = class_to_adb[class_name]['params']
        print(func.__name__, pos)
        func(**pos)

        # Finish
        if class_name in finish_class:
            print("Finished. Exiting...")
            break

        # Sleep for few seconds
        time.sleep(config.next_task_interval)
