from bs4 import BeautifulSoup

class Injector:
	def __init__(self, input_path, output_path):
		self.input_path = input_path
		self.output_path = output_path
		# todo errorchecking
		f = open(input_path, "r")
		self.soup = BeautifulSoup(f.read(), "html.parser")
		f.close()

	def replace(self, kwargs, string):
		tags = self.soup.find_all(**kwargs)
		for tag in tags:
			tag.string = string

	def refresh_soup(self):
		f = open(input_path, "r")
		self.soup = BeautifulSoup(f.read(), "html.parser")
		f.close()

	def apply(self):
		f = open(self.output_path, "w")
		f.write(self.soup.prettify()) # not ideal, doesn't preserve original indentation
		f.close()






