import pytest
from faker import Faker
# from main.models import Author


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

# @pytest.fixture(scope='function')
# def author_fixt():
#     """
#     Создание нового Автора и получение его.
#     """
#     author = Author.objects.create()
#     yield author

# @pytest.fixture(scope='module')
# @pytest.fixture(scope='session')
@pytest.fixture(scope='function')
def tt():
    yield 123


@pytest.fixture(scope='function')
def fake_fixt():
    """
    Генерация данных для фейкового пользователя.
    """

    faker = Faker()
    yield faker
