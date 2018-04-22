import urllib2
import json


# Global Variable Declaration
key = 'https://api.darksky.net/forecast/YOUR_KEY_HERE/'   # key from darksky
latitude = 45.6523                                                           # latitude of desired location
longitude = 25.6103                                                          # longitude of desired location
url = key + str(latitude) + ',' + str(longitude)


class CurrentWeather:
    def __init__(self, time, summary, icon, temperature, precipProbability, humidity):
        self.time = time
        self.summary = summary
        self.icon = icon
        self.temperature = temperature
        self.precipProbability = precipProbability
        self.humidity = humidity



# Get data from darksky in JSON format
def get_current_weather():
    print('get_current_weather called')

    # get request to darksky api
    data = urllib2.urlopen(url).read()
    dataJSON = json.loads(data)

    # return an object with currently weather info
    currData = dataJSON['currently']
    obj = CurrentWeather(
                         currData['time'],
                         currData['summary'],
                         currData['icon'],
                         currData['temperature'],
                         currData['precipProbability'],
                         currData['humidity']
                         )
    return obj


# dataObj = get_current_weather()
# w = CurrentWeather(data['time'], data['summary'], data['icon'], data['temperature'])
# print(dataObj.summary)
