
from selenium.webdriver.common.keys import Keys



# command for line break
L_BREAK = (Keys.SHIFT)+(Keys.ENTER)+(Keys.SHIFT)   

def seller_message(url):
    message =   'Hi, I am interested by your car posted at this ' + url + L_BREAK + L_BREAK + \
                'Could you please send me your location? '\
                'I also need the VIN number. When can I come to try it out?' + L_BREAK + L_BREAK + \
                'Thank you and have a good day!'
       
    return message



    
def client_message(url, price, seller_message = False):   
    message_body = 'URL of the car ad: ' + url + L_BREAK + \
                    'Price: ' + str(price) + ' AED' 
    
    if seller_message:
        message = message_body

    else:
        message = 'Note: This seller does not use Whatsapp.' + L_BREAK + L_BREAK + message_body
    
    return message
                            

