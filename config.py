# ==========================
#     adb服务器和设备位置
# ==========================
adb_host = "127.0.0.1"
adb_port = 5037
device_serial = "localhost:6602"

# ==========================
#         游戏名称
# ==========================
package_name = 'com.shenlan.m.reverse1999'
start_activity_name = 'com.ssgame.mobile.gamesdk.frame.AppStartUpActivity'

# ==========================
#     游戏交互时间间隔
# ==========================
double_tap_interval = 0.25
sleep_tap_long_interval = 10
sleep_tap_short_interval = 5
go_back_sleep_time = 3
next_task_interval = 5
next_file_interval = 5
long_sleep = 90

# ==========================
#        任务链设置
# ==========================
ERR_COUNT = 3   # 最大任务链失败次数
seq_retry_wait = 30 # seconds，每次任务链失败重试前等待时间

task_timeout = 300 # seconds，每个任务的最长时长
task_timeout_threshold = 5  # 允许的最大任务失败个数，任务链失败判定根据
task_seq = [
    "python3 to_menu.py",
    "python3 to_harvest.py",
    "python3 to_menu.py",
    "python3 to_mind.py",
    "python3 to_menu.py",
    "python3 to_gold.py",
    "python3 to_menu.py",
    "python3 to_dust.py",
    "python3 to_mailbox.py",
    "python3 to_menu.py",
    "python3 to_harvest.py",
    "python3 to_daily_weekly.py",
    "python3 to_juke.py",
]

# ==========================
#      Alert发送邮箱设置
# ==========================
SOURCE_MAIL_ADDR = "xxx"
SOURCE_MAIL_PASS = "xxx"
TARGET_MAIL_ADDR = "xxx"

# ==========================
#       mobileNet相关
# ==========================
RKNN_MODEL = 'model/mobilenetv2_re1999.rknn'
IMG_PATH = './screenshot.jpg'
CLASS_LABEL_PATH = 'model/mobilenetv2_re1999_class_labels.txt'

# ==========================
#    训练用的图片保存设置
# ==========================
PIC_SAVE_FLAG = False    # Decide whether to save the picture
PIC_SAVE_PATH = "screenShot"
PIC_SAVE_MAX = 100  # Maximum number of pictures to save