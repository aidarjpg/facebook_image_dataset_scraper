#facebook scraper
from matplotlib.cbook import index_of
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget


"""
Downloading images

"""
def download(dish):
        
    print(dish + ": " + str(len(links[dish]) + '\n'))
    """
    !!!!!!!!!!!!!     Enter your values   !!!!!!!!!!!!!!

    """
    # Enter the absolute path to the folder where this file is located
    os.chdir(r'C:\Users\АЛСЕР\Desktop\ISSAI\fb_images')

    """
    !!!!!!!!!!!!!     Enter your values   !!!!!!!!!!!!!!

    """
    path = os.getcwd()
    path = os.path.join(path, dish)
    #create the directory
    os.mkdir(path)
    counter = 0
    for image in links[dish]:
        save_as = os.path.join(path, str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1

    """
    !!!!!!!!!!!!!     Enter your values   !!!!!!!!!!!!!!

    """
    # Enter the absolute path to the folder where this file is located
    os.chdir(r'C:\Users\АЛСЕР\Desktop\ISSAI\fb_images')

    """
    !!!!!!!!!!!!!     Enter your values   !!!!!!!!!!!!!!

    """

# the dictionary with variations a word can occur
# can further be extended with more request_word per your needs
request_words = {
    "house": ["house", "дом", "үй"]
    }


links = {
    "house": set()
}


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome(r'C:\Users\АЛСЕР\Desktop\ISSAI\chromedriver.exe', chrome_options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))


"""
!!!!!!!!!!!!!     Enter your values   !!!!!!!!!!!!!!

"""
#enter username and password
username.clear()
username.send_keys("")
password.clear()
password.send_keys("")

"""
!!!!!!!!!!!!!     Enter your values   !!!!!!!!!!!!!!

"""
#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5) 

if __name__ == "__main__":
    for subrequests in request_words:
        for el in request_words[subrequests]:  
            """
            Scratching Posts
            
            """
            driver.get("https://www.facebook.com/search/posts?q="+el)
            time.sleep(5)

            #scroll down
            #increase the range to sroll more
            #example: range(0,10) scrolls down more images
            for j in range(0,5):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
            # target all the link elements on the page
            img = driver.find_elements_by_tag_name("img")

            for h in img:
                try:
                    link = h.get_attribute("src")
                    if str(link).startswith("https://scontent") or str(link).startswith("https://external"):
                        links[subrequests].add(link)
                except:
                    pass
            
            """
            Scratching Photos
            
            """
            driver.get("https://www.facebook.com/search/photos?q="+el)
            time.sleep(5)
            driver.find_element_by_link_text("See all").click()
            
            for k in range(0,20):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
        
            img = driver.find_elements_by_tag_name("img")
            
            for g in img:
                try:
                    link = g.get_attribute("src")
                    if str(link).startswith("https://scontent") or str(link).startswith("https://external"):
                        links[subrequests].add(link)
                except:
                    pass
        
        download(subrequests) 
print("Done!")         
