# Import
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import itertools

# Define Browser Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Hides the browser window
# Reference the local Chromedriver instance
chrome_path = 'H:\Chrome Driver\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get('https://www.ishtar-collective.net/books')
time.sleep(5) # Let the user actually see something!
books = [x.find_element_by_tag_name('h3').find_element_by_tag_name('a').get_attribute("href") for x in driver.find_elements_by_class_name("book-description")]
entries = []
for book in books:
    driver.get(book)
    entry = [x.find_element_by_tag_name('a').get_attribute("href") for x in driver.find_elements_by_class_name('entry-thumbnail')]
    entries.append(entry)
# htmltext = driver.page_source
entries = list(itertools.chain(*entries))
for idx, entry in enumerate(entries):
    driver.get(entry)
    description = driver.find_element_by_class_name('description').text
    file = open("Entries/text{}.txt".format(idx), "a",encoding='utf-8')
    file.write(description)
    file.close()
# print(entries)
# driver.get('https://www.ishtar-collective.net/entries/i-ambush#book-ripples')
# t = driver.find_element_by_class_name('description')
# print(t.text)
driver.quit()

