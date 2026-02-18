import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../'))
sys.path.insert(0, project_root)

import pytest
from .....src.infrastructure.db.connection_aurora import AuroraPostgreSQLConnection

class TestDatabaseConnection:

    def test_create_database_engine(self):
        db_connection = AuroraPostgreSQLConnection()
        engine = db_connection.connect()

        assert engine is not None
