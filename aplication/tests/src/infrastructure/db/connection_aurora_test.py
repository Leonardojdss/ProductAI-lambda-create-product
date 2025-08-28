import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../'))
sys.path.insert(0, project_root)

import pytest
from .....src.infrastructure.db.connection_aurora import AuroraPostgreSQLConnection

def test_create_database_engine():
    db_connection = AuroraPostgreSQLConnection()

    engine = db_connection.connect()
    print(engine)