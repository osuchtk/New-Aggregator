from datetime import datetime

import pandas as pd
from pyowm import OWM

from credentials import weatherAPI


# classes for actual and future weather object
class Weather:
    def __init__(self, city, time, temp, hum, press, status, windSpeed, windDir, snow, precProb, icon):
        self.city = city
        self.actualTime = time
        self.actualTemp = temp
        self.actualHum = hum
        self.actualPress = press
        self.actualStatus = status
        self.actualWindSpeed = windSpeed
        self.actualWindDir = windDir
        self.actualSnow = snow
        self.actualPrecProb = precProb
        self.icon = "https://openweathermap.org/img/wn/{}@2x.png".format(icon)


class ForecastWeather(Weather):
    def __init__(self, city, time, temp, hum, press, status, windSpeed, windDir, snow, precProb, measureId, icon):
        super().__init__(city, time, temp, hum, press, status, windSpeed, windDir, snow, precProb, icon)
        self.measureID = measureId


def getWeather():
    # read file with polish cities
    citiesFile = pd.read_excel("./worldcities.xlsx")
    citiesFile = citiesFile.query("country == 'Poland'")
    polishCities = citiesFile['city']

    cities = []
    for city in polishCities:
        cities.append(city)

    # conect to Open Weather Map
    owm = OWM(weatherAPI)
    mgr = owm.weather_manager()

    # getting actual weather
    err = []
    actualWeatherList = []

    for city in cities:
        try:
            observation = mgr.weather_at_place('{},PL'.format(city))

            actualTime = datetime.fromtimestamp(observation.weather.ref_time)
            actualTemp = observation.weather.temp['temp']
            actualHum = observation.weather.humidity
            actualPress = observation.weather.pressure['press']
            actualStatus = observation.weather.status
            actualWindSpeed = observation.weather.wnd['speed']
            actualWindDir = observation.weather.wnd['deg']

            try:
                actualSnow = observation.weather.snow['1h']
            except KeyError:
                actualSnow = 0

            actualPrecProb = observation.weather.precipitation_probability
            if actualPrecProb is None:
                actualPrecProb = 0

            icon = observation.weather.weather_icon_name

            actualWeatherList.append(Weather(city, actualTime, actualTemp, actualHum, actualPress, actualStatus,
                                             actualWindSpeed, actualWindDir, actualSnow, actualPrecProb, icon))

        # test without try...except to refine except clause
        except:
            err.append(city)

    # getting forecast
    err = []
    forecastWeatherList = []

    for city in cities:
        try:
            observation = mgr.forecast_at_place('{},PL'.format(city), '3h').forecast

            for ind in range(len(observation.weathers)):
                forecastTime = datetime.fromtimestamp(observation.weathers[ind].ref_time)
                forecastTemp = observation.weathers[ind].temp['temp']
                forecastHum = observation.weathers[ind].humidity
                forecastPress = observation.weathers[ind].pressure['press']
                forecastStatus = observation.weathers[ind].status
                forecastWindSpeed = observation.weathers[ind].wnd['speed']
                forecastWindDir = observation.weathers[ind].wnd['deg']

                try:
                    forecastSnow = observation.weathers[ind].snow['1h']
                except KeyError:
                    forecastSnow = 0

                forecastPrecProb = observation.weathers[ind].precipitation_probability
                if forecastPrecProb is None:
                    forecastPrecProb = 0

                measureid = city + " " + str(forecastTime)
                icon = observation.weathers[ind].weather_icon_name

                forecastWeatherList.append(ForecastWeather(city, forecastTime, forecastTemp, forecastHum, forecastPress,
                                                           forecastStatus, forecastWindSpeed, forecastWindDir,
                                                           forecastSnow, forecastPrecProb, measureid, icon))

        except:
            err.append(city)

    print("Weather - SUCCESS")
    return actualWeatherList, forecastWeatherList
