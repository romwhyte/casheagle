import sys
from casheagle import app
from db import sqllitedb


if __name__ == "__main__":
    db = sqllitedb.Database()
    app.run(db)