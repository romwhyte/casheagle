import sys
from casheagle import app
from db import database


if __name__ == "__main__":
    db = database.Database('sqlite:///borrower.db')
    app.run(db)