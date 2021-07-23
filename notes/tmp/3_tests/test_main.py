from foo.main import foo, inc


def test_foo():
    assert len(foo()) > 0


def test_answer():
    assert inc(3) == 4

# Тесты всех директорий (текущая и вложенные - autodiscovery).
# pytest

# Тесты файла.
# pytest test_main.py

# Отдельный тест из файла
# pytest test_main.py::test_foo

# Тесты класса TestCl из файла test_main.py.
# pytest test_main.py::TestCl
