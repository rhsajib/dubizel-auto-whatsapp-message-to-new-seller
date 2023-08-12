import time
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchWindowException
from lib.contrib import create_sent_message_data, get_cache_data, new_car_ads
from lib.sender import msg_to_seller_and_client
from lib.core import get_cars_info, get_price_url_phonenumber_data
from lib.settings import LIST_OF_URLS_TO_SCAN, TIME_INTERVAL, CHROME_PROFILE_PATH
    




def main():
    try:
        while True:
            # set up the Chrome options            
            options = uc.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("--disable-popup-blocking")   # for allowing chrome to open a blank new tab
            # options.add_argument(CHROME_PROFILE_PATH)          # path for whatsapp data 
            driver = uc.Chrome(options=options, use_subprocess=True)

            # open the webpage in chrome driver
            driver.get('https://www.google.com/')

            driver.implicitly_wait(10)
            wait = WebDriverWait(driver, 30)
        
            # selecting the current window as main tab
            main_tab = driver.current_window_handle
            
            for url in LIST_OF_URLS_TO_SCAN:

                # open a blank new tab
                # set options.add_argument("--disable-popup-blocking") 
                # for allowing chrome to open a blank new tab
                driver.execute_script("window.open(''),'_blannk';")

                # switch to the new tab
                driver.switch_to.window(driver.window_handles[-1])
                          
                driver.get(url)                
                time.sleep(3)

                # getting all cars information of first page
                cars_info = get_cars_info(driver)

                # closing current tab & Switch back to the original tab (main tab)
                driver.close()
                driver.switch_to.window(main_tab)

                time.sleep(3)     

                # get previously sent messeages client data
                cache_data = get_cache_data()
                
                # filter new car ads
                new_car_ads_list = new_car_ads(cars_info, cache_data)

                if not new_car_ads_list:
                    continue

                # creating data list where the script will send messages
                price_url_phonenumber_data = get_price_url_phonenumber_data(new_car_ads_list, driver=driver)

                # sending messages to new seller and client  
                sent_message_list = msg_to_seller_and_client(price_url_phonenumber_data, driver=driver)             
                
                #---------------------------------------------------------------------------------------------
                # only for test purpose

                # to understand the format of seller phone number (if it raises any exception)   
                # pd.DataFrame(price_url_phonenumber_data).to_csv('price_url_phonenumber_data.csv', index=False)               
        
                # to compare price_url_phonenumber_data and sent_message_list
                # pd.DataFrame(sent_message_list).to_csv('new_sent_message_list.csv', index=False)
                #---------------------------------------------------------------------------------------------
                
                create_sent_message_data(sent_message_list, cache_data)

            time.sleep(60*TIME_INTERVAL)  # time interval in minutes

    except KeyboardInterrupt:
        print('|-------------------------------------------|')
        print('| Someone intentionally stopped the program |')
        print('|-------------------------------------------|')

    except NoSuchWindowException:
        print('|---------------------------------------------|')
        print('| Someone intentionally stopped Chrome Driver |')
        print('|---------------------------------------------|')