from sqlalchemy import create_engine, MetaData
from databases import Database
import os

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:551553Hm@@localhost:5432/mydatabase"
# postgre isn't supposed to be running on local host, thus the URL is incorrect 
# also the password set in the .env is different than the one set in the URL


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"


# SQLALCHEMY_DATABASE_URL = (
#     f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
#     f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
# )



database = Database(SQLALCHEMY_DATABASE_URL)
metadata = MetaData ()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
