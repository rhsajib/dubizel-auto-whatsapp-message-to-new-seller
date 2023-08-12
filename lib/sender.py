
import os
from lib.whatsapp.messages import client_message, seller_message
from lib.whatsapp.wapp import send_whatsapp_messages
from dotenv import load_dotenv

load_dotenv()


def msg_to_seller_and_client(price_url_phonenumber_data, driver=None):
    # a list of car ads which sellers received messages
    sent_message_to_seller_list = []

    for data in price_url_phonenumber_data:

        car_price = data['car_price']
        url = data['car_ad_url']
        seller_phone = data['seller_phone_number']

        
        # send message to seller
        s_message = seller_message(url)
        seller_status = send_whatsapp_messages(seller_phone, s_message, driver=driver)
        data['seller_message_status'] = seller_status

        
        # send message to client
        client_phone = os.environ.get('CLIENT_PHONE_NUMBER')
        c_message = client_message(client_phone, car_price, seller_message=seller_status)
        client_status = send_whatsapp_messages(seller_phone, c_message, driver=driver)
        data['client_message_status'] = client_status

        
        if data['seller_message_status'] == True:
            sent_message_to_seller_list.append(data)
        
    return sent_message_to_seller_list