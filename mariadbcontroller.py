import mariadb

import credentials


# connectingdo database
def connectToDatabase():
    # loggin in
    try:
        conn = mariadb.connect(
            user=credentials.user,
            password=credentials.password,
            host=credentials.host,
            port=credentials.port,
            database=credentials.database
        )
    except mariadb.Error:
        print("Error")

    cur = conn.cursor()

    return conn, cur


# adding class object to database
def addNews(object, cur, conn):
    try:
        cur.execute("INSERT INTO newsAggregator.news (title, description, link, pubDate, image, category, guid) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)", (object.title, object.description, object.link, object.pubDate,
                                                     object.image, object.category, object.guid))
    except mariadb.Error as e:
        print(e)

    conn.commit()


def addActualWeather(object, cur, conn):
    try:
        cur.execute("INSERT INTO newsAggregator.actualweather (city, time, temperature, humidity, pressure, status, "
                    "windSpeed, windDirection, snow, precitipationProbability) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (object.city, object.actualTime, object.actualTemp,
                                                              object.actualHum, object.actualPress, object.actualStatus,
                                                              object.actualWindSpeed, object.actualWindDir,
                                                              object.actualSnow, object.actualPrecProb))
    except mariadb.Error as e:
        print(e)

    conn.commit()


def addForecastWeather(object, cur, conn):
    try:
        cur.execute(
            "INSERT INTO newsAggregator.forecastweather (measureid, city, time, temperature, humidity, pressure, status, "
            "windSpeed, windDirection, snow, precitipationProbability) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (object.measureID, object.city, object.actualTime,
                                                         object.actualTemp, object.actualHum,
                                                         object.actualPress, object.actualStatus,
                                                         object.actualWindSpeed, object.actualWindDir,
                                                         object.actualSnow, object.actualPrecProb))
    except mariadb.Error as e:
        print(e)

    conn.commit()
