# Aivoconvert

Aivoconvert is a python script that looks through a html file for specific tags and generates a file which has replaced those tags with the days food, which is gotten from the site [Aivomenu](http://www.aivomenu.se).


## Installation
To install you need python3 installed and pip3, then you cd into the install directory and run:

`pip3 install -r requirements.txt`


## Basic usage
To use aivoconvert you need to give it an input:

`aivoconvert.py /path/to/the/input.html`

The input html file must contain the tags you want to change or else you will not see any significant changes,
by default these tags work fine:
```html
<p data-food="0">This will be replaced by the first food item</p>
<p data-food="1">This will be replaced by the second food item</p>
<p data-food="full">This will be replaced by both, separated by a joiner</p>
```

This will by default generate a file called "output.html" in the current working directory but this can be changed by simply adding the output path:

`aivoconvert.py /path/to/the/input.html /path/to/the/output_file.html`

## Example commands

`aivoconvert.py example.html ../modified.html -d tisdag`

This command specifies the day with `-d tisdag`, the same thing can be achieved with `--day tisdag`

`aivoconvert.py example.html ../modified.html --joiner " || "`

This command changes the joiner to be " || ", this means when using the full value in the attrubute the output will look like this:
> Thaigryta med röd curry, mango och ris/matvete || Karibisk biff med lime och mynta dressing

The joiner can be any string at all, but avoid using html and other special character as they will be escaped throught the html.escape() function.

`aivoconvert.py example.html ../modified.html --attribute data-mat`

This command will only look for attributes that are named "data-mat" instead of the default "data-food". It is worth noting that even though this could be any string without a space, it sould be a string and follow the html data attribute syntax. Which for the lazy basically means:

> the name of a valid custom data attribute must contain only letters, numbers, hyphen (-), dot (.), colon (:) or underscore (_). It cannot contain capital letters.
> Data stored in these attributes should be of type string

[Learn more.](https://www.sitepoint.com/how-why-use-html5-custom-data-attributes/)

`aivoconvert.py example.html ../modified.html --full_val allthefood`

If you for some reason need to change the value the attribute needs to be in order to use the joined output this would be it. This command would only use the joined output on tags with the attribute set to "allthefood" instead of the default "full". 
