import sqlite3

try:
    table_artist = """
        CREATE TABLE IF NOT EXISTS artist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """

    table_album = """
        CREATE TABLE IF NOT EXISTS album (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER REFERENCES artist(id) ON DELETE CASCADE,
            name TEXT NOT NULL,
            release_year INTEGER NOT NULL
        )
        """

    table_insert_artist = "INSERT INTO artist (name) VALUES (?)"
    artists = [("Kanye West",), ("Paul McCartney",), ("Kid Cudi",), ("Michael Jackson",)]
    albums = [
        (1, "The College Dropout", 2007),
        (1, "Late Registration", 2012),
        (1, "Graduation", 2007),
        (2, "The Beatles", 1960),
        (3, "Man On the Moon", 2009),
        (4, "Thriller", 1982),
    ]

    table_insert_album = "INSERT INTO album (artist_id, name, release_year) VALUES (?, ?, ?)"

    with sqlite3.connect("music.db") as db:
        cursor = db.cursor()
        cursor.execute(table_artist)
        cursor.execute(table_album)
        cursor.executemany(table_insert_artist, artists)
        cursor.executemany(table_insert_album, albums)
        db.commit()
except sqlite3.Error as error:
    print("Error: ", error)
