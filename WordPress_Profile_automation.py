import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class WordPressProfile(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("C:\\Users\\SwaPrabhu\\Documents\\WebDrivers\\chromedriver.exe")

    def test_wordpress_profile(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.get('https://wordpress.com/me')
        self.assertIn("WordPress.com", driver.title)
        username_textbox = driver.find_element_by_id("usernameOrEmail")
        username_textbox.send_keys("automationt841")
        driver.implicitly_wait(10)
        driver.find_element_by_id("usernameOrEmail").send_keys(Keys.RETURN)
        password_textbox = driver.find_element_by_xpath("//*[@type='password'][@class='form-text-input']")
        password_textbox.send_keys("automationt841123")
        password_textbox.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        fname=driver.find_element_by_xpath("//input[@id='first_name']")
        fname.clear()
        fname.send_keys("Testing")
        lname=driver.find_element_by_xpath("//input[@id='last_name']")
        lname.clear()
        lname.send_keys("Site")
        dis_name=driver.find_element_by_xpath("//input[@id='display_name']")
        dis_name.clear()
        dis_name.send_keys("Automation1")
        describe_field=driver.find_element_by_xpath("//textarea[@id='description']")
        describe_field.clear()
        describe_field.send_keys("I am automating the profile page")
        time.sleep(2)
        toggle=driver.find_element_by_xpath("//input[@id='inspector-toggle-control-0']")
        toggle.click()
        time.sleep(2)
        submit_button=driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        time.sleep(2)
        tog_button=driver.find_element_by_xpath("//input[@id='inspector-toggle-control-0']")
        tog_button.click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        add_button=driver.find_element_by_css_selector("svg.gridicons-add-outline")
        add_button.click()
        time.sleep(2)
        add_wordpress=driver.find_element_by_css_selector("button.popover__menu-item")
        add_wordpress.click()
        time.sleep(2)
        cancel_button=driver.find_element_by_xpath("(//button[@type='submit'])[3]")
        cancel_button.click()
        time.sleep(2)
        add_button=driver.find_element_by_css_selector("svg.gridicons-add-outline")
        add_button.click()
        time.sleep(2)
        add_url_button=driver.find_element_by_css_selector("button.popover__menu-item:nth-child(2)")
        add_url_button.click()
        time.sleep(3)
        add_url_link=driver.find_element_by_xpath("//input[@name='value']")
        add_url_link.clear()
        add_url_link.send_keys("https://www.google.com")
        time.sleep(2)
        add_url_desc=driver.find_element_by_xpath("//input[@name='title']")
        add_url_desc.clear()
        add_url_desc.send_keys("Test site")
        time.sleep(2)

        cancel_button1=driver.find_element_by_xpath("(//button[@type='submit'])[3]")
        cancel_button1.click()
        time.sleep(3)

    def tearDown(self) -> None:    
        self.driver.close()

        

if __name__ == "__main__":
    unittest.main()
