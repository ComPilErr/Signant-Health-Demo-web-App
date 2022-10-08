from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Locators.PageElements import LoginElements, RegisterElements, InformationTab, Alerts

class ChromeLib:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, url = 'http://127.0.0.1:6969', version = '90.0.4430.24') -> None:
        self.driver = None
        self.url = url
        self.version = version

    def start(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--start-maximized")
        options.add_argument('--headless')
        options.add_argument("window-size=800,600")
        self.driver = webdriver.Chrome(options = options, executable_path=ChromeDriverManager(version = self.version).install())
        self.driver.implicitly_wait(10)

    def catch_same_user_alert(self):
        text = self.driver.find_element(*Alerts.SAME_USER).text
        print(text)
        return text

    def catch_wrong_creds_alert(self):
        text = self.driver.find_element(*Alerts.WRONG_CREDS).text
        print(text)
        return text

    def get_username(self):
        text = self.driver.find_element(*InformationTab.USERNAME).text
        print(text)
        return text

    def get_firstname(self):
        text = self.driver.find_element(*InformationTab.FIRSTNAME).text
        print(text)
        return text

    def get_lastname(self):
        text = self.driver.find_element(*InformationTab.LASTNAME).text
        print(text)
        return text

    def get_phone(self):
        text = self.driver.find_element(*InformationTab.PHONE).text
        print(text)
        return text

    def click_on_logout(self):
        self.driver.find_element(*LoginElements.LOGOUT).click()

    def click_on_login(self):
        self.driver.find_element(*LoginElements.LOGIN).click()

    def fill_login_username(self, name=""):
        self.driver.find_element(*LoginElements.USERNAME_INPUT).send_keys(name)

    def fill_login_passw(self, passw=""):
        self.driver.find_element(*LoginElements.PASSWD_INPUT).send_keys(passw)

    def perform_login(self):
        self.driver.find_element(*LoginElements.ENTER).click()

    def click_on_register(self):
        self.driver.find_element(*RegisterElements.REGISTER).click()

    def fill_register_username(self, name=""):
        self.driver.find_element(*RegisterElements.USERNAME_INPUT).send_keys(name)

    def fill_register_passw(self, passw=""):
        self.driver.find_element(*RegisterElements.PASSWD_INPUT).send_keys(passw)

    def fill_register_first_name(self, name=""):
        self.driver.find_element(*RegisterElements.FIRSTNAME_INPUT).send_keys(name)

    def fill_register_family_name(self, name=""):
        self.driver.find_element(*RegisterElements.FAMILYNAME_INPUT).send_keys(name)

    def fill_register_phone_number(self, phone=""):
        self.driver.find_element(*RegisterElements.PHONE_INPUT).send_keys(phone)

    def perform_register(self):
        self.driver.find_element(*RegisterElements.ENTER).click()

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def switch_to(self):
        return self.driver.switch_to

    def get_title(self):
        print(f"Here is the title: {self.driver.title}")
        return self.driver.title

    def close(self):
        if self.driver != None:
            self.driver.quit()
        print("Everything is terminated. See you soon.")

