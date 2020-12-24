import datetime
import time
import pyautogui
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        now = datetime.datetime.now()
        print(now.year,now.month,now.day,now.hour,now.minute)

        if now.day == 24 and now.hour == 22 and now.minute == 57 :
            print('click moment')
            pyautogui.click()
        time.sleep(5)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
