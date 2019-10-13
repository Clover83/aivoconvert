from bs4 import BeautifulSoup

def _get_soup(html_path):
	f = open(html_path, "r")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()
	return soup

def _get_replaced_soup(html_path, html_class, string):
	soup = _get_soup(html_path)
	tags = soup.find_all(class_ = html_class)
	for tag in tags:
		tag.string = string
	return soup

# if output_path is None then it overwrites the original file
def inject(input_path, html_class, string, output_path = None):
	soup = _get_replaced_soup(input_path, html_class, string)
	if output_path == None:
		output_path = input_path
	f = open(output_path, "w")
	f.write(soup.prettify()) # not ideal, doesn't preserve original indentation
	f.close()

