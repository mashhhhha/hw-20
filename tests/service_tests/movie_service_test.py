import pytest
from dao.movie import MovieDAO
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_Dao: MovieDAO):
        self.movie_service = MovieService(movie_Dao)

    def test_get_one(self):
        certain_movie = self.movie_service.get_one(1)

        assert certain_movie is not None
        assert certain_movie.id is not None
        assert certain_movie.title == 'The Naked Gun'

    def test_get_all(self):
        filters = {
            "director_id": None,
            "genre_id": None,
            "year": None
        }
        all_movie = self.movie_service.get_all(filters)

        assert all_movie is not None
        assert len(all_movie) == 3
        assert type(all_movie) == list

    def test_create(self):
        new_movie = self.movie_service.create(
            {
                'id': '',
                'title': ''
            }
        )

        assert new_movie is not None
        assert new_movie.id == 3
        assert new_movie.title == 'The Naked Gun 3'

    def test_delete(self):
        movie = self.movie_service.delete(1)

        assert movie is None

    def test_upgrade(self):
        updated_movie = self.movie_service.update(
            {
                'id': '',
                'title': ''
            }
        )

        assert updated_movie is not None