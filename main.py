import sys
from util import union
from util import intersection
from util import get_all_urls
from util import get_all_films

def main():

	functions = {"u":union, "i":intersection}

	# get all the urls
	filename = "url.txt"
	all_urls = get_all_urls(filename)

	# get all the lists
	all_lists = [get_all_films(url) for url in all_urls]

	# get the final list of films
	final_films = functions[sys.argv[1]](all_lists)

	# print all the films
	for film in final_films:
		print(film)

main()