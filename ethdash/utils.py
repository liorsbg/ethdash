import os
import json

def current_directory():
    '''
    :return: Absolute path of file from which this function is run
    '''
    return os.path.dirname(os.path.realpath(__file__))

def load_local_json(name):
    return json.load(open(os.path.join(current_directory(), name)))
