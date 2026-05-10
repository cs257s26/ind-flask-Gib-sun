import psycopg2 as ps
import psqlConfig as config


def connect():
    try:
        connection = ps.connect(
            database=config.database,
            user=config.user,
            password=config.password,
            host="localhost"
        )

    except Exception as e:
        print("Connection error:", e)
        exit()

    return connection


def get_artworks_by_artist(connection, artist):

    try:
        cursor = connection.cursor()

        query = """
            SELECT artwork_name
            FROM artworks
            WHERE artist_name = %s;
        """

        cursor.execute(query, (artist,))

        return cursor.fetchall()

    except Exception as e:
        print("Query error:", e)
        return None


def count_artists_from_country(connection, country):

    try:
        cursor = connection.cursor()

        query = """
            SELECT COUNT(*)
            FROM artists
            WHERE origin_country = %s;
        """

        cursor.execute(query, (country,))

        return cursor.fetchone()

    except Exception as e:
        print("Query error:", e)
        return None


def main():

    connection = connect()

    results = get_artworks_by_artist(connection, "Pablo Picasso")

    print("Artworks by Pablo Picasso:")

    if results is not None:
        for item in results:
            print(item)

    print()

    country_count = count_artists_from_country(connection, "France")

    print("Artists from France:")

    if country_count is not None:
        print(country_count[0])

    # close connection
    connection.close()


main()