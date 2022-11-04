import pytest
from dao.genre import GenreDAO
from service.genre import GenreService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_Dao: GenreDAO):
        self.genre_service = GenreService(genre_Dao)

    def test_get_one(self):
        certain_genre = self.genre_service.get_one(1)

        assert certain_genre is not None
        assert certain_genre.id == 1
        assert certain_genre.name == 'horror'

    def test_get_all(self):
        all_genres = self.genre_service.get_all()

        assert all_genres is not None
        assert type(all_genres) == list
        assert len(all_genres) == 3

    def test_create(self):
        new_genre = self.genre_service.create(
            {
                'id': '', 'name': ''
            }
        )

        assert new_genre is not None
        assert new_genre.id == 3
        assert new_genre.name == 'comedy'

    def test_delete(self):
        genre = self.genre_service.delete(1)

        assert genre is None

    def test_update(self):
        updated_genre = self.genre_service.update(
            {
                'id': '',
                'name': ''
            }
        )

        assert updated_genre is not None