import pyautogui as p
#p.PAUSE = .3
#this should automate the game QWOP
for i in range(1000):
    p.keyDown('q')
    p.press('space')
    p.keyDown('p')
    p.press('space')
    p.keyUp('q')
    p.press('space')
    p.keyUp('p')
    p.press('space')
    p.keyDown('w')
    p.press('space')
    p.keyDown('o')
    p.press('space')
    p.keyUp('w')
    p.press('space')
    p.keyUp('o')
    p.press('space')
    
  
    

