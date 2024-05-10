from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# engine = create_engine("postgresql+psycopg2://postgres:123456789@localhost:5432/123456789")
engine = create_engine("postgresql://postgres:123456789@localhost/123456789")

Base = declarative_base()
Session = sessionmaker()
