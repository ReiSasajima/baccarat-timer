import schedule
from time import sleep
import datetime
import pytz

#01 定期実行する関数を準備
def task():
    # 今の時間を取得
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    print(now)
#02 スケジュール登録
# 毎時間指定分に実行
# schedule.every().hour.at(":33").do(task)
# 数秒ごとに実装
schedule.every(10).seconds.do(task)

#03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)