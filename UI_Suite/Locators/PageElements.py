from selenium.webdriver.common.by import By

class LoginElements:
    LOGOUT = (By.LINK_TEXT, "Log Out")
    LOGIN = (By.LINK_TEXT, "Log In")
    USERNAME_INPUT = (By.XPATH, "//form[@method='post']/input[@id='username']")
    PASSWD_INPUT = (By.XPATH, "//form[@method='post']/input[@id='password']")
    ENTER = (By.XPATH, "//form[@method='post']/input[@value='Log In']")

class RegisterElements:
    REGISTER = (By.LINK_TEXT, "Register")
    USERNAME_INPUT = (By.XPATH, "//form[@method='post']/input[@id='username']")
    PASSWD_INPUT = (By.XPATH, "//form[@method='post']/input[@id='password']")
    FIRSTNAME_INPUT = (By.XPATH, "//form[@method='post']/input[@id='firstname']")
    FAMILYNAME_INPUT = (By.XPATH, "//form[@method='post']/input[@id='lastname']")
    PHONE_INPUT = (By.XPATH, "//form[@method='post']/input[@id='phone']")
    ENTER = (By.XPATH, "//form[@method='post']/input[@value='Register']")

class InformationTab:
    USERNAME = (By.XPATH, "//table[@id='content']/tbody//td[@id='username']")
    FIRSTNAME = (By.XPATH, "//table[@id='content']/tbody//td[@id='firstname']")
    LASTNAME = (By.XPATH, "//table[@id='content']/tbody//td[@id='lastname']")
    PHONE = (By.XPATH, "//table[@id='content']/tbody//td[@id='phone']")

class Alerts:
    SAME_USER = (By.XPATH, "//section[@class='content']/div[@class='flash'][contains(text(), 'is already registered')]")
    WRONG_CREDS = (By.XPATH, "//section[@class='content']/p[1][contains(text(), 'incorrect login details')]")
