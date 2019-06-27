

# This module is for getting jokes from jokes_stupidstuff.json

from abstractjoke_class import AbstractJoke
import json


class Joke(AbstractJoke):
    """
    This class is for a representation of a Joke from
    a jokes_stupidstuff.json file
    """
    def set_id(self, idnum):
        self._idnum = idnum

    def set_label(self, label):
        self._label = label

    def set_rating(self, rating):
        self._rating = rating

    def set_joketext(self, text):
        self._text = text


class JokeSetFromFile:
    """
    Class for representation of jokeset
    from jokes_stupidstuff.json file
    """
    def __init__(self, filename):
        """
        Constructs the JokeSetFromFile object
        :param filename: str
        """
        self._filename = filename
        # calculating when run
        self._num_jokes = 0
        self._jokedict = {}

    def size(self):
        return self._num_jokes

    def read_jokes(self):
        with open(self._filename, encoding="UTF-8") as f:
            f = json.load(f)
            for each in f:
                if self.check_quality(each):
                    category = self._clear_category(each["category"])
                    new_joke = Joke(self.size(), category,
                                    each["rating"], each["body"])
                    self._num_jokes += 1

                    if category not in self._jokedict:
                        self.add_category(category)

                    self._jokedict[category].append(new_joke)

    @staticmethod
    def _clear_category(category):
        return "".join(list(filter(lambda x: x.isalpha(), category)))

    def add_category(self, category):
        self._jokedict[category] = []

    def get_jokes(self):
        return self._jokedict


    @staticmethod
    def check_quality(joke_dict):
        """
        Returns True if there is full information about the joke, False if one
        or more keys have no information
        PRECONDITION joke_dict should have keys 'body', 'category'
        'rating'
        :param joke_dict: dict
        :return: bool
        """
        return joke_dict['body'] != None and joke_dict['category'] != None\
               and joke_dict['rating'] != None








