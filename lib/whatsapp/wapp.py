import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException



def validate_phone(phn):
    # UAE phone number = country_code + last 9 digits.
    # for example +971 123456789
    # for BD +880 1234567890

    p_number = '+880' + phn[-10:] 
    return p_number





def create_whats_app_url(phone):
    url = 'https://web.whatsapp.com/send?phone=' + phone + '&text=&app_absent=1'  
    return url





def send_whatsapp_messages(phone, message, driver=None, status=False):
    """
    : whatsapp web will require scan option for login
    : for auto login we have to use cookies and data of our chrome browser
    : this can be done using ChromeOptions (it will load data from our previous login to chrome browser)
    """ 

    # open a blank new tab
    driver.execute_script("window.open(''),'_blannk';")

    # switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    valid_phone = validate_phone(phone)
    whats_app_url = create_whats_app_url(valid_phone)
             
    driver.get(whats_app_url)                

    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 60)

    
    try:
        # search_box_path = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]'           # search box path to input number
        message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'  # message box xpath

        driver.find_element(By.XPATH, message_box_path)
        # if there is no such element it will raise NoSuchElementException  

        message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))           
    
        # write message in message box and send it
        message_box.send_keys(message + Keys.ENTER)
        time.sleep(3)

        # hashing status for sending message
        status = True
        
    except NoSuchElementException:       
            # after proceding to this exception, it will try to find ok button
            # if ok button does not exist, it will raise another NoSuchElementException

            try:
                ok_button_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button'

                # find ok button
                ok_button = driver.find_element(By.XPATH, ok_button_xpath)

                # click the 'Ok' button of popup window
                ok_button.click()
                
            except NoSuchElementException:
                pass  

    # closing current tab & Switch back to the original tab (main tab)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return status
            




    
    