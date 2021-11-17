# Предметная область 10: 
# Книга - книжный магазин
# Запросы Д:
#   1.«Книга» и «Книжный магазин» связаны соотношением один-ко-многим.
#     Выведите список всех книг, у которых название заканчивается на "е", и названия книжных магазинов с этими книгами.
#   2.«Книга» и «Книжный магазин» связаны соотношением один-ко-многим.
#     Выведите список книг со средней датой появления в каждом магазине, отсортированный по средней дате.
#     (отдельной функции вычисления среднего значения в Python нет, нужно использовать комбинацию функций вычисления суммы и количества значений).
#   3. «Книга» и «Книжный магазин» связаны соотношением многие-ко-многим.
#     Выведите список всех книжных магазинов, у которых название начинается с буквы «П», и список книг в них.

from operator import itemgetter
from store.shop import shops
from store.book import books
from store.book_shop import shops_with_books

def main():
  print("\n \\/ \\/ \\/ \\/ \\/ \\/ \n")

  # Соединение данных один-ко-многим 
  books_join_shops = [{'books': b, 'shops': s}
    for b in books
    for s in shops 
    if b.shop_id == s.id
  ]

  print('Задание Д-1')
  # Выведем id, name, appear_year таблицы "Книга"
  # для записей с name, заканчивающимся на 'е'.
  # И выведем магазины с этими книгами
  D1 = [(x['books'].id, x['books'].name, x['books'].appear_year, x['shops'].name)
    for x in books_join_shops
    if x['books'].name.endswith('е')
  ]
  for x in D1:
    print(x)
  

  print('\nЗадание Д-2')
  # Выведем название магазина, средний возраст книги в магазине
  # Сортируя по этому среднему

  # Заведем таблицу с накапливаемой суммой дат и количеством книг:
  shop_sum_count_dict = {}
  for b_shops_row in books_join_shops:
    shop_name = b_shops_row['shops'].name
    appear_year = b_shops_row['books'].appear_year

    if shop_name in shop_sum_count_dict:
      shop_sum_count_dict[shop_name]['sum'] = shop_sum_count_dict[shop_name]['sum'] + appear_year
      shop_sum_count_dict[shop_name]['count'] = shop_sum_count_dict[shop_name]['count'] + 1
    else:
      shop_sum_count_dict[shop_name] = {'sum': appear_year, 'count': 1}

  D2 = sorted(
    [(shop_name, shop_sum_count_dict[shop_name]['sum'] / shop_sum_count_dict[shop_name]['count'])
      for shop_name in shop_sum_count_dict
      if shop_sum_count_dict[shop_name]['count'] != 0
    ],
    key=itemgetter(1), reverse=True
  )
  for x in D2:
    print(x)

  print('\nЗадание Д-3')

  # Соединение данных многие-ко-многим
  many_to_many = [(c.name, co.shop_id, co.book_id)
    for c in shops
        for co in shops_with_books 
            if c.id == co.shop_id]

  shops_with_books_table = [(book.name, book.appear_year, shop_name)
    for shop_name, shop_id, book_id in many_to_many
        for book in books if book.id == book_id]

  D3 = {}
  for shop in shops:
    if shop.name.startswith('П'):
        books_of_shop = list(filter(lambda i: i[2] == shop.name, shops_with_books_table))
        books_names = [x for x, _, _ in books_of_shop]
        D3[shop.name] = books_names
  for d in D3:
    print(d, ':', D3[d])
    
  print("\n /\\ /\\ /\\ /\\ /\\ /\\ \n")
 
if __name__ == '__main__':
  main()

