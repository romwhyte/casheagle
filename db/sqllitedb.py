from sqlalchemy import Table,Sequence, MetaData,create_engine, Column, Integer, String 
from sqlalchemy.orm import sessionmaker
from db import models
class Database:

    def __init__(self, *args, **kwargs):
        engine = create_engine('sqlite:///borrower.db', echo = True)

        # generate the database schema
        models.Base.metadata.create_all(engine)

        # create a configured "Session" class
        self.session = sessionmaker(bind=engine)

    def insert(self, *args, **kwargs):
        self.session.add(args[0])
        self.session.commit()

    def delete(self, *args, **kwargs):
        self.session.delete(args[0])
        self.session.commit()

    def find(self, *args, **kwargs):
        return self.session.query(args[0]).filter_by(id=args[1]).first()

    def findAll(self, *args, **kwargs):
        return self.session.query(args[0]).all()

    def close(self):
        session.close()
