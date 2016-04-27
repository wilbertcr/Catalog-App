import database
from subprocess import call
from app.config.config import Config

setup_path = Config.BASE_DIR+"/app/db/setup_db.sh"
# Script sets up password and database in the database server.
call(setup_path)

# Initiate database tables(SQLAlchemy)
database.init_db()

populate_path = Config.BASE_DIR+"/app/db/populate_db.py"
# Populates database.
execfile(populate_path)
