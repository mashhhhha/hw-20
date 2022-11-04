from unittest.mock import MagicMock

import pytest
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_Dao():
    """
    fixture for director service tests
    """
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='Скорсезе')
    d2 = Director(id=2, name='Тарантино')
    d3 = Director(id=3, name='Балабанов')

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=Director(id=3, name='Балабанов'))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock(return_value=Director(id=3, name='Ричи'))

    return director_dao


@pytest.fixture()
def genre_Dao():
    """
    fixture for genre service tests
    """

    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='milf')
    g2 = Genre(id=2, name='stepmom')
    g3 = Genre(id=3, name='amateur')

    genre_dao.get_one = MagicMock(return_value=Genre(id=1, name='horror'))
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])
    genre_dao.create = MagicMock(return_value=Genre(id=3, name='comedy'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock(return_value=Genre(id=4, name='action'))

    return genre_dao


@pytest.fixture()
def movie_Dao():
    """
    fixture for movie service tests
    """

    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='The Naked Gun')
    m2 = Movie(id=2, title='The Naked Gun 2')
    m3 = Movie(id=3, title='The Naked Gun 3')

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=Movie(id=3, title='The Naked Gun 3'))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock(return_value=Movie(id=4, title='The Naked Gun 4'))

    return movie_dao