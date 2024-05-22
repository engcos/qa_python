from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

import pytest
from main import BooksCollector

@pytest.fixture()
def collector():
    collector = BooksCollector()
    collector.books_genre = {
        'Мстители': 'Фантастика',
        'Аватар': 'Фантастика',
        'Гордость и предубеждение и зомби': '',
        'Достать ножи': '',
        'Позже': 'Ужасы',
        'Институт': 'Ужасы',
        'Женитьба': 'Комедии',
    }
    collector.favorites = ['Происхождение', 'Триггер', 'Мстители']
    return collector

@pytest.mark.parametrize('name, genre', [
    ('Гордость и предубеждение и зомби', 'Фантастика')
])
def test_set_book_genre_if_genre_equal_true(collector, name, genre):
    collector.set_book_genre(name, genre)
    assert collector.books_genre[name] == genre

@pytest.mark.parametrize('name, expected_genre', [
    ('Позже', 'Ужасы'),
    ('Институт', 'Ужасы'),
    ('Женитьба', 'Комедии')
])
def test_get_book_genre_compare_with_correct_genre(collector, name, expected_genre):
    assert collector.get_book_genre(name) == expected_genre

@pytest.mark.parametrize('genre, expected_result', [
    ('Ужасы', ['Позже', 'Институт']),
    ('Фантастика', ['Мстители', 'Аватар']),
    ('Комедии', ['Женитьба'])
])
def test_get_books_with_specific_genre_genre_true(collector, genre, expected_result):
    assert collector.get_books_with_specific_genre(genre) == expected_result

@pytest.mark.parametrize('expected_result', [{
    'Мстители': 'Фантастика',
    'Аватар': 'Фантастика',
    'Гордость и предубеждение и зомби': '',
    'Достать ножи': '',
    'Позже': 'Ужасы',
    'Институт': 'Ужасы',
    'Женитьба': 'Комедии'
}])
def test_get_books_genre_nothing_dict_true(collector, expected_result):
    assert collector.get_books_genre() == expected_result

@pytest.mark.parametrize('expected_result', [['Мстители', 'Аватар']])
def test_get_books_for_children_wait_that_returned_two_books(collector, expected_result):
    assert collector.get_books_for_children() == expected_result

@pytest.mark.parametrize('name', ['Мстители'])
def test_add_book_in_favorites_book_in_dict_book_added_in_favorites(collector, name):
    collector.add_book_in_favorites(name)
    assert name in collector.favorites

@pytest.mark.parametrize('name', ['Происхождение', 'Триггер'])
def test_delete_book_from_favorites_name_book_book_deleted(collector, name):
    collector.delete_book_from_favorites(name)
    assert name not in collector.favorites

@pytest.mark.parametrize('expected_result', [['Происхождение', 'Триггер', 'Мстители']])
def test_get_list_of_favorites_books_do_nothing_return_all_fav_books(collector, expected_result):
    assert collector.get_list_of_favorites_books() == expected_result

@pytest.mark.parametrize('name', ['Новая книга'])
def test_add_new_book(collector, name):
    collector.add_new_book(name)
    assert name in collector.books_genre
    assert collector.books_genre[name] == ''