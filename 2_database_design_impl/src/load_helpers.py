
import json

def load_original_id(path):
    '''
    path: path of id file.
    return: list of strings with code snippets ids.
    '''
    # read file
    with open(path, 'r') as id_file:
        data=id_file.readlines()

    return list(map(lambda i: i.replace('\n',''), data))


def load_original_json(path):
    '''
    path: path of json file.
    return: parsed json with the pre-processed data.
    '''
    # read file
    with open(path, 'r') as json_file:
        data=json_file.read()

    # parse file
    return json.loads(data)

