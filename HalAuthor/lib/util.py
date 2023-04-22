from datetime import datetime

def get_now_time() -> str:
    """日時及び時刻を返却する

    Returns:
        str: 時刻情報[年-月-日 hh:mm:ssの形式で返却する]
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")