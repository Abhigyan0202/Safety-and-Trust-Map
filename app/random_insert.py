import sqlite3
import random
import string
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()


for _ in range(200):
    random_station = random.randint(1,98)
    random_rating = random.randint(1,5)
    random_letters = ''.join(random.choices(string.ascii_letters, k=20))
    cursor.execute("""
        INSERT INTO crime_data_region_reviews
        (user_id, police_station_id, review, rating, created_at)
        VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, (1, random_station, random_letters, random_rating))

conn.commit()
conn.close()