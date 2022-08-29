#! /bin/python3

import csv


# Reading the template files from the disk
htmlTemplateFile	= open('templates/template.html', 'r')
cssTemplateFile		= open('templates/template.css', 'r')
entryTemplateFile	= open('templates/entryTemplate.html', 'r')

htmlTemplate 	= htmlTemplateFile.read()
cssTemplate 	= cssTemplateFile.read()
entryTemplate 	= entryTemplateFile.read()

htmlTemplateFile.close()
cssTemplateFile.close()
entryTemplateFile.close()

index = 1


# Reading the content from the file on disk & inserting it into the template
with open('content.csv', 'r') as file:
	content = csv.reader(file)
	for entry in content:
		htmlTemplate = htmlTemplate.format(entry=entryTemplate.format(
			url		= 'https://' + entry[1].lstrip(),
			index	= index,
			short	= entry[0][0:2].title(),
			name	= entry[0],
			entry 	= '{entry}'
		)[:-1], styles = '{styles}')
		
		index += 1


# Inserting the corrent column count into the css template
cssTemplate = cssTemplate.replace('$width$', ('auto ' * round(index / 4))[:-1])

# Cleaning the html template
htmlTemplate = htmlTemplate.format(entry='', styles=cssTemplate)

htmlFile	= open('home.html', 'w')
htmlFile.write(htmlTemplate)
htmlFile.close()
