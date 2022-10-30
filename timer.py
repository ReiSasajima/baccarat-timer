import schedule
from time import sleep
import datetime
import pytz
from playsound import playsound

#01 定期実行する関数を準備
def forty():
    # 今の時間を取得
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    print(f'今の時間は{now}です！10分前です!')
    playsound("警告音1.mp3")
    playsound("警告音1.mp3")

def fifty():
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    print(f'今は{now}です！カジノしていただきありがとうございました!')
    playsound("成功音.mp3")
    playsound("成功音.mp3")


# 40分になったらfortyの実行
schedule.every().hour.at(":40").do(forty)
# 50分になったらfiftyの実行
schedule.every().hour.at(":50").do(fifty)
# 数秒ごとに実装
# schedule.every(10).seconds.do(forty)

#03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)