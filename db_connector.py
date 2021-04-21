import psycopg2
import configparser
import datetime

config = configparser.ConfigParser()
config.read('config.ini')

sample_query = \
"""
insert into "rsvp"."guests" (name, attendance)
values ('Bry', 'yes')
"""

def get_cnxn():
    connection = psycopg2.connect(user = "postgres",
                            password = config['credentials']['password'],
                            host = config['credentials']['host'],
                            port = "5432",
                            database = "postgres")
    return connection

def write_to_db(name, attendance, email, affiliation ,anythingelse):
    today = datetime.datetime.now()
    connection = get_cnxn()
    cursor = connection.cursor()
    query = \
    """
    INSERT INTO "rsvp"."guests" (name, attendance, email, affiliation, anythingelse, time)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    cursor.execute(query, (name, attendance, email, affiliation, anythingelse, today))
    connection.commit()

# for pymysql
import pymysql

def open_connection():
    unix_socket = '/cloudsql/{}'.format(config['credentials']['unix_socket'])
    try:
        conn = pymysql.connect(user='root', password=config['credentials']['password'],
                            # unix_socket=unix_socket, 
                            db='mysql',
                            host=config['credentials']['host'], 
                            # host='localhost', 
                            port=3306,
                            cursorclass=pymysql.cursors.DictCursor
                            )
    except pymysql.MySQLError as e:
        print(e)

    return conn

def write_to_mysql(name, attendance, email, affiliation ,anythingelse):
    today = datetime.datetime.now()
    connection = open_connection()
    cursor = connection.cursor()
    query = \
    """
    INSERT INTO rsvp.guests (name, attendance, email, affiliation, anythingelse, time)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    cursor.execute(query, (name, attendance, email, affiliation, anythingelse, today))
    connection.commit()
    connection.close()