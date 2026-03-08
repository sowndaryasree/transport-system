import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = os.getenv("DATABASE_URL")
#DATABASE_URL = "postgresql://postgres:Sowndaryasree@9894@db.pqkuncbhligypafaodgn.supabase.co:5432/postgres"
DATABASE_URL = "postgresql+psycopg2://postgres.pqkuncbhligypafaodgn:Sowndaryasree@aws-1-ap-southeast-1.pooler.supabase.com:6543/postgres"
engine = create_engine(DATABASE_URL,pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()