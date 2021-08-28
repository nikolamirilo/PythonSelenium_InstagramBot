from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from secrets import instagram_username, instagram_password

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like_posts(self,hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)
        for i in range(1,4):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            posts = bot.find_elements_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]/a[1]')
            links = [elem.get_attribute("href") for elem in posts]
            for link in links:
                bot.get(link)
                try:
                    bot.find_elements_by_xpath('//button[@class="wpO6b  "]')[1].click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)

pd = InstagramBot(instagram_username, instagram_password)
pd.login()
pd.like_posts('nature')