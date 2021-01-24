import config
import mysql.connector


db = mysql.connector.connect(
  host=config.HOST,
  user=config.USER,
  password=config.PASSWORD,
)

cursor = db.cursor()

cursor.execute(f"create database if not exists {config.DATABASE}")

cursor.execute(f"""
    create table if not exists {config.DATABASE}.cafes
    (
        name varchar(255) null,
        phone varchar(255) null,
        website text null,
        tags text null,
        address varchar(255) null,
        city varchar(255) null,
        zip_code int null,
        latitude double null,
        longitude double null,
        yelp_rating float null,
        google_rating float null
    );
 """)

