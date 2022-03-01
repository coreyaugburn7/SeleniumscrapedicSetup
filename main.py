from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/coreyaugburn/Desktop/CodeProjectspy/chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

event_date = driver.find_elements(By.CLASS_NAME, 'event-widget time')
# print(event_date)
# date = event_date.text



event_name = driver.find_elements(By.CLASS_NAME, 'event-widget li a')
# print(event_name)
# Doesnt work with the .text notation
# print(event_name.text)

event_num = 0


event_dict = {}

# for n in event_date:
#     print(n.text)
#     event_dict['date'] = n.text
#
# for n in event_name:
#     print(n.text)
#     event_dict['name'] = n.text
#
# print(event_dict['date'], event_dict['name'])


for n in range(len(event_date)):
    event_dict[n] = {
        "time": event_date[n].text,
        "name": event_name[n].text,
    }

print(event_dict)


driver.quit()


































