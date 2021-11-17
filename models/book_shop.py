class BookShop:
    """
    Книги и магазины
    для реализации связи многие-ко-многим
    """

    def __init__(self, shop_id, book_id):
        self.book_id = book_id
        self.shop_id = shop_id