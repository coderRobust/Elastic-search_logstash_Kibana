import json
import requests
import elasticsearch
from elasticsearch import Elasticsearch
import sys

def elasticsearch_connection():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    return es

def data_insert_elastic(index_name, e1, es, ids):
    res = es.index(index=index_name,doc_type='employee',id=ids,body=e1)
    print(res)

if __name__ == '__main__':
    index_name = sys.argv[1]
    e1={
    "first_name":"nitin",
    "last_name":"panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
    }
    #print(array)
    ids = 0
    print(index_name)
    try:
        es = elasticsearch_connection()
        #import pdb; pdb.set_trace()
        with open('log.json', 'r') as f:
            #array = f.readline()
            for ex in f.readlines():
                ids +=1
                data_insert_elastic(str(index_name), ex, es, ids)
    except Exception:
        raise Exception
    else:
        ids = 0
        print('Successfully updated')