from time import sleep
import pyautogui

sleep(3)
with open('to_ban_ids', 'r', encoding='utf-8') as f:
    for line in f:
                sleep(1)
                msg = "!ban <@{}> bot".format(str(line).rstrip())
                pyautogui.write(msg)
                sleep(1.5)
                pyautogui.press('enter')
                #print(msg)
                print(line + ' BANNED')
    
