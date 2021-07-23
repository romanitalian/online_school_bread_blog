
```shell
#!/bin/zsh

make new-migrate
make migrate

make shell
author = Author.objects.last()
# книги ещё не созданы
book = Book.objects.last()
book = Book.objects.create(title='book title', author=author)
book = Book.objects.create(title='book title', author_id=author.id)

book.author
book.author.id
book.author.name
book.author.full_name
book.author_id

python blog/manage.py generate_data
Book.objects.count()
Author.objects.count()
```

```python
# Problem: N+1
books = Book.objects.all()
for book in books:
  print(book.id, book.title, book.author.name)
```

А нужно вот так (чтобы сразу джанго вытащил все данные):

https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all
```sqlite-psql
SELECT Products.ProductName, Categories.CategoryName FROM Products
INNER JOIN Categories ON Products.CategoryId = Categories.CategoryId

SELECT Products.ProductName, Categories.CategoryName FROM Products, Categories
WHERE Categories ON Products.CategoryId = Categories.CategoryId
```



```python
books = Book.objects.all().select_related('author')
for book in books:
  print(book.id, book.title, book.author.name)


list([Book.objects.all().select_related('author')])
```

```python
author = Author.objects.order_by('?').last()
Book.objects.filter(author=author).count()

# Взять все книги данного Автора
author.book_set.all()
author.book_set.all().count()


# models.Book: related_name='books'
author = Author.objects.order_by('?').first()
author.books.count()

Book.objects.filter(author=author).count()
Book.objects.filter(author_id=author.id).count()
```


```python
# Problem: N+1
authors = Author.objects.all()
for author in authors:
    print(author.id, author.books.count())

# sub select
authors = Author.objects.all().prefetch_related('books')
for author in authors:
    list([author.id, author.books.count()])
```


```python
# выборка не будет в базу ходить
authors = Author.objects.filter(age__lt=18).all()
# ... выборка только сейчас
authors.count()

# список кортежей
list(authors.values_list('id'))
# только список
list(authors.values_list('id', flat=True))

# А теперь сделаем выборку: Количество книг, где автор младше 18
author_ids = authors.values_list('id', flat=True)
Book.objects.filter(author_id__in=author_ids).count()


Book.objects.filter(author__age__lt=18).count()
Book.objects.filter(author__email__endswith='gmail.com').count()
Book.objects.filter(author__email__endswith='hotmail.com').count()

list(Author.objects.all().values('email'))
list(Author.objects.all().values_list('email', flat=True))
```




------------------------------
python blog/manage.py sqlmigrate main 0002
#------------------------------
pip install django-extensions
INSTALLED_APPS = [
    'django_extensions',

python src/manage.py shell_plus --print-sql

#------------------------------
python src/manage.py shell_plus --print-sql

from time import time

st = time()
st

end = time()
end - st

python src/manage.py createsuperuser


pip install django
pip install Faker
pip install django_extensions
pip install django-debug-toolbar


pip install Celery
brew install rabbitmq

cd src
celery -A core worker -l info

celery -A core beat -l info

-- CLI intreface
cd src
celery -A core events

-- WEB interface
pip install flower
cd src
celery -A core flower



```shell
file = open('/tmp/test.txt', 'w')
type(file)
dir(file)

import csv
import io
file = io.StringIO()
type(file)
dir(file)

file.write('hello')
file.seek(0)
file.read()
writer = csv.writer(file)
writer.writerow([1, 2])
```


```python
for _ in range(1000): post = Post.objects.last(); post.pk = None; post.save()
```



# python ./blog/manage.py show_urls
# pip install django-shell-plus



