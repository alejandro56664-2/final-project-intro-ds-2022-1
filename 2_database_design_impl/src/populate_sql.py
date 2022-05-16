# This script Transform & Load the sample data from ./data
# into the postgreSQL database.
import psycopg2
from load_helpers import *


def insert_doc(id, doc):
    '''
    doc: dictionary represent a pre-processed code snipped.
    return: SQL Insert & tupla with values.
    '''
    insert_sql = "INSERT INTO code_snipped (id, code_string, code_toks_joined, anonymize_dict) VALUES(%s, %s, %s, %s)"
    return insert_sql, (id, doc['code_string'], doc['code_toks_joined'], str(doc['anonymize_dict']))

def insert_error(cursor,id_doc, doc):
    '''
    cursor: psycopg2 cursor object.
    id_doc: id of the document.
    doc: dictionary represent a pre-processed code snipped.
    '''
    # This function makes the relational model unfeasible, 
    # it is very expensive to insert data avoiding data redundancy.
    err_msg = doc['err_obj']['msg']
    # used for debug purposes.
    #print(f"Error msg: {err_msg}")
    #print(cursor.mogrify("SELECT id FROM bug WHERE msg = %s", (err_msg,))) 
    cursor.execute("SELECT id FROM err_obj WHERE msg = %s", (err_msg,))
    error_ids = cursor.fetchall()
    id_error = 0
    if len(error_ids) == 0:
        cursor.execute("INSERT INTO err_obj (msg) VALUES(%s) RETURNING id;", (err_msg,))
        id_error = cursor.fetchone()[0]
    else:
        id_error = error_ids[0]
    cursor.execute("INSERT INTO bug (code_id, error_id) VALUES(%s, %s);", (id_doc, id_error))

def TL(host, user, password):
    '''
    host: host of NoSQL database
    user: user of NoSQL database
    password: password of NoSQL database
    Transform & Load data into a SQL db (postgreSQL)
    '''
    print('Starting T(ransform) & L(load) data to SQL db')

    print(f'SQLDB Host: {host}')

    #establishing the connection
    conn = psycopg2.connect(
        database="postgres", user=user, password=password, host=host, port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()


    # Create schema.
    cursor.execute('''
    CREATE SCHEMA bifi; 
    SET SCHEMA 'bifi';
    DROP TABLE IF EXISTS bug;
    DROP TABLE IF EXISTS err_obj;
    DROP TABLE IF EXISTS code_snipped;

    CREATE TABLE code_snipped (
        id VARCHAR PRIMARY KEY, 
        code_string TEXT NOT NULL, 
        code_toks_joined TEXT NOT NULL, 
        anonymize_dict TEXT
        );

    CREATE TABLE err_obj (
        id SERIAL PRIMARY KEY, 
        msg TEXT NOT NULL
        );

    CREATE TABLE bug (
        id SERIAL PRIMARY KEY, 
        code_id VARCHAR, 
        error_id SERIAL, 
        CONSTRAINT fk_code 
            FOREIGN KEY(code_id) 
                REFERENCES code_snipped(id), 
        CONSTRAINT fk_error 
            FOREIGN KEY(error_id)
                REFERENCES err_obj(id)
        );
    ''')


    # Load documents.
    bad_json = load_original_json('./data/orig_bad_code/orig.bad.json')
    bad_ids = load_original_id('./data/orig_bad_code/orig.0.id')

    good_json = load_original_json('./data/orig_good_code/orig.good.json')
    good_ids = load_original_id('./data/orig_good_code/orig.0.id')

    # insert bad examples
    for id in bad_ids:
        doc = bad_json[id]
        
        query, vars = insert_doc(id, doc)
        cursor.execute(query, vars)
        insert_error(cursor, id, doc)

    # insert good examples
    for id in good_ids:
        doc = good_json[id]
        # insert
        query, vars = insert_doc(id, doc)
        cursor.execute(query, vars)

    #Closing the connections
    cursor.close()
    conn.close()
