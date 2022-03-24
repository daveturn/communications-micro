import requests

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from decouple import config


versium_url = 'https://api.versium.com/v2/contact'

versium_headers = {
    "Accept": "application/json",
    "x-versium-api-key": config('VERSIUM_API_KEY')
}

auth_provider = PlainTextAuthProvider(
        username=config('CASSANDRA_USER'),
        password=config('CASSANDRA_PASS')
)
cluster = Cluster(
        [config('CASSANDRA_HOST'), ],
        auth_provider=auth_provider
)
session = cluster.connect()
rows = session.execute('SELECT * FROM candidates.fec_candidates limit 1')
for user_row in rows:
    print('-------------')
    name = user_row.name.split(',')
    querystring = {
        'output[]': ['email', 'phone', ],
        'first': name[1],
        'last': name[0],
        'city': user_row.city,
        'state': user_row.state,
        'zip': user_row.zip_code,
        'country':'US',
        'match_type':'hhld',
        'cfg_maxrecs':'1'
    }
    
    response = requests.request(
        'GET',
        versium_url,
        headers=versium_headers,
        params=querystring
    )
    print(response.text)
