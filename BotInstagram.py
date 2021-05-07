from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# https://www.youtube.com/watch?v=0PdIP2Q2X4U&ab_channel=DevAprender
#https://github.com/mozilla/geckodriver

# //input[@name='username']
# //input[@name='password']

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path= r'C:\Users\hugo1\Desktop\Play_With_Instagram\geckodriver.exe')

    def login(self):
        driver = self.driver

        # Navegar até um site
        driver.get('https://www.instagram.com/')
        time.sleep(1) # Um tempo para carregar a página

        User_Element = driver.find_element_by_xpath("//input[@name='username']")
        User_Element.clear()
        User_Element.send_keys(self.username)

        User_Password = driver.find_element_by_xpath("//input[@name='password']")
        User_Password.clear()
        User_Password.send_keys(self.password)
        User_Password.send_keys(Keys.RETURN)

        
         # para não cair na primeira tela de notificação
   

    def curtir_fotos(self, hashtag):
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)

        # scroll da página
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            try:
                driver.find_element_by_xpath("//svg[@aria-label='Like']").click() # tipo button e propriedade class
                time.sleep(19)
            except Exception as e:
                time.sleep(5)
            break
        # aria-label="Like"
hugoBot = InstagramBot('hugorotorquato@gmail.com', 'Metalica-01.')

hugoBot.login()
hugoBot.curtir_fotos('memesBR')

