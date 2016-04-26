from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker

if __package__ is None:
    # File is not being used as a package, we need to add
    # upper levels to PYTHONPATH so import is succesfull.
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
    from app.config.config import Config
else:
    # File is being used as a package so we can just use a relative import.
    from ..config.config import Config

engine = create_engine(Config.DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.metadata.bind = engine
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Category, Item
    Category.items = relationship(Item, order_by=Item.id, back_populates="category")
    Base.metadata.create_all(bind=engine)
