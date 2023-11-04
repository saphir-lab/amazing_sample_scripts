# This convenient script allows you to set the battery percentage at which you want to receive notifications. The script uses Pyler for notifications and Psutil to get the current battery percentage.

# Battery Notifier
# pip instal plyer
from plyer import notification
import psutil
from time import sleep

while True:
    battery = psutil.sensors_battery()
    life = battery.percent
    if life < 50:
        notification.notify(
            title = "Battery Low",
            message = "Please connect to power source",
            timeout = 10
        )
    sleep(60)