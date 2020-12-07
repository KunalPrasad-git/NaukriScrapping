import Scrapper.scrapper
import JsonHelper.jsonhelper
import Constant.constant
import time



def main():
    jsonhelperobj  = JsonHelper.jsonhelper.JsonHelper.getInstance()
    if jsonhelperobj is not None:
        config_data  = jsonhelperobj.readJson(Constant.constant.CONFIG_FILE_PATH)
        while True:
            scraperObj= Scrapper.scrapper.Scrapper()
            scraperObj.startScrapping(config_data)
<<<<<<< HEAD
            time.sleep(Constant.constant.NEXT_SCRAPPING_WAIT_TIME)
=======
            time.sleep(900)

>>>>>>> d68d40963db6c8eed5fcd8cd9200672b8841f09f
if __name__ == "__main__":
    main()
