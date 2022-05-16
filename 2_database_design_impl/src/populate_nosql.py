# This script Transform & Load the sample data from ./data
# into the MongoDB database.

from pymongo import MongoClient
from load_helpers import *

def TL(host, user, password):
    '''
    host:
    user:
    password:
    Transform & Load data into a NoSQL db (MongoDB)
    '''
    print('Starting T(ransform) & L(load) data into NoSQL db')

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb://{user}:{password}@{host}:27017/"

    print(CONNECTION_STRING)

    # Create a connection using MongoClient.
    client = MongoClient(CONNECTION_STRING)
    
    print("Connection created successfully........")

    # Load documents.
    bad_json = load_original_json('./data/orig_bad_code/orig.bad.json')
    bad_ids = load_original_id('./data/orig_bad_code/orig.0.id')

    good_json = load_original_json('./data/orig_good_code/orig.good.json')
    good_ids = load_original_id('./data/orig_good_code/orig.0.id')


    # Insert documents.
    # Probably this is not the most performant solution, but is
    # sufficient for the PoC.

    db = client['nosqldb']
    bad_code = db['bad_code']
    good_code = db['good_code']

    for id in bad_ids:
        doc = bad_json[id]
        # insert
        bad_code.insert_one(doc)
        #print(f"code_string: {doc['code_string']}")

    for id in good_ids:
        doc = good_json[id]
        # insert
        good_code.insert_one(doc)
        #print(f"code_string: {doc['code_string']}")


