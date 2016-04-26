import database
from subprocess import call

# Script sets up password and database in the database server.
call("./setup_db.sh")

# Initiate database tables(SQLAlchemy)
database.init_db()

# Populates database.
execfile("./populate_db.py")
