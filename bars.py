import json
import math

def load_data(filepath):
    myfile = open(filepath, mode = 'r', encoding = 'cp1251')
    return json.load(myfile)


def get_biggest_bar(data):
    return max(data, key=lambda x: x['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda x: x['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    dist = lambda x: math.sqrt((float(x['Longitude_WGS84'])-longitude)**2 + (float(x['Latitude_WGS84'])-latitude)**2)
    return min(data, key = dist)

def get_info_bars(data):
    print("Name: ", data['Name'])
    print("Seats Count: ", data['SeatsCount'])
    print("Coordinates", data['Latitude_WGS84'], data['Longitude_WGS84'])

if __name__ == '__main__':
    bars_data = load_data(input("Input path please: "))
    lati = float(input("Input latitude, please: "))
    #lati = 55.773039
    longi = float(input("Input longitude, please: "))
    #longi = 37.675786
    print("The biggest bar -> ") 
    get_info_bars(get_biggest_bar(bars_data))
    print("The smallest bar - > ")
    get_info_bars(get_smallest_bar(bars_data))
    print("The closest bar - > ")
    get_info_bars(get_closest_bar(bars_data, longi, lati))
