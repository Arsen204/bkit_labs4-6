import psycopg2

db = psycopg2.connect(
    host="localhost",
    user="arsenvardumyan",
    dbname="lab5_db"
)

c = db.cursor()
c.execute('INSERT INTO "Lab4_person" (name, experience, technology_id) VALUES (%s, %s, %s);',
          ('Natali Harris', 4, 'py'))
db.commit()

c.execute('INSERT INTO "Lab4_technology" (id, name, description) VALUES (%s, %s, %s);',
          ('tg', 'Telegram', 'Best messenger'))
db.commit()
c.close()
db.close()
