from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base

# Replace this with your actual database URI
DATABASE_URI = 'postgresql://neondb_owner:JLrd8UXnN9EP@ep-yellow-shadow-a49j7ui8.us-east-1.aws.neon.tech/neondb?sslmode=require'

# Set up the engine and session
engine = create_engine(DATABASE_URI, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Bind the session to the Base class
Base.query = db_session.query_property()

# Initialize the database (for migrations, if needed)
def init_db():
    import models  # Ensure all models are imported
    Base.metadata.create_all(bind=engine)
