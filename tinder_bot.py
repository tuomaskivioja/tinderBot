import undetected_chromedriver as uc
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

from login_details import email, password

class TinderBot():
    def __init__(self):
        # self.driver = webdriver.Chrome()
        self.driver = uc.Chrome(use_subprocess=True)
    def open_tinder(self):
        sleep(10)
        wait = WebDriverWait(self.driver, 20)
        url = 'https://accounts.google.com/ServiceLogin?service=accountsettings&continue=https://myaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button'
        self.driver.get(url)

        wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
        sleep(8)
        wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(password)
        sleep(600)
        print("Logged into Google: Going into Tinder...")
        self.driver.get('https://tinder.onelink.me/9K8a/3d4abb81')
        sleep(10)
        loginElement = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[1]')))
        print("loginElement is set. it is:")
        print(loginElement)
        sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[1]'))).click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[1]'))).send_keys(Keys.TAB + Keys.TAB + Keys.RETURN + Keys.RETURN + Keys.RETURN)
        sleep(20)
        # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[1]'))).send_keys(Keys.RETURN + Keys.RETURN + Keys.RETURN)

        try:
            base_window = self.driver.window_handles[0]
            google_popup_window = self.driver.window_handles[1]
            # switch to Google window
            self.driver.switch_to.window(google_popup_window)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div/main/div/div/div[1]/div[1]/div[1]'))).click()
            self.driver.switch_to.window(base_window)
        except:
            print('no window popup')

        print("Successfully logged into Tinder!")
        sleep(30)
        
        try:
            # allow_location_button = self.driver.find_element('xpath', '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[1]')
            allow_location_button = wait.until(EC.visibility_of_element_located((By.XPATH,  '/html/body/div[2]/main/div/div/div/div[3]/button[1]')))
            allow_location_button.click()
        except:
            print('no location popup')

        sleep(15)

        try:
            notifications_button = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
            notifications_button.click()
        except:
            print('no notification popup')


        try:
            dismiss_darkMode_button = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div[2]/button')
            dismiss_darkMode_button.click()
        except:
            print('dark mode popup did not happen')

    def right_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_RIGHT)
    def left_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_LEFT)

    def auto_swipe(self):
        while True:
            sleep(2)
            if self.driver.find_element('xpath', '/html/body/div[2]/main/div'): # XPATH /html/body/div[2]/main/div/div[2]/div/button[2]/div
                print("Out of Likes, messaging matches (if any)...")
                bot.send_messages_to_matches()
                sleep(5)
                print("Exiting...")
                break
            else:
                try:
                    self.right_swipe()
                except:
                    self.close_match()

                # div id=s1903812341 for out of likes

    def close_match(self):
        match_popup = self.driver.find_element('xpath', '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def get_matches(self):
        print("Getting matches..")
        match_profiles = self.driver.find_elements('class name', 'matchListItem')
        message_links = []
        for profile in match_profiles:
            if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute('href') == 'https://tinder.com/app/likes-you':
                continue
            else:
                print('no matches :(')
            message_links.append(profile.get_attribute('href'))
        return message_links

    def send_messages_to_matches(self):
        links = self.get_matches()
        message_list = ["Hi", "Hey what's up?", "Hey :)", "How's it going?"]
        for link in links:
            print("Original list is : " + str(message_list))
            rand_idx = random.randrange(len(message_list))
            random_message = message_list[rand_idx]
            print("First message is: " + str(random_message))
            self.send_message(link, random_message)

    def send_message(self, link, random_message):
        self.driver.get(link)
        sleep(3)
        text_area = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')

        text_area.send_keys(random_message)

        text_area.send_keys(Keys.ENTER)

bot = TinderBot()
bot.open_tinder()
sleep(30)
bot.auto_swipe()
# bot.send_messages_to_matches()