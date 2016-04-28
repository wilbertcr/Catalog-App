import database
from time import sleep
from subprocess import call
from app.config.config import Config

setup_path = Config.BASE_DIR+"/app/db/setup_db.sh"
reset_db_path = Config.BASE_DIR+"/app/db/reset_db.sql"
populate_path = Config.BASE_DIR+"/app/db/populate_db.py"

sql_command_1 = "ALTER ROLE "+Config.DB_CONNECT_OPTIONS['username']+" WITH ENCRYPTED PASSWORD '"+\
                Config.DB_CONNECT_OPTIONS['password']+"';\n"
sql_command_2 = "DROP DATABASE IF EXISTS "+Config.DB_CONNECT_OPTIONS['dbname']+";\n"
sql_command_3 = "CREATE DATABASE "+Config.DB_CONNECT_OPTIONS['dbname']+";\n"
warning = "/* This file is automatically created. Anything you'll write here will " \
          "be deleted when database is setup again.*/\n"
reset_db_file = open(reset_db_path, 'w')
reset_db_file.write(sql_command_1)
reset_db_file.write(sql_command_2)
reset_db_file.write(sql_command_3)
reset_db_file.close()
sleep(2)
# Script sets up password and database in the database server.

call(setup_path)

# Initiate database tables(SQLAlchemy)
database.init_db()

# Populates database.
execfile(populate_path)
