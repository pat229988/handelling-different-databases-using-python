import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants

#url = 'your ur to doccument db'
#key = 'secret key by azure'
#client = cosmos_client.CosmosClient(url, {'masterKey': key})

from pydocumentdb import document_client
## cresential to azure cluster database
url = 'your ur to doccument db'
key = 'secret key by azure'

client = document_client.DocumentClient(uri, {'masterKey': key})

db_id = 'student'
db_query = "select * from r where r.id = '{0}'".format(db_id)
db = list(client.QueryDatabases(db_query))[0]
db_link = db['_self']

coll_id = 'user'
coll_query = "select * from r where r.id = '{0}'".format(coll_id)
coll = list(client.QueryCollections(db_link, coll_query))[0]
coll_link = coll['_self']

docs = client.ReadDocuments(coll_link)
print(list(docs))