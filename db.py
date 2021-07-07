import sqlite3
from sqlite3 import Error
import json
import pandas as pd
import sys

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("select events.data from events where events.action_name = 'phno' or events.action_name = 'objet' or events.action_name = 'Nom_Prenom' ;")

    rows = cur.fetchall()
    i = 0
    sys.stdout = open('log.ods', 'w')
    for row in rows:
        
        
        if str(json.loads(row[0]).get('value'))!='None':
            print(json.loads(row[0]).get('name') + ' :' + str(json.loads(row[0]).get('value')))
            i=i+1 
            if (i%3==0):
                print('**********************************************************************')
        
       
               
def main():
    database = r"rasa"

    # create a database connection
    conn = create_connection(database)
    with conn:
        
        select_all_tasks(conn)


if __name__ == '__main__':
    main()


def create_connection2(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks2(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("select events.data from events where events.action_name = 'utter_Parfait' or events.action_name = 'utter_Moyen' or events.action_name = 'utter_Bien' or events.action_name = 'utter_Mediocre' or events.action_name = 'utter_Horrible'")

    rows = cur.fetchall()
    
    sys.stdout = open('log2.ods', 'w')
    for row in rows:
        
        
        print(json.loads(row[0]).get('name'))
        
       
               
def main2():
    database = r"rasa"

    # create a database connection
    conn = create_connection2(database)
    with conn:
        
        select_all_tasks2(conn)


if __name__ == '__main__':
    main2()



