import json
import math
import urllib.request
import os, zipfile

url = 'http://op.mos.ru/EHDWSREST/catalog/export/get?id=84505'
response = urllib.request.urlopen(url)
#json_data = response.read()
zipArchive = zipfile.ZipFile(response, 'r')
unzippedFile = zipArchive.open(response, 'r')
json_data = unzippedFile.read()
#filenames = filename.json()
#filename = "data.json"
#myfile = open(filename, mode = 'r', encoding = 'cp1251')
#json_data = json.load(myfile)

dist = []
#coord_x = float(input('coordinate X = '))
#coord_y = float(input('coordinate Y = '))
coord_x = 55.773065
coord_y = 37.675870

for bar in json_data:
   x = float(bar['geoData']['coordinates'][1])
   y = float(bar['geoData']['coordinates'][0])
   #print("Coordinate Y " + str(x))
   #print("Coordinate X " + str(y))
   dist.append(math.sqrt((coord_x - x)**2 + (coord_y-y)**2))
min_dist = min(dist)
nomber = dist.index(min_dist)
print(" Min dist = " + str(min_dist) + ", Nomer = " + str(nomber))   
    
def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['SeatsCount'])
    return biggest_bar
print("Biggest bar : " + str(get_biggest_bar(json_data)['Name']) + " SeatsCount = " + str(get_biggest_bar(json_data)['SeatsCount']))

def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['SeatsCount'])
    return smallest_bar
print("Smallest bar : " + str(get_smallest_bar(json_data)['Name']) + " SeatsCount = " + str(get_smallest_bar(json_data)['SeatsCount']))

print("ryadom  = " + str(json_data[nomber]['Name']))

myfile.close()