#!/usr/bin/python3
import inject
import foody
import html
from pathlib import Path

# Default optional argument variables
_joiner = " | "
_attribute = "data-food"
_full_val = "full"

def refresh(input_file_path, output_file_path, day, joiner, attribute, full_val):
	food = foody.get_food(day)
	inj = inject.Injector(input_file_path, output_file_path)
	for i in range(len(food)):
		inj.replace({"attrs" : {attribute : str(i)}}, html.escape(food[i]))
	food = joiner.join(food)
	inj.replace({"attrs" : {attribute : full_val}}, html.escape(food))
	inj.apply()

_DESCRIPTION = """
Parses a html file for tags with a specific attribute
and replaces the content of that tag with the days food.
"""
# aivoconvert input output --joiner " | " --attribute "foody" --full_val "full"
if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(description=_DESCRIPTION)
	
	parser.add_argument("input", 
		type=lambda p: Path(p).absolute(),
		help="The input file")

	parser.add_argument("output", 
		type=lambda p: Path(p).absolute(),
		help="The output file, cwd by default.",
		nargs="?",
		default=Path.cwd() / "output.html")

	parser.add_argument("-d", "--day",
		type=str,
		help="The day in Swedish, i.e \"måndag\" for monday, if not specified todays day will be used.")

	parser.add_argument("--joiner",
		type=str,
		help="The string that will separate each food item when injecting the full food list.",
		default=_joiner)

	parser.add_argument("--attribute",
		type=str,
		help="The attribute it will look for when parsing tags, by default \"" + str(_attribute) + "\".",
		default=_attribute)

	parser.add_argument("--full_val",
		type=str,
		help="If the attribute is equal to this it will use the full food list, by default \"" + str(_full_val) + "\".",
		default=_full_val)

	args = parser.parse_args()
	
	refresh(args.input, args.output, args.day, args.joiner, args.attribute, args.full_val)


