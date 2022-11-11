import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from login_details import email, password

class TinderBot():
    def open_tinder(self):
        # self.driver = uc.Chrome(use_subprocess=True)
        self.driver = webdriver.Chrome()
        # wait = WebDriverWait(self.driver, 20)
        # url = 'https://accounts.google.com/ServiceLogin?service=accountsettings&continue=https://myaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button'
        # self.driver.get(url)

        # wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
        # sleep(5)
        # wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(password)
        # sleep(15)
        # print("You're in. Going into Tinder...")

        self.driver.get('https://tinder.com')
        sleep(5)

        # login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        login.click()
        sleep(1)
        # self.facebook_login()
        self.google_login()

        sleep(6)
        try:
            allow_location_button = self.driver.find_element('xpath', '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[1]')
            allow_location_button.click()
        except:
            print('no location popup')

        try:
            notifications_button = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
            notifications_button.click()
        except:
            print('no notification popup')
    
    def google_login(self):
        # find and click FB login button
        # login_with_facebook = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
        # login_with_facebook.click()
        login_with_google = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
        login_with_google.click()

        
        # save references to main and FB windows
        sleep(20)
        base_window = self.driver.window_handles[0]
        google_popup_window = self.driver.window_handles[1]
        # switch to Google window
        self.driver.switch_to.window(google_popup_window)

        # find enter email, password, login
        cookies_accept_button = self.driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]')
        cookies_accept_button.click()

    #     # login to FB

    #     email_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
    #     pw_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
    #     login_button = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
    #     # enter email, password and login
    #     email_field.send_keys(email)
    #     pw_field.send_keys(password)
    #     login_button.click()
    #     self.driver.switch_to.window(base_window)

    # def right_swipe(self):
    #     doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
    #     doc.send_keys(Keys.ARROW_RIGHT)
    # def left_swipe(self):
    #     doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
    #     doc.send_keys(Keys.ARROW_LEFT)

    # def auto_swipe(self):
    #     while True:
    #         sleep(2)
    #         try:
    #             self.right_swipe()
    #         except:
    #             self.close_match()

    # def close_match(self):
    #     match_popup = self.driver.find_element('xpath', '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    #     match_popup.click()

    # def get_matches(self):
    #     match_profiles = self.driver.find_elements('class name', 'matchListItem')
    #     message_links = []
    #     for profile in match_profiles:
    #         if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute('href') == 'https://tinder.com/app/likes-you':
    #             continue
    #         message_links.append(profile.get_attribute('href'))
    #     return message_links

    # def send_messages_to_matches(self):
    #     links = self.get_matches()
    #     for link in links:
    #         self.send_message(link)

    # def send_message(self, link):
    #     self.driver.get(link)
    #     sleep(2)
    #     text_area = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')

    #     text_area.send_keys('hi')

    #     text_area.send_keys(Keys.ENTER)

bot = TinderBot()
bot.open_tinder()