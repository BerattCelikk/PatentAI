# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database dosyasının yolu burda
SQLALCHEMY_DATABASE_URL = "sqlite:///./patentai.db"

# SQLAlchemy engine, veritabanıyla olan ana iletişim noktası gibi
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Not: connect_args={"check_same_thread": False} sadece SQLite için gereklidir.

# database sessionları için bir fabrika oluşturuyoz
# her bir session, veritabanıyla yapılacak bir dizi işlemin birimidir
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modellerimizin (veritabanı tablolarımızın) miras alacağı bir ana sınıf oluşturuyoruz.
Base = declarative_base()