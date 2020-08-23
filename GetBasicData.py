from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=University+of+North+Texas&schoolID=1252&queryoption=TEACHER")

#Get pop-ups out of the way
cookie_notice = driver.find_element_by_id('cookie_notice')
cookie_buttons = cookie_notice.find_elements_by_tag_name('a')
cookie_buttons[0].click()

ccpa_notice = driver.find_element_by_id('ccpa-footer')
ccpa_buttons = ccpa_notice.find_elements_by_class_name("close-this")
ccpa_buttons[0].send_keys(Keys.RETURN)

#Calculate how many times I need to load in more professors
#Loads in 20 to start and 20 more each time
count = driver.find_element_by_class_name("professor-count").text
print(str(count) + " professors found")

num = int(int(count) / 2) + 5
print(str(num) + " clicks")

#Load all professors
load_more = driver.find_element_by_class_name("progressbtnwrap")
load_more_button = load_more.find_element_by_class_name("content")

for i in range(0, 3000):
    driver.execute_script("arguments[0].click();", load_more_button)  # It works!

print("Finished...")

#Get list of professors
results = driver.find_elements_by_class_name("result-list")

#Want second element of results
rawProfessors = results[1]
rawProfessors = str(rawProfessors.text).replace('\t', '').replace('\r', '').strip()
rawProfessors = rawProfessors.replace("  \n", "\n")

for i in range(2, 20):
    temp = ""
    for x in range(1, i):
        temp += "\n"
    rawProfessors = rawProfessors.replace(temp, "\n")

for i in range(2, 20):
    temp = ""
    for x in range(1, i):
        temp += "\r"
    rawProfessors = rawProfessors.replace(temp, "\n")

rawProfessors = rawProfessors.replace("\n\n", "")

splitProfessors = rawProfessors.split('×')
splitProfessors.remove(splitProfessors[0])
newProfs = []
for sp in splitProfessors:
    newProfs.append(sp.strip('\n'))

splitProfessors = newProfs


class Professor:
    def __init__(self, name, rating, numRatings):
        self.rating = rating
        self.name = name
        self.numRatings = numRatings


professors = []
for sp in splitProfessors:
    s = sp.split('\n')
    professors.append(Professor(s[1], s[0], s[2]))

output = ""

for p in professors:
    output += p.name + "/" + p.rating + "/" + p.numRatings + "\n"

file_out = open("professors.txt", "w")
file_out.write(output)
file_out.close()

print("File ready...")

driver.close()
