

import sqlite3


class JokeDB:
    """
    This class represents a database for jokes
    """
    def __init__(self, db_name):
        """
        This method creates a database for joke storage and classification
        """
        self._name = db_name

    def create_table(self, table_name):
        """
        Creating a table with id, rating and joke columns
        :param table_name: str
        """
        # creating basic database
        with sqlite3.connect(self._name) as connection:
            # creating cursor for operating with database
            cursor = connection.cursor()
            # create a table 'table_name' where the columns will be
            # 'id', 'rating', 'joke'
        cursor.execute(f""" CREATE table {table_name} (
                 id int, rating float, joke text)""")
        # in order to save changes, commit()
        connection.commit()
        print("created a table: ", table_name)

    def table_insert(self, table_name, joke):
        """
        Inserts a joke into a joke database into a specific table called
        table_name
        :param table_name: str
        :param joke: Joke object
        """
        data_tuple = (joke.get_idnum(), joke.get_rating(), joke.get_joke())
        # in order to insert to a created table in database
        with sqlite3.connect(self._name) as connection:
            cursor = connection.cursor()
            cursor.execute(f""" INSERT INTO {table_name} VALUES (?, ?, ?)
                   """, data_tuple)
            connection.commit()

    def index_select_from_table(self, table_name, start_id, finish_id):
        """
        Selects the needed data from the table by the index
        :param table_name: str
        :param start_id: int
        :param finish_id: int
        """
        with sqlite3.connect(self._name) as connection:
            cursor = connection.cursor()
            # selecting the needed columns by the names or if needed all - *
            cursor.execute(f""" SELECT id, rating, joke FROM {table_name} WHERE rowid <= {finish_id} and rowid >= {start_id}""")
            ids = cursor.fetchall()
        return ids


    def update_joke(self, table_name, joke_id, new_rating):
        """
        Updates the rating for a joke of a certain category
        (in specific table table_name) of a specific id joke_id
        PRECONDITION: new_rating should be positive float not greater than 10
        :param table_name: str
        :param joke_id: int
        :param new_rating: float
        """
        with sqlite3.connect(self._name) as connection:
            cursor = connection.cursor()
            # set rating of a joke to the new_rating
            cursor.execute(f""" UPDATE {table_name} SET rating = {new_rating} WHERE id = {joke_id}""")
            connection.commit()

    def tables(self):
        """
        Returns the list of names of tables that the database contains
        :return: lst
        """
        with sqlite3.connect(self._name) as connection:
            cursor = connection.cursor()
            cursor.execute(f""" SELECT name FROM sqlite_master WHERE type = 'table'""")
            tbs = cursor.fetchall()
        return tbs

    def get_column_from_table(self, col, table_name):
        """
        Returns the list of values in a column col
        of the table table_name
        :param col: str
        :param table_name: str
        :return: lst
        """
        with sqlite3.connect(self._name) as connection:
            cursor = connection.cursor()
            cursor.execute(f""" SELECT {col} FROM {table_name}""")
            data = cursor.fetchall()
        return data

    def get_joke_by_id(self, table_name, joke_id):
        """
        Returns a joke of a certain category
        (in specific table table_name) of a specific id (joke_id)
        :param table_name: str
        :param joke_id: int
        """
        with sqlite3.connect(self._name) as connection:
            cursor = connection.cursor()
            cursor.execute(f""" SELECT * FROM {table_name} WHERE id={joke_id} """)
            temp = cursor.fetchall()

        return temp

