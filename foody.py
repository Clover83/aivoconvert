# meant to be an importable module

from bs4 import BeautifulSoup
import requests

URL = "http://www.aivomenu.se/ShowMenu.aspx?MenuId=362&lang=sv-SE"
# anything containing something in this list will be removed from the output, capitalization independent
FILTERED_WORDS = ["måndag", "tisdag", "torsdag", "fredag", "onsdag", "skollunch", "idag", "startsida", "skriv ut"]
TODAY = "idag"
DAYS = ["måndag", "tisdag", "onsdag", "torsdag", "fredag"]
# returns the soup of the URL constant
def _get_soup():
	page = requests.get(URL)
	soup = None
	if page.status_code == 200:
		soup = BeautifulSoup(page.text, "html.parser")
	return soup

def _get_search_area(soup):
	search_area = soup.find(id="contentDiv")
	search_area = search_area.find_all("td")
	return search_area

def _strip_duplicates(a_list):
	x = list(dict.fromkeys(a_list))
	return x


def _get_today_divs(divs, search_day=TODAY):
	x = []
	passed_today = False
	for div in divs:
		if passed_today:
			for day in DAYS:
				if day in div.text.lower():
					return x
			x += [div]
		elif search_day.lower() in div.text.lower():
			passed_today = True
			x += [div]
	return x

def _divs_to_text(divs):
	x = []
	for div in divs:
		# remove the leading and trailing whitespace
		x += [div.text.lstrip().rstrip()]

	x = _strip_duplicates(x)
	return x

def _get_filtered_list(a_list):
	for word in FILTERED_WORDS:
		for item in a_list:
			if word.lower() in item.lower():
				a_list.remove(item)
			# remove if empty string
			elif not item:
				a_list.remove(item)
	return a_list

def get_food(day=TODAY):
	# this could all be written as one line, but this is better for readability
	soup = _get_soup()
	if soup != None:
		search_area = _get_search_area(soup)
		today_divs = _get_today_divs(search_area, day)
		food = _divs_to_text(today_divs)
		food = _get_filtered_list(food)
		return food;
	else:
		print("soup not found")

def _get_invalid_arg_blurb():
	x = "Invalid argument, please use the days in Swedish, i.e: \"måndag torsdag\""
	return x

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		for item in sys.argv[1:]:
			if item.lower() in DAYS:
				food = get_food(item)
				print(food)
			else:
				print(_get_invalid_arg_blurb())
				break
	else:
		food = get_food()
		print(food)

