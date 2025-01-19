from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = 'chromedriver.exe'  # Update the path to ChromeDriver

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

# Wait for elements to load
wait = WebDriverWait(driver, 10)
containers = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="teaser__copy-container"]')))

titles = []
subtitles = []
links = []

for container in containers:
    try:
        title = container.find_element(By.XPATH, './a/h3').text
    except:
        title = "N/A"
    try:
        subtitle = container.find_element(By.XPATH, './a/p').text
    except:
        subtitle = "N/A"
    try:
        link = container.find_element(By.XPATH, './a').get_attribute('href')
    except:
        link = "N/A"

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv', index=False)

driver.quit()
