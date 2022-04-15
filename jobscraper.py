from bs4 import BeautifulSoup
import pandas as pd
import requests

def scrapedata(page):
	url = f"https://www.indeed.com/jobs?q=Quantitative%20developer&l&vjk=1ee02b93f3eeda74{page}"
	headers = {"User Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
	r = requests.get(url, headers)
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup
 
def alterdata(soup):
	divs = soup.find_all('div', class_ = 'slider_container css-11g4k3a eu4oa1w0')
	for i in divs:
		title = i.find('h2').text
		if "new" in title:
			title = title.replace("new", "")
		company = i.find('span', class_ = "companyName").text
		location = i.find('div', class_ = "companyLocation").text
		try:
			salary = i.find('div', class_ = "metadata salary-snippet-container").text
		except:
			salary = ''
		desc = i.find('li').text

		job = {
			"Title" : title,
			"Company" : company,
			"Salary" : salary,
			"Location" : location,
			"Description" : desc
		}
		JL.append(job)



	return

JL = []

#First four pages of URL
i = 1;
for x in range(0, 40, 10):
	print(f"Scraping page {i}")
	new = scrapedata(x)
	alterdata(new)
	i += 1


dataframe = pd.DataFrame(JL)
print(dataframe.head())
dataframe.to_csv("internships.csv")