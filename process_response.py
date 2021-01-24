import config
import mysql.connector


from google_request import google_request


def process_response(response):
    db = mysql.connector.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        database=config.DATABASE
    )

    cursor = db.cursor()
    tags = []

    for business in response['businesses']:
        name = business['name']
        yepl_rating = business['rating']
        phone = business['phone']
        website = business['url']
        address = business['location']['address1']
        city = business['location']['city']
        zip_code = business['location']['zip_code']
        longitude = business['coordinates']['longitude']
        latitude = business['coordinates']['latitude']
        google_rating = google_request(name, latitude, longitude)
        for tag in business['categories']:
            tags.append(tag['alias'])
        str_tags = ",".join(tags)


        sql = '''insert into cafes 
            (name, phone, website, tags, address, city, zip_code, 
            longitude, latitude, yelp_rating, google_rating) 
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        val = [(
            name, phone, website, str_tags, address, city, zip_code,
            longitude, latitude, yepl_rating, google_rating
        )]

        cursor.executemany(sql, val)

    db.commit()
