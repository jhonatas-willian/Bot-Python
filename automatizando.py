from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://login.live.com/")

navegador.find_element("xpath", value='//*[@id="i0116"]').send_keys("Email_aleatorio@hotmail.com")
time.sleep(1)

navegador.find_element("xpath", value='//*[@id="idSIButton9"]').click()
time.sleep(1)

navegador.find_element("xpath", value='//*[@id="i0118"]').send_keys("SenhaAleatoria123.")
time.sleep(1)

navegador.find_element("xpath", value='//*[@id="idSIButton9"]').click()
time.sleep(1)

navegador.find_element("xpath", value='//*[@id="KmsiCheckboxField"]').click()
time.sleep(1)

navegador.find_element("xpath", value='//*[@id="idBtn_Back"]').click()
time.sleep(1)

time.sleep(10)