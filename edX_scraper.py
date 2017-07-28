#edX scraper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

driver = webdriver.Chrome('/Users/Patrick/Downloads/chromedriver')

driver.get('https://www.edx.org/course?language=English')

csv_file = open('courses.csv', 'w')

writer = csv.writer(csv_file)

writer.writerow(['title', 'content', 'username', 'date'])

index = 1
total_courses = 0
wait = WebDriverWait(driver, 2)

num_classes_str = driver.find_element_by_xpath('//span[@class="js-count result-count"]').text		#get the total number of courses
num_classes = int((re.findall(r'\d+', num_classes_str))[0])											#convert course number to int

page = 0

while page < num_classes:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	try:
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="loading"]')))
		page += 1
	except Exception as e:
		print(e)
		print(page)
		break


courses = driver.find_elements_by_xpath('//div[@class="discovery-card-inner-wrapper"]/a[@class="course-link"]')
print('='*50)
print(len(courses))
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])
print('='*50)
course_links = []
for course in courses:
	course_links.append(course.get_attribute('href'))

print('='*50)
print(len(course_links))
print(course_links[0])

course_links = ['https://www.edx.org/course/islamic-finance-banking-modes-finance-irtix-ifb102x-0#!']

for course_link in course_links:
	course_dict = {}
	driver = webdriver.Chrome('/Users/Patrick/Downloads/chromedriver')
	driver.get(course_link)


	try:
		title = driver.find_element_by_xpath('.//*[@id="course-info-page"]/header/div/div/div[2]/h1[@id="course-intro-heading"]').text
		print(title)
		short_description = driver.find_element_by_xpath('.//*[@id="course-info-page"]/header/div/div/div[2]/p[@class="course-intro-lead-in"]').text
		print(short_description)
		length = driver.find_element_by_xpath('.//*[@id="course-summary-area"]/ul/li[1]/span[2][@class="block-list__desc"]').text
		print(length)
		effort = course_link.find_element_by_xpath('.//*[@id="course-summary-area"]/ul/li[2]/span[2][@class="block-list__desc"]').text
		print(effort)
		price = course_link.find_element_by_xpath('.//*[@id="course-summary-area"]/ul/li[3]/span[2]/span[@class="uppercase"]').text
		print(price)
		institution = course_link.find_element_by_xpath('.//*[@id="course-summary-area"]/ul/li[4]/span[2]/a').text
		print(institution)
		subject = course_link.find_element_by_xpath('.//*[@id="course-summary-area"]/ul/li[5]/span[2]/a').text
		print(subject)
		level = course_link.find_element_by_xpath('.//*[@id="course-summary-area"]/ul/li[6]/span[2][@class="block-list__desc"]').text
		print(level)
		languages = course_link.find_element_by_xpath('.//*[@id="course-summary-area"]/ul/li[7]/span[2]/span').text
		print(languages)
		video_transcripts = course_link.find_element_by_xpath('.//*[@id="course-summary-area"]/ul/li[8]/span[2]/span').text
		print(video_transcripts)
		prerequisites = course_link.find_element_by_xpath('.//*[@id="course-summary-area"]/div[2]/p').text
		print(prerequisites)

		course_dict['title'] = title
		course_dict['short_description'] = short_description
		course_dict['length'] = length
		course_dict['effort'] = effort
		course_dict['price'] = price
		course_dict['institution'] = institution
		course_dict['subject'] = subject
		course_dict['level'] = level
		course_dict['languages'] = languages
		course_dict['video_transcripts'] = video_transcripts
		course_dict['prerequisites'] = prerequisites
		writer.writerow(course_dict.values())


	except Exception as e:
		print(e)
		pass















#---------------------------------------------------------------------------------------------------------
# while True:
# 	try:
# 		courses = driver.find_elements_by_xpath('//div[@class="js-card-list filtered"]/div[@class="discovery-card course-card shadow verified"]')
# 		print('='*50)
# 		print(len(courses))
# 		print(courses[0])
# 		print('='*50)

# 	except Exception as e:
# 		print(e)
# 		csv_file.close()
# 		driver.close()
# 		break


# while index < :
# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	
# 	if EC.invisibility_of_element_located((By.XPATH, '//div[@class="loading"]')):
# 		print("breaking")
# 		# break
		# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	


# while True:
# 	try:
# 		courses = driver.find_elements_by_xpath('//div[@class="js-card-list filtered"]/div[@class="discovery-card course-card shadow verified"]')
# 		print('='*50)
# 		print(len(courses))
# 		print(courses[0])
# 		print('='*50)

# 	except Exception as e:
# 		print(e)
# 		csv_file.close()
# 		driver.close()
# 		break

# path_to_chromedriver = '/Users/Patrick/Downloads/chromedriver'
# response = webdriver.Chrome(executable_path = path_to_chromedriver)

# url = 'https://www.edx.org/course?language=English'
# response.get(url)

# #def parse(url):

# parser = html.fromstring(response.page_source, response.current_url)
# courses = parser.xpath('//a[@class="course-link"]/text()').extract()
# print(courses)
#href="https://www.edx.org/course/knowledge-management-big-data-business-hkpolyux-ise101x-3"