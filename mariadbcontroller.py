import mariadb

import mariadbcredentials


# connectingdo database
def connectToDatabase():
    # loggin in
    try:
        conn = mariadb.connect(
            user=mariadbcredentials.user,
            password=mariadbcredentials.password,
            host=mariadbcredentials.host,
            port=mariadbcredentials.port,
            database=mariadbcredentials.database
        )
    except mariadb.Error:
        print("Error")

    cur = conn.cursor()

    return conn, cur


# adding class object to database
def addToDatabase(object, cur, conn):
    try:
        cur.execute("INSERT INTO newsAggregator.news (title, description, link, pubDate, image, category, guid) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)", (object.title, object.description, object.link, object.pubDate,
                                                     object.image, object.category, object.guid))
    except mariadb.Error as e:
        print("Error")

    conn.commit()
