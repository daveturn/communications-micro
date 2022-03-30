
from email.generator import Generator
from typing import Callable
from enum import Enum, auto
from app.app.core.config import settings

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

from cassandra.cqlengine.connection import register_connection, set_default_connection
from cassandra.cqlengine.management import sync_table

from cassandra.cluster import Cluster, Session

from app.app.core.config import settings

def sync_all_tables():
    '''
            According to this, the connection must be made before models are declared
            https://stackoverflow.com/questions/39720240/cql-engine-exception-about-a-connection-name-not-existing-in-registry
    '''
    from app.app.cassandra.models import Contact, UpdatedContact
    sync_table(Contact)
    sync_table(UpdatedContact)



def get_session(username: str, password: str, host: str):        
    # Define your database names here.
    # Enum used here to reduce chance of typos

    auth_provider = None

    if username and password:
        auth_provider = PlainTextAuthProvider(
                username=username,
                password=password
        )

    cluster = Cluster(
            [host],
            auth_provider=auth_provider,
            protocol_version=3
    )

    session: Session = cluster.connect()
    # Create keyspace if it doesn't exist yet

    session.execute(f'''
    CREATE KEYSPACE IF NOT EXISTS {settings.KEYSPACE_NAME}
    WITH replication = {{'class': 'SimpleStrategy',
                            'replication_factor' : 1}}''')
    session.set_keyspace(settings.KEYSPACE_NAME)

    register_connection(str(session), session=session)
    set_default_connection(str(session))
    sync_all_tables()

    return session

