import pytest
from dao.director import DirectorDAO
from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_Dao: DirectorDAO):
        self.director_service = DirectorService(director_Dao)

    def test_get_one(self):
        certain_director = self.director_service.get_one(5)

        assert certain_director is not None
        assert certain_director.id is not None
        assert certain_director.name == 'Скорсезе'

    def test_get_all(self):
        all_directors = self.director_service.get_all()

        assert all_directors is not None
        assert len(all_directors) == 3
        assert type(all_directors) == list

    def test_create(self):
        new_director = self.director_service.create({
            'id': '',
            'name': ''})

        assert new_director is not None
        assert new_director.id == 3
        assert new_director.name == 'Балабанов'

    def test_delete(self):
        director = self.director_service.delete(2)

        assert director is None

    def test_update(self):
        updated_director = self.director_service.update(
            {
                'id': '',
                'name': ''
            }
        )

        assert updated_director is not None