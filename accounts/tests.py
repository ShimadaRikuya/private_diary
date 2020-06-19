from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver


class TestLogin(LiveServerTestCase):

    @classmethod
    def SetUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='/Users/user/Downloads/chromedriver')

    @classmethod
    def tearDownClass(cls):
        cls.selenium = WebDriver(executable_path='/Users/user/Downloads/chromedriver').quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        # ログイン
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys('maeda@gmail.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('keizi1234')
        self.selenium.find_element_by_class_name('btn').click()

        # ページタイトルの検証
        self.assertEqual('日記一覧 | Private Diary', self.selenium.title)
