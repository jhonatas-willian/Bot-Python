import pyautogui
import time

pyautogui.PAUSE = 1

# Abrir a ferramente / sistema / programa
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")

# Clicar no login (Point(x=515, y=386)) or (Point(x=421, y=276))
pyautogui.click(x=421, y=276)
pyautogui.write("Jhonatas")

# Clicar na senha (Point(x=430, y=313)) or (Point(x=398, y=331))
pyautogui.click(x=398, y=331)
pyautogui.write("Senhaincorreta")

# Clicar em Fazer Login (Point(x=413, y=441)) or (Point(x=383, y=433))
pyautogui.click(x=383, y=433)

# Clicar em Voltar (Point(x=1250, y=1079)) or (Point(x=509, y=584))
time.sleep(3)
pyautogui.click(x=509, y=584)
