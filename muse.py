import pyautogui as p

import time as t
t.sleep(5)
p.click()
distance=500
while distance>0:
    p.dragRel(distance, 0, duration=5)
    distance=distance -5
    p.dragRel(0, 10, duration=1)
    distance=distance -5
    p.dragRel(-distance,0,duration=5)
    #p.dragRel(0, 10, duration=1)
    distance=distance-5
    p.dragRel(0, -10, duration=1)
