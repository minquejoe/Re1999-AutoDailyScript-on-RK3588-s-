import config
import time
from utils import exec_seq, game_start, game_close

ERR_COUNT = config.ERR_COUNT
seq_retry_wait = config.seq_retry_wait
while ERR_COUNT:
    # 启动游戏
    game_start()

    if exec_seq():
        ERR_COUNT -= 1
        print(f"=== Remaining ERR_COUNT: {ERR_COUNT} ===")
        
        time.sleep(seq_retry_wait)
    else:
        ERR_COUNT = 0

    # 关闭游戏
    # 任务失败，达到重启游戏目的
    # 任务完成，省电
    game_close()
    