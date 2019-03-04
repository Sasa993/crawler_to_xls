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
    	lista = {}
    	lista2 = []
    	brojac = 0

    	driver = self.driver
    	driver.get("https://www.malioglasi.com")

    	grupa_oglasa = Select(driver.find_element_by_name("grupar"))
    	grupa_oglasa.select_by_visible_text("Stanovi")

    	tip_oglasa = Select(driver.find_element_by_name("tipr"))
    	tip_oglasa.select_by_visible_text("Izdavanje")

    	grad = Select(driver.find_element_by_name("gradr"))
    	grad.select_by_visible_text("Banjaluka")
    	
    	driver.find_element_by_xpath("//input[@value='Pretraži']").click()

    	tihin_broj = "497-795"

    	while(True):
    		try:
    			driver.find_element_by_xpath("//img[@src='../nlimages/or.gif']").click()
    			oglas_sadrzaj = driver.find_elements_by_xpath("//span[@class='crveni']/parent::div/parent::div/parent::td/parent::tr/preceding-sibling::tr[1]")
    			oglas_broj_telefona = driver.find_elements_by_xpath("//span[@class='crveni']")
    			oglas_datum_vrijeme_objave = driver.find_elements_by_xpath("//span[@class='crveni']/parent::div/parent::div/parent::td/parent::tr/following-sibling::tr")

		    	for x, y, z in zip(oglas_sadrzaj, oglas_broj_telefona, oglas_datum_vrijeme_objave):
		    		isjeckan_z = z.text.split('|')[1]

		    		lista[brojac] = {}
		    		lista[brojac]['oglas_sadrzaj'] = x.text
		    		lista[brojac]['oglas_broj_telefona'] = y.text
		    		lista[brojac]['oglas_datum_vrijeme_objave'] = isjeckan_z

		    		brojac += 1

    		except NoSuchElementException:
    			break

    	for x in range(brojac):
    		print("{0}.\nSadrzaj:\n{1}Telefon:\n{2}\nDatum i vrijeme:\n{3}\n".format(x, lista[x]['oglas_sadrzaj'], lista[x]['oglas_broj_telefona'], lista[x]['oglas_datum_vrijeme_objave']))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()