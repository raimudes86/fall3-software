class Book:
    _author:str
    _title:str
    _pages:int

    #オブジェクト生成時に_authorフィールドと_titleフィールドをセットする
    def __init__(self, author, title):
        self._author = author
        self._title = title
        self._pages = 0

    #さらにメソッドをー追加
    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self,p):
        self._pages = p

    def print_author(self):
        print(self.author)

    def print_title(self):
        print(self.title)

    def print_pages(self):
        print(self.pages)

    def print_details(self):
        self.print_author()
        self.print_title()
        self.print_pages()

if __name__ == "__main__":
  b = Book("夏目漱石", "吾輩は猫である")
  b.pages = 564
  b.print_details()
  b2 = Book("Charles Dickens", "A Christmas Carol")
  b2.pages = 189
  b2.print_details()

