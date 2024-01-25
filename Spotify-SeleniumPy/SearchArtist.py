import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchArtist(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login_validcred(self):
        self.driver.get("https://www.spotify.com/")
        self.driver.find_element(By.XPATH, "//header/div[4]/div[3]/button[2]").click()
        self.driver.find_element(By.XPATH, "//input[@id='login-username']").send_keys("lyjtuegief@isecmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='login-password']").send_keys("Password-123")
        self.driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(8)

    def test_search_artist(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
        self.driver.find_element(By.XPATH, "//header/div[3]/div[1]/div[1]/form[1]/input[1]").send_keys("Taylor Swift")
        self.driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[4]").click()
        scrl = self.driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/section[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]")
        scrl.location_once_scrolled_into_view
        self.driver.find_element(By.XPATH, "//div[contains(text(),'See more')]").click()
        time.sleep(6)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Finish!")
