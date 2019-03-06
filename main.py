import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.common.by import By
from xlwt import Workbook, easyxf
from xlwt.Utils import rowcol_to_cell

class Stan(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_one(self):
    	#excel stuff
    	book = Workbook()
    	first_sheet = book.add_sheet('Prvi Sheet')

    	first_row_style = easyxf('pattern: pattern solid, fore_colour aqua; borders: bottom thick, left thin, right thin, bottom_colour blue_gray, left_colour blue_gray, right_colour blue_gray; font: bold True, height 240; alignment: horizontal center, vertical center')
    	column_first_style = easyxf('alignment: horizontal center, vertical center, wrap True; pattern: pattern solid, fore_colour gray40; font: colour white; borders: bottom thin, top thin, top_colour black, bottom_colour gray80')
    	column_second_style = easyxf('alignment: horizontal center, vertical center, wrap True; pattern: pattern solid, fore_colour gray25; borders: left thin, top thin, right thin, left_colour gray80, top_colour black, right_colour gray80')

    	first_sheet.col(2).width = 1500
    	first_sheet.col(3).width = 12000
    	first_sheet.col(4).width = 6000
    	first_sheet.col(5).width = 5000
    	first_sheet.col(6).width = 5000
    	first_sheet.row(2).height = 500
    	first_row = first_sheet.row(2)
    	first_row.write(2, 'Br.', first_row_style)
    	first_row.write(3, 'Sadrzaj', first_row_style)
    	first_row.write(4, 'Broj Telefona', first_row_style)
    	first_row.write(5, 'Datum', first_row_style)
    	first_row.write(6, 'Vrijeme', first_row_style)

    	lista = {}
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
    	# kita = True
    	while(True):
    		try:
    			driver.find_element_by_xpath("//img[@src='../nlimages/or.gif']").click()
    			oglas_sadrzaj = driver.find_elements_by_xpath("//span[@class='crveni']/parent::div/parent::div/parent::td/parent::tr/preceding-sibling::tr[1]")
    			oglas_broj_telefona = driver.find_elements_by_xpath("//span[@class='crveni']")
    			oglas_datum_vrijeme_objave = driver.find_elements_by_xpath("//span[@class='crveni']/parent::div/parent::div/parent::td/parent::tr/following-sibling::tr")

		    	for x, y, z in zip(oglas_sadrzaj, oglas_broj_telefona, oglas_datum_vrijeme_objave):
		    		isjeckan_datum = z.text.split('|')[1].split(' ')[1]
		    		isjeckan_vrijeme = z.text.split('|')[1].split(' ')[2]

		    		lista[brojac] = {}
		    		lista[brojac]['oglas_sadrzaj'] = x.text
		    		lista[brojac]['oglas_broj_telefona'] = y.text
		    		lista[brojac]['oglas_datum_objave'] = isjeckan_datum
		    		lista[brojac]['oglas_vrijeme_objave'] = isjeckan_vrijeme

		    		brojac += 1
		    	# kita = False

    		except NoSuchElementException:
    			break

    	for x in range(brojac):
    		first_sheet.row(x + 3).write(2, "{0}.".format(x + 1), column_second_style)
    		first_sheet.row(x + 3).height = 2000
    		first_sheet.row(x + 3).write(3, lista[x]['oglas_sadrzaj'], column_first_style)
    		first_sheet.row(x + 3).write(4, lista[x]['oglas_broj_telefona'],column_second_style)
    		first_sheet.row(x + 3).write(5, lista[x]['oglas_datum_objave'], column_first_style)
    		first_sheet.row(x + 3).write(6, lista[x]['oglas_vrijeme_objave'], column_second_style)

    		# print("{0}.\nSadrzaj:\n{1}Telefon:\n{2}\nDatum i vrijeme:\n{3}\n".format(x, lista[x]['oglas_sadrzaj'], lista[x]['oglas_broj_telefona'], lista[x]['oglas_datum_vrijeme_objave']))

    	book.save('testiramo.xls')

    # def test_two(self):
    # 	book = Workbook()

    # 	first_sheet = book.add_sheet('Kurcina')
    # 	# first_sheet.write(0, 0, 'A1')
    # 	# first_sheet.write(0, 1, 'B1')
    # 	first_row_style = easyxf('pattern: pattern solid, fore_colour aqua; borders: bottom thick, left thin, right thin, bottom_colour blue_gray, left_colour blue_gray, right_colour blue_gray; font: bold True, height 240; alignment: horizontal center, vertical center')
    # 	column_style = easyxf('alignment: wrap True')

    # 	# for i in range(0, 10, 2):
    # 	# 	first_sheet.row(i).set_style(first_row_style)
    # 	first_row = first_sheet.row(0)
    # 	first_sheet.col(0).width = 1500
    # 	first_sheet.col(1).width = 6500
    # 	first_sheet.col(2).width = 5000
    # 	first_sheet.col(3).width = 4000
    # 	first_sheet.col(4).width = 4000
    # 	first_sheet.row(0).height = 500
    # 	first_row.write(0, 'Br.', first_row_style)
    # 	first_row.write(1, 'Sadrzaj', first_row_style)
    # 	first_row.write(2, 'Broj Telefona', first_row_style)
    # 	first_row.write(3, 'Datum', first_row_style)
    # 	first_row.write(4, 'Vrijeme', first_row_style)
    # 	first_sheet.col(1).set_style(column_style)
    # 	#column_style cu morati prikaciti na svaki unos/celiju
    # 	# first_sheet.col(0).width = 10000
    # 	# first_sheet.row(0).height = 10000

    # 	book.save('testiramo2.xls')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()