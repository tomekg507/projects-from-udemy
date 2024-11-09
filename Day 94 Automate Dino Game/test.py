import pyautogui

dis = 'kurwe zwisa tetrisa anubisa dioniza waliza matiza remiza hiperanaliza suareza synteza orteza geneza katecheza gierczaka raka ssaka robaka lewaka jebaka JD'
dis_list = dis.split(' ')
print(dis_list)

i=0

pyautogui.hotkey('ctrl', 'shift', 'n')
pyautogui.write('Jebac disa', interval=0.10)
pyautogui.press('enter')

distance = 400
while distance > 0:

    pyautogui.drag(distance, 0, duration=0.01)   # move right
    distance -= 10
    pyautogui.drag(0, distance, duration=0.01)   # move down
    pyautogui.drag(-distance, 0, duration=0.01)  # move left
    distance -= 10
    pyautogui.drag(0, -distance, duration=0.01)  # move up
    i += 1
    pyautogui.hotkey('ctrl', 'shift', 'n')
    pyautogui.write(dis_list[i], interval=0.20)
    pyautogui.press('enter')

