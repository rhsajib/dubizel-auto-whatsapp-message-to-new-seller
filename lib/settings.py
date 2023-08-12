
# if you want to insert an url in the LIST_OF_URLS_TO_SCAN,
# do not forget about coma(,) 

LIST_OF_URLS_TO_SCAN =[
    'https://uae.dubizzle.com/motors/used-cars/audi/?sorting=date_desc&price__gte=790000&price__lte=200000000',
    'https://uae.dubizzle.com/motors/used-cars/bmw/?sorting=date_desc&price__gte=890000&price__lte=200000000',
]



# this is time interval (in minutes) to run the program
TIME_INTERVAL = 10             # 10 minutes          



#  chrome driver profile setting

# set up chrome profile path to run chrome driver with a specific existing profile
# this will set up the path for whatsapp data (for )

### for windows OS
# CHROME_PROFILE_PATH = 'user-data-dir=C:/Users/<PC_name>/AppData/Local/Google/Chrome/User Data/Default/'

### for mac OS  
CHROME_PROFILE_PATH = 'user-data-dir=Users/sajib/Library/Application Support/Google/Chrome/Default/'




# CSS SELECTORS (it changes over time)

# class = 'sc-cmkc2d-0 iLxLXX dbz-ads-listing' for car ads list 
# for list of car ads from current page
CAR_ADS_LIST_CSS_SELECTOR= 'div.sc-cmkc2d-0.iLxLXX.dbz-ads-listing'

# class = 'sc-cmkc2d-7 sc-11jo8dj-5 iZrQA-D hCGBVi for car price
PRICE_CSS_SELECTOR = 'div.sc-cmkc2d-7.sc-11jo8dj-5.iZrQA-D.hCGBVi'

# the above two class attributes change over time ******







