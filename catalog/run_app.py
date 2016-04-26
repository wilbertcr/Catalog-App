from app.controllers import app
# Take your pick depending on which configuration you want to run.
from app.config.config import DevelopmentConfig
from app.db.database import init_db

if __name__ == "__main__":
    # Setup SQLAlchemy mappings and relationships.
    init_db()
    # Input appropriate configuration object
    app.config.from_object(DevelopmentConfig)
    # Run app
    app.run(host='0.0.0.0', port=5000)

