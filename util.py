import requests
from bs4 import BeautifulSoup

def get_soup(link):
	"""
	Get the soup for the HTML from link using requests.
	"""

	page = requests.get(link)
	return BeautifulSoup(page.content, 'html.parser')


def get_films_on_page(link, page_no):
	"""
	return the list of films on current page
	"""

	all_films = []

	# get the elements containing films
	soup = get_soup(link+"page/%d"%(page_no))
	list_elements = soup.find_all(class_="film-poster")

	# iterate over all the elements
	for film in list_elements:
		all_films.append(film.img.get('alt'))

	return all_films

def get_all_films(link):
	"""
	return a list of all the films in a list
	"""

	all_films = []

	# start from the first page
	page_no = 1

	while True:

		# get films on the current page
		films_on_page = get_films_on_page(link, page_no)

		# if the page doesn't have any films
		if len(films_on_page) == 0:
			break

		all_films += films_on_page
		page_no += 1

	return set(all_films)


def get_all_urls(filename):
	"""
	return all the URLs from filename
	"""

	# get all the lines from filename
	file = open(filename)
	all_lines = file.readlines()
	file.close()

	# init empty list
	urls = []

	# iterate over all lines
	for line in all_lines:

		# skip an empty line
		if len(line.strip()) == 0:
			continue

		# skip commented out line
		if line[0] == '#':
			continue

		urls.append(line.strip())

	return urls

def union(lists):
	"""
	return the union of all the lists in 'lists'
	"""

	return set([]).union(*lists)

def intersection(lists):
	"""
	return the intersection of the lists in 'lists'
	"""

	return lists[0].intersection(*lists)


