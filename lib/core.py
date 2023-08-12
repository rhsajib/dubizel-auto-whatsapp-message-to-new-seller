import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from random import randint
from lib.settings import CAR_ADS_LIST_CSS_SELECTOR, PRICE_CSS_SELECTOR




def get_cars_info(driver):
    """ 
    : this function will only return the cars info of first page
    """ 
    
    # car ads list
    car_ads_list = driver.find_elements(By.CSS_SELECTOR, CAR_ADS_LIST_CSS_SELECTOR)

    cars_info = []
    for car_add in car_ads_list:

        dic = {} 

        # get car url
        url_element = car_add.find_element(By.TAG_NAME, 'a')
        url = url_element.get_attribute('href')


        # get car price
        price_element = car_add.find_element(By.CSS_SELECTOR, PRICE_CSS_SELECTOR).text
        price = int(''.join(price_element.strip().split(',')))
              
        dic['car_ad_url'] = url
        dic['car_price'] = price

        cars_info.append(dic) 
    
    return cars_info






def get_phone_number(car_ad_url, driver=None): 
    """
    : here, phn_num_button class changes over time 
    """

    # open a blank new tab
    driver.execute_script("window.open(''),'_blannk';")

    # switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
                
    driver.get(car_ad_url)                
    time.sleep(3)    
               
    try:
        # find the phone number

        all_button_selector = 'button.sc-161sydf-1.iTrmhH.dpv-cta' 

        elements = driver.find_elements(By.CSS_SELECTOR, all_button_selector)   

        # check if phone number button is available or not
        button_elements = [elm.text for elm in elements]

        if 'Show Phone Number'in button_elements:   
            for element in elements: 
                # getting exact element of phone number
                if element.text == 'Show Phone Number':        
                    element.click()                        
                    time.sleep(5)                     
                    dialog_box_selector = 'a.sc-1wygika-0.fIXdhU.sc-fl9rht-5.fhQGYI' 
                    # class = 'sc-1wygika-0 fIXdhU sc-fl9rht-5 fhQGYI'
                    try:
                        phone_showed = driver.find_element(By.CSS_SELECTOR, dialog_box_selector).text
                    
                    except NoSuchElementException:
                        phone_showed = 'unavailable'
        else:
            phone_showed = 'unavailable'
    
    except NoSuchElementException:
        phone_showed = 'unavailable'
     

    # close current tab
    driver.close() 

    # Switch back to the original tab (main tab)
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(randint(2, 6))  

    return (phone_showed)






def get_price_url_phonenumber_data(ads, driver=None):
    """
    : ads is a list
    """

    price_url_phonenumber = []
    for ad in ads:
        dic = {}

        dic['car_price'] = ad['car_price']
        dic['car_ad_url'] = ad['car_ad_url']

        phone_number = get_phone_number(ad['car_ad_url'], driver = driver)
        dic['seller_phone_number'] = phone_number
        
        price_url_phonenumber.append(dic)
    return price_url_phonenumber






    


                