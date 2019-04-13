import webbrowser
from selenium import webdriver

# Open instance of Firefox, maximize the window, and open up Blackboard Sign
# in page.
# Change Firefox to Chrome or whatever as needed. (I have no clue how well other browsers work)
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://lowell.umassonline.net/webapps/bb-auth-provider-shibboleth-BBLEARN/execute/shibbolethLogin?returnUrl=https%3A%2F%2Flowell.umassonline.net%2Fwebapps%2Fportal%2Fexecute%2FdefaultTab&authProviderId=_8264_1")

# Find Username input field
username = driver.find_element_by_name("UserName")
# Add your username in the quotes below
username.send_keys("")

#Find Password input field
password = driver.find_element_by_name("Password")
# Add your password in the quotes below
password.send_keys("")

# Find submit button and click it
loginButton = driver.find_element_by_id("submitButton")
loginButton.click()

# Wait to allow for cookie agreement pop-up to appear, and then accept it
driver.implicitly_wait(5)
agree = driver.find_element_by_id("agree_button")
agree.click()
