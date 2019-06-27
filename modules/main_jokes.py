

from joke_db import JokeDB
from jokes import JokeSetFromFile
import random


joke_db = JokeDB("joke_db.db")

def create_db(joke_db):
    """
    This function creates a sqlite joke database
    :param joke_db: JokeDB
    """
    joke_set = JokeSetFromFile("stupidstuff.json")
    joke_set.read_jokes()
    joke_set = joke_set.get_jokes()

    for category in joke_set:
        print(category)
        joke_db.create_table(category)
        for joke in joke_set[category]:
            joke_db.table_insert(category, joke)

    # for selecting specific rows in specific table by indexes
    # for i in joke_db.index_select_from_table("Insults", 0, 8):
        # print(i)

    # to print the names of the tables in database
    # print(joke_db.tables())

# create_db(joke_db)

def generate_random_joke(joke_db=JokeDB("joke_db.db")):
    """
    This function generates random jokes from the joke
    database
    :param joke_db: JokeDB
    :return: lst
    """
    lst = joke_db.tables()
    category = random.choice(lst)
    """
    #categories = random.choices(lst, k=10)
    jokes = []
    for each in categories:
        category = each[0]
        ids = joke_db.get_column_from_table('id', category)
        id = random.choice(ids)
        joke = joke_db.get_joke_by_id(category, id[0])
        jokes.extend(joke)
    """
    ids = joke_db.get_column_from_table('id', category[0])
    id = random.choice(ids)
    joke = joke_db.get_joke_by_id(category[0], id[0])
    return [category[0], *joke[0]]


