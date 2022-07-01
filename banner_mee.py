from time import sleep
import pyautogui

sleep(3)
with open('to_ban_mee.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
        line = line.split(' ')
        if len(line) > 1:
            if ('<@') in line[1]:
                sleep(3)
                msg = "!ban {} bot".format(str(line[1]))
                pyautogui.write(msg)
                sleep(1)
                pyautogui.press('enter')
                print(line[1] + ' BANNED')
    
