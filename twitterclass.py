from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER = "https://x.com/home"
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_ACCOUNT_ID = "YOUR ACCOUNT ID"
TWITTER_PASSWORD = "YOUR PASSWORD"
INTERNET = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.int_download = 0
        self.int_upload = 0



    def open_twitter(self):
        self.driver.get(url=TWITTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div[1]/div/div/div/div[2]/button[1]/div/span/span').click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div[2]/div/div/div/button').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div').click()
        time.sleep(3)
        twitter = self.driver.find_element(By.XPATH,
                                           value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        twitter.send_keys(TWITTER_EMAIL)
        time.sleep(4)
        twitter.send_keys(Keys.ENTER)
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_ACCOUNT_ID)
        time.sleep(5)
        username.send_keys(Keys.ENTER)
        time.sleep(4)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        time.sleep(8)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        if self.int_upload < 200 or self.int_download < 200:
            time.sleep(5)
            post = self.driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            post.send_keys(f"My internet upload speed is {self.int_upload} and download speed is {self.int_download}")
            time.sleep(8)
            post_click = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()
        print(self.driver.title)
        time.sleep(4)

    def open_ookla(self):
        self.driver.get(url=INTERNET)
        time.sleep(3)
        self.driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, value="start-text").click()
        time.sleep(25)
        download_speed = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.int_download = float(download_speed)
        time.sleep(15)
        upload_speed = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        self.int_upload = float(upload_speed)
        print(type(self.int_download))
        print(type(self.int_upload))
        print(self.int_upload)
        print(self.int_download)



