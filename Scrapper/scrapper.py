from selenium import webdriver
from selenium.webdriver import ActionChains
import os
import time
import Constant.constant


class Scrapper:
    __instance = None
    
    def __init__(self):
        base_path = os.getcwd()
        chrome_driver_path = base_path +"/" +"Config" +"/"+"chromedriver"
        self.scrapper_driver=  webdriver.Chrome(chrome_driver_path)
    
    def performEachOperation(self,task):
        print(task)
        element = self.scrapper_driver.find_element_by_xpath(task[Constant.constant.XPATH])
        if task[Constant.constant.OPERATION] == Constant.constant.CLICK:
            element.click()
        elif task[Constant.constant.OPERATION] == Constant.constant.PUSH_DATA:
            element.send_keys(task[Constant.constant.DATA])
        elif task[Constant.constant.OPERATION]== Constant.constant.UPLOAD_FILE:
            self.scrapper_driver.maximize_window()
            element.send_keys(task[Constant.constant.DATA])

    def performPageOperation(self,operationData):
        print(operationData)
        for task in operationData[Constant.constant.TASK]:
            self.performEachOperation(task)
            time.sleep(1)


    def startScrapping(self,scrappingdeatils):
        try:
            self.scrapper_driver.get(scrappingdeatils[Constant.constant.URL])
            time.sleep(5)
            pages = scrappingdeatils[Constant.constant.PAGES]
            for page in pages:
                self.performPageOperation(page)
                time.sleep(5)
        except Exception as e:
            print(e)
        finally:
            self.scrapper_driver.close()
            self.scrapper_driver.quit()
            



    
