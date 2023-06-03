import time
from pyotp import TOTP
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USERID = 'your userid'
PASSWORD = 'your passwd'
TOTPQRCODE = 'your qr code'


class LoginAndAuthenticator:
    _user_id = USERID
    _password = PASSWORD
    _kite_connect_obj = None
    _sel_web_driver = None
    _totp_token = ''
    _request_token = ''

    def __init__(self, kite):
        self._kite_connect_obj = kite

    def _generate_totp(self):
        self._totp_token = TOTP(TOTPQRCODE).now()

    def _enter_userid_passwd(self):
        self._sel_web_driver = webdriver.Chrome()
        self._sel_web_driver.get(self._kite_connect_obj.login_url())
        time.sleep(1)
        self._sel_web_driver.find_element(By.ID, 'userid').send_keys(self._user_id)
        self._sel_web_driver.find_element(By.ID, 'password').send_keys(self._password)
        self._sel_web_driver.find_element(By.XPATH, '//button[text()="Login "]').click()

    def _enter_totp(self):
        self._generate_totp()
        totp_element = self._sel_web_driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
        totp_element.click()
        time.sleep(1)
        totp_element.send_keys(Keys.HOME)
        time.sleep(1)
        totp_element.send_keys(self._totp_token)
        print("TOPT is", self._totp_token)
        time.sleep(3)

    def _scalp_request_token(self):
        self._request_token = self._sel_web_driver.current_url.split('request_token=')[1][:32]

    def start_login_and_auth(self):
        self._enter_userid_passwd()
        self._enter_totp()
        self._scalp_request_token()

    def get_request_token(self):
        return self._request_token

