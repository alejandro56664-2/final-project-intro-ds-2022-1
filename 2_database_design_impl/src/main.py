# This is the entry point for the container that Transform de data
# in their original state to a SQL and NoSQL databases.

from populate_sql import TL as TL_sql
from populate_nosql import TL as TL_nosql

import os

user_nosql = os.getenv('NOSQLDB_USER')
pass_nosql = os.getenv('NOSQLDB_PASS')
host_nosql = os.getenv('NOSQLDB_HOST')

user_sql = os.getenv('SQLDB_USER')
pass_sql = os.getenv('SQLDB_PASS')
host_sql = os.getenv('SQLDB_HOST')

TL_nosql(host_nosql, user_nosql, pass_nosql)
TL_sql(host_sql, user_sql, pass_sql)