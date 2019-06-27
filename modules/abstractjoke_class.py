

# This module contains abstract class Joke


class AbstractJoke:
    """
    This class is for a representation of a basic joke
    """
    def __init__(self, idnum=0, label='', avRating=0, text=''):
        """
        This method constructs a Joke object
        :param idnum: int
        :param label: str
        :param avRating: float
        :param text: str
        """
        self._idnum = idnum
        self._label = label
        self._avRating = avRating
        self._text = text

    def __str__(self):
        """
        This method returns a string representation of a Joke object
        :return: str
        """
        return "Joke ID: {0}\nCategory: {1}\n" \
               "Average rating: {2}\n{3}".format(self._idnum,
                                                 self._label,
                                                 self._avRating,
                                                 self._text)

    def set_id(self, idnum):
        raise NotImplementedError

    def set_label(self, label):
        raise NotImplementedError

    def set_rating(self, rating):
        raise NotImplementedError

    def set_joketext(self, text):
        raise NotImplementedError

    def get_rating(self):
        """
        This method returns average rating of a joke
        :return: float
        """
        return self._avRating

    def get_idnum(self):
        """
        This method returns id number of a joke
        :return: int
        """
        return self._idnum

    def get_joke(self):
        """
        This method returns the text of a joke
        :return: str
        """
        return self._text

    def get_category(self):
        """
        This method returns the category of a joke
        :return: str
        """
        return self._label





