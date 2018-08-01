import csv
import io
import re

svg_filename = “your SVG map filename”
svg_map_data = open(svg_filename,'r',encoding="utf8").read()
# extract country code from data-iso
regexpHandler1 = re.compile('data-iso="(.*?)"/>')
country_code_matches = re.findall(regexpHandler1, svg_map_data)
# open and read your JS map file
js_map_data = open("your JS map filename", "r").read()
# check and get all the ‘”name”: “name”’ for replacement of country name later
regexpHandler2 = re.compile('\"name\": (\"name\d{0,3}\")')
js_map_matches = re.findall(regexpHandler2, js_map_data)
my_csv_filename = “your country information csv filename”
# Assign a variable with 0 for used
i = 0
# Match the country code from map file with the country information file and replace the country name according to order.
for country_code_match in country_code_matches:
	with open(my_csv_filename, 'r', encoding = 'utf-8') as f:
		mycsv = csv.reader(f)
		for row in mycsv:
			country_code = row[0]
			country_name = row[1]
			if country_code_match == country_code:
				country_name_string = 'name: \"'+ country_code + '\"'
				js_map_data = re.sub(regexpHandler2,country_name_string, js_map_data,1)
				print (js_map_matches[i] + ', ' + country_code_match + ', '+ country_name)
				i += 1

# Save the js map code to new JS file
with open('new_world_map.js', mode="w", encoding="utf8") as f:
	f.write(js_map_data)
