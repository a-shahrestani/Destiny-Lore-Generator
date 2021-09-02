# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import itertools

# Define Browser Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Hides the browser window
# Reference the local Chromedriver instance
chrome_path = 'H:\Chrome Driver\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)


def crawl_books():
    driver.get('https://www.ishtar-collective.net/books')
    books = [x.find_element_by_tag_name('h3').find_element_by_tag_name('a').get_attribute("href") for x in
             driver.find_elements_by_class_name("book-description")]
    entries = []
    for book in books:
        driver.get(book)
        entry = [x.find_element_by_tag_name('a').get_attribute("href") for x in
                 driver.find_elements_by_class_name('entry-thumbnail')]
        entries.append(entry)

    entries = list(itertools.chain(*entries))
    for idx, entry in enumerate(entries):
        driver.get(entry)
        description = driver.find_element_by_class_name('description').text
        file = open("Entries/Books/text{}.txt".format(idx), "a", encoding='utf-8')
        file.write(description)
        file.close()

    driver.quit()


def crawl_exotics():
    exotics = []
    for i in range(1, 7):
        driver.get('https://www.light.gg/db/category/-1?page=' + str(i) + '&f=2|3')
        exotics.append([x.get_attribute("href") for x in
                        driver.find_elements_by_class_name("text-exotic")])
    exotics = list(itertools.chain(*exotics))
    exotics = [x for x in exotics if x is not None]
    entries = []
    for exotic in exotics:
        driver.get(exotic)
        entries.append(driver.find_element_by_class_name('lore-desc').text)
    entries = list(set(entries))
    for idx, entry in enumerate(entries):
        file = open("Entries/Exotics/text{}.txt".format(idx), "a", encoding='utf-8')
        file.write(entry)
        file.close()
    # print(entries)
    driver.quit()


crawl_exotics()
