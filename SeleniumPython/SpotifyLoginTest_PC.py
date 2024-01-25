import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SpotifyLogin_PC(unittest.TestCase):

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
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[1]/span[1]").click()
        time.sleep(6)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
