from time import sleep
from subprocess import call
from os import path
from db import database
from config.config import Config

setup_path = path.join(Config.BASE_DIR, "app/bin/setup_db.sh")
reset_db_path = path.join(Config.BASE_DIR, "app/db/reset_db.sql")
populate_path = path.join(Config.BASE_DIR, "app/db/populate_db.py")


def build_alter_role_query(username, password):
    """Write a SQL statement to defined a role"""
    statement = "ALTER ROLE {0} WITH ENCRYPTED PASSWORD '{1}';\n".format(username, password)
    return statement


def build_drop_database_query(db_name):
    statement = "DROP DATABASE IF EXISTS {0};\n".format(db_name)
    return statement


def build_create_database_query(db_name):
    statement = "CREATE DATABASE {0};\n".format(db_name)
    return statement


def store_statements_into_reset_file(filename, statements):
    """Write an SQL statement to a file"""
    with open(filename, 'w') as opened_file:
        for statement in statements:
            opened_file.write(statement)

# Build a list of SQL statements.
sql_statements = ["/* This file is automatically created. Anything you'll write here "
                  "will be deleted when database is setup again.*/\n",
                  build_alter_role_query(Config.DB_CONNECT_OPTIONS['username'],
                                         Config.DB_CONNECT_OPTIONS['password']),
                  build_drop_database_query(Config.DB_CONNECT_OPTIONS['dbname']),
                  build_create_database_query(Config.DB_CONNECT_OPTIONS['dbname'])]

# Write list of SQL statements to file
store_statements_into_reset_file(reset_db_path, sql_statements)

# Let's allow some time for the writing to be done.
sleep(2)

# Now we call the script we just created.
call(setup_path)

# Initialize database tables(SQLAlchemy)
database.init_db()

# Now we populate the database.

# Here's how you do it in Python 2
# execfile(populate_path)

# Here's how that's done in Python 3
with open(populate_path) as f:
    code = compile(f.read(), populate_path, 'exec')
    exec(code)
