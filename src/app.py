import time
from userinfo import username, password

# We define modules related to Selenium ↓

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Arguments you can use.
"""
# These are the attributes available for By class:

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

# These are the various ways the attributes are used to locate elements on a page:

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

For more information => https://selenium-python.readthedocs.io/locating-elements.html
"""

class Github(object):
    def __init__(self):
        self.browseR = webdriver.Chrome("src/chromedriver") # If you are using google chrome, don't touch it. If you are using another browser, don't forget to download and identify the driver for that browser!
        self.urlA = "https://github.com/"
        self.usernameG = username
        self.passwordE = password

    def login(self):
        
        #####################################
        # You can remove this part. Advertisement of my own page :)
        self.browseR.get("https://salihkayatemir.cf") # You can remove this part. Advertisement of my own page :)
        self.browseR.maximize_window() # You can remove this part. Advertisement of my own page :)
        time.sleep(5) # You can remove this part. Advertisement of my own page :)
        #####################################
        
        # Username section
        self.browseR.get(self.urlA+"login")
        self.browseR.maximize_window()
        username = self.browseR.find_element(By.ID , "login_field")
        password = self.browseR.find_element(By.ID , "password")
        enterButton = self.browseR.find_element(By.NAME , "commit")
        time.sleep(2)
        # command processing part
        username.send_keys(self.usernameG)
        password.send_keys(self.passwordE)
        enterButton.send_keys(Keys.ENTER)
        time.sleep(2)
        self.browseR.get(self.urlA+"salihkayatemir") # You can use the command "(self.urlA+self.usernameG)" to go to your own page.

    def findRepositories(self):
        self.browseR.get(self.urlA)
        self.browseR.maximize_window()
        time.sleep(1)
        searchButton = self.browseR.find_element(By.NAME, "q")
        searchButton.send_keys("salihkayatemir") # Enter the keyword you want to search for.
        searchButton.send_keys(Keys.ENTER)  

    def deletePage(self):
        time.sleep(5)
        self.browseR.close()
        
       
app = Github()
app.login() # => To deactivate the "login" method, simply put "#" before it.
# app.findRepositories() # => To enable the "findRepositories" method, simply delete "#"

# Automatically closes the page after 40 seconds.
time.sleep(10*4)
app.deletePage()


    
