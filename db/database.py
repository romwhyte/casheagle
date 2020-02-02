from sqlalchemy import Table,Sequence, MetaData,create_engine, Column, Integer, String 
from sqlalchemy.orm import sessionmaker, scoped_session
from db import tables

class Database:

    def __init__(self, *args, **kwargs):
        self.engine = create_engine(args[0], echo=kwargs['echo'])

        # generate the database schema
        tables.Base.metadata.create_all(self.engine)

        # create a configured "Session" class
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        self.session = self.Session()

    def save(self, *args, **kwargs):
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

    def reset(self):
        for tbl in reversed(tables.Base.metadata.sorted_tables):
            self.engine.execute(tbl.delete())

