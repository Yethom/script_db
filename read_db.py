import sqlite3

try:
    db = sqlite3.connect("music.db")
    cursor = db.cursor()

    get_artist = "SELECT * FROM artist"
    get_album = "SELECT * FROM album"
    get_album_artist = "SELECT a.name, ab.name, ab.release_year FROM album ab JOIN artist a ON ab.artist_id = a.id"

    cursor.execute(get_album_artist)
    for row in cursor.fetchall():
        print(row)
    db.close()
except sqlite3.Error as e:
    print("Error reading data from sqlite table", e)

