# This is the entry point for the container that Transform de data
# in their original state to a SQL and NoSQL databases.

from populate_sql import TL as TL_sql
from populate_nosql import TL as TL_nosql

TL_nosql()
TL_sql()