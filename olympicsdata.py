import urllib, json

def updateData():
	url = "http://wowappprd.rio2016.com/json/medals/OG2016_medalsList.json"
	response = urllib.urlopen(url)
	data = json.loads(response.read())

	text = open("olympics.txt", "w")

	for country in data["body"]["medalRank"]["medalsList"]:
		string = country['noc_code'] + "- G:" + country['me_gold'] + " S:" + country['me_silver'] + " B:" + country['me_bronze'] + " T:" + country['me_tot'] + "\n" 
		text.write(string)

	text.close()
