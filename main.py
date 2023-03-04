import pyautogui as pg
import webbrowser as web
import datetime
from time import sleep

# variables with defined times
first_hour = datetime.datetime.strptime("10:00", "%H:%M").time()
second_hour = datetime.datetime.strptime("11:00", "%H:%M").time()
third_hour = datetime.datetime.strptime("13:00", "%H:%M").time()
fourth_hour = datetime.datetime.strptime("15:00", "%H:%M").time()

# variable with phone number
phone_number = "55_41992220452"

# variables with messages
message_one = "Ola"
message_two = "Oi"
message_three = "Tudo bem?"
message_four = "Lembre de tomar água"

# sending the messages relative to the time
while True:
    now_hour = datetime.datetime.now().time()

    if first_hour == now_hour:
        web.open("https://web.whatsapp.com/send?phone="+phone_number+"&text="+message_one)
        sleep(4)
        width, height = pg.size()
        pg.click(width/2, height/2)
        sleep(7)
        pg.press("esc")
        sleep(5)
        pg.press("enter")
        sleep(10)
        pg.hotkey("ctrl", "w")
    elif second_hour == now_hour:
        web.open("https://web.whatsapp.com/send?phone=" + phone_number + "&text=" + message_two)
        sleep(4)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        sleep(7)
        pg.press("esc")
        sleep(5)
        pg.press("enter")
        sleep(10)
        pg.hotkey("ctrl", "w")
    elif third_hour == now_hour:
        web.open("https://web.whatsapp.com/send?phone=" + phone_number + "&text=" + message_three)
        sleep(4)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        sleep(7)
        pg.press("esc")
        sleep(5)
        pg.press("enter")
        sleep(10)
        pg.hotkey("ctrl", "w")
    elif fourth_hour == now_hour:
        web.open("https://web.whatsapp.com/send?phone=" + phone_number + "&text=" + message_four)
        sleep(4)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        sleep(7)
        pg.press("esc")
        sleep(5)
        pg.press("enter")
        sleep(10)
        pg.hotkey("ctrl", "w")
