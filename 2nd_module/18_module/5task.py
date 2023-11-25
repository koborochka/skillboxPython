import requests
from bs4 import BeautifulSoup


def get_subheadings(url):
	response = requests.get(url)

	soup = BeautifulSoup(response.content, 'html.parser')

	subheadings = [heading.text.strip() for heading in soup.find_all('h3')]

	return subheadings


url = 'http://www.columbia.edu/~fdc/sample.html'

subheadings = get_subheadings(url)

print(subheadings)