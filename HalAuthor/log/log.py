import logging
import os
import sys

from enum import Enum
from lib import get_now_time

log_dir = "log/out"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, "example.log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")

# ファイル出力用のハンドラを追加
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# コンソール出力用のハンドラを追加
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# モード切替フラグ
do_write_file = True

class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

def set_log_dir(dir:str):
    """ログ出力先ディレクトリの変更

    Args:
        dir (str): ログ出力先
    """
    global log_dir
    log_dir = dir
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    __log_reload()
    
def switch_log_mode(value:bool):
    """ログ出力モードを切り替える。

    Args:
        value (bool): 切替変数
    """
    global do_write_file
    do_write_file = value

def log(msg:str, level:LogLevel):
    """ログ出力
    
    do_write_fileがTrueの場合は、
    ログ発生時にコンソールログ出力と同時にログファイルへの書き込みを行う。
    また、ログ書き込み時に指定レベル(level)に応じたログ出力を行う

    Args:
        msg (str): ログ出力文字列
        level (LogLevel): ログレベル
    """
    global do_write_file
    
    __print_log(level, msg)
    
    if do_write_file != True:
        return
    
    if level == LogLevel.DEBUG:
        logger.debug(msg)
    
    elif level == LogLevel.INFO:
        logger.info(msg)
        
    elif level == LogLevel.WARNING:
        logger.warning(msg)
        
    elif level == LogLevel.ERROR:
        logger.error(msg)
        
    elif level == LogLevel.CRITICAL:
        logger.critical(msg)
        
def __print_log(level:LogLevel, msg:str):
    """ログをコンソール出力する

    Args:
        logtag (LogLevel): ログレベル
        msg (str): ログ出力文字列
    """
    datetime = get_now_time()
    print(f"[{datetime}] level:{level.name} message:{msg}")
    
def __log_reload():
    """ログ処理に必要な情報の更新
    """
    global file_handler, log_dir, log_file
    
    log_file = os.path.join(log_dir, "example.log")
    new_file_handler = logging.FileHandler(log_file)
    new_file_handler.setLevel(logging.DEBUG)
    new_file_handler.setFormatter(formatter)
    
    logger.removeHandler(file_handler)
    logger.addHandler(new_file_handler)