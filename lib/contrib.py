import pandas as pd



def get_cache_data():

    # get previously sent messeages client data (data where messages were sent)
    cache_data = pd.read_csv('temp/sent_messages_data.csv')
    return cache_data
                



def create_sent_message_data(message_list, cache_data):

    # adding new_car_ad_list with previous cache data (sellers data who received whatsapp messages)    
    df = pd.DataFrame(message_list)
    new_cache_data = pd.concat([df, cache_data], axis=0)

    new_cache_data.to_csv('temp/sent_messages_data.csv', index = False)




def new_car_ads(cars_info, data):

    # list of all urls from cache data
    url_cache = data['car_ad_url'].tolist()

    # new car ads
    ads_list = [info for info in cars_info if info['car_ad_url'] not in url_cache] 
    return ads_list
