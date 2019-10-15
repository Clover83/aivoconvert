from bs4 import BeautifulSoup

class Injector:
	def __init__(self, input_path, output_path):
		self.input_path = input_path
		self.output_path = output_path
		try:
			f = open(input_path, "r")
			self.soup = BeautifulSoup(f.read(), "html.parser")
			f.close()
		except:
			raise Exception("Could not open input file")

	# kwargs example: {{"attrs" : {attribute : True}}
	# string is what you want to replace the content of the tag with
	def replace(self, kwargs, string):
		tags = self.soup.find_all(**kwargs)
		for tag in tags:
			tag.string = string

	def refresh_soup(self):
		try:
			f = open(input_path, "r")
			self.soup = BeautifulSoup(f.read(), "html.parser")
			f.close()
		except:
			raise Exception("Could not open input file")

	# no file will be written to unless you call this function
	def apply(self):
		f = open(self.output_path, "w")
		f.write(self.soup.prettify()) # not ideal, doesn't preserve original indentation
		f.close()






