import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Stan(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_one(self):
    	driver = self.driver
    	driver.get("https://www.malioglasi.com")
    	# grupa_oglasa = driver.find_element_by_xpath("//select[@name='grupar']")
    	# options_grupa_oglasa = grupa_oglasa.find_elements_by_tag_name("option")
    	grupa_oglasa = Select(driver.find_element_by_name("grupar"))
    	grupa_oglasa.select_by_visible_text("Stanovi")

    	tip_oglasa = Select(driver.find_element_by_name("tipr"))
    	tip_oglasa.select_by_visible_text("Izdavanje")
#066 497 795
    	grad = Select(driver.find_element_by_name("gradr"))
    	grad.select_by_visible_text("Banjaluka")

    	# driver.find_element_by_value("Pretraži").click()
    	driver.find_element_by_xpath("//input[@value='Pretraži']").click()

    	broj_telefona = "262-557"
    	kita = driver.find_elements_by_css_selector("span.crveni")
    	for x in kita:
    		if (broj_telefona in x.text):
    			print("YEAH! Evo ga: " + str(x.text))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()