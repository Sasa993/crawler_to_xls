import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.common.by import By

class Stan(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_one(self):
    	lista = []

    	driver = self.driver
    	driver.get("https://www.malioglasi.com")

    	grupa_oglasa = Select(driver.find_element_by_name("grupar"))
    	grupa_oglasa.select_by_visible_text("Stanovi")

    	tip_oglasa = Select(driver.find_element_by_name("tipr"))
    	tip_oglasa.select_by_visible_text("Izdavanje")

    	grad = Select(driver.find_element_by_name("gradr"))
    	grad.select_by_visible_text("Banjaluka")
    	
    	driver.find_element_by_xpath("//input[@value='Pretraži']").click()

    	broj_telefona = "497-795"

    	while(True):
    		try:
    			driver.find_element_by_xpath("//img[@src='../nlimages/or.gif']").click()
    			svi_brojevi_telefona = driver.find_elements_by_css_selector("span.crveni")

		    	for x in svi_brojevi_telefona:
		    		lista.append(x.text)

    		except NoSuchElementException:
    			break

    	print(lista)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()