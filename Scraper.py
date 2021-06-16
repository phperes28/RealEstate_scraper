from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


WEBSITE = "https://www.wimoveis.com.br/apartamentos-venda-aguas-claras-df-mais-de-3-banheiros-3-quartos-mais-de-1-vaga-100-130-m2.html"
FORM = "your_form_url"


class Scraper:

    def __init__(self):
        chrome_driver_path = "E:\Documentos\Development\chromedriver.exe"   #Your driver path here
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()
        self.price_list = []
        self.address_list = []
        self.all_info = []
        self.all_links =[]


    def get_info(self):
        """Gets Addresses, info, prices and link from realestate ads"""

        self.driver.get(WEBSITE)
        time.sleep(3)
        self.driver.find_element_by_xpath("""//*[@id="modalContent"]/div/button/i""").click()
        time.sleep(3)
        #gets prices and appends to list
        all_prices = self.driver.find_elements_by_class_name("firstPrice")
        for price in all_prices:
            text = price.text
            new_p = text.replace(".", "")
            price_int = int(new_p.split(" ")[1])
            self.price_list.append(price_int)
        #gets addresses
        all_addresses = self.driver.find_elements_by_class_name("postingCardLocationTitle")
        for address in all_addresses:
            self.address_list.append(address.text)
        print(self.address_list)
        # gets info
        ad_info = self.driver.find_elements_by_css_selector("a.go-to-posting")
        for info in ad_info:
            links = info.get_attribute('href')   #gets href link inside the css
            self.all_links.append(links)
            self.all_info.append(info.text)

        # Just for tests
        print(self.price_list)
        print(self.all_info)
        print(self.all_links)

    def fill_listing(self):
        """Fills google form with information from the lists """
        self.driver.get(FORM)
        for i in range(len(self.all_links)):

            time.sleep(3)
            question_1 = self.driver.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input""")
            question_1.send_keys(self.address_list[i])
            question_1.send_keys(Keys.TAB)
            question_2 = self.driver.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input""")
            question_2.send_keys(self.price_list[i])
            question_2.send_keys(Keys.TAB)
            question_3 = self.driver.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input""")
            question_3.send_keys(self.all_info[i])
            question_3.send_keys(Keys.TAB)
            question_4 = self.driver.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input""")
            question_4.send_keys(self.all_links[i])
            send = self.driver.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span""").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div[1]/div/div[4]/a""").click()









