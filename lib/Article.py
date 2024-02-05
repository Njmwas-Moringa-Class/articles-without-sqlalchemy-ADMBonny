class Article:
    pass
    _all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all_articles.append(self)
        magazine._articles.append(self)
        author._articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
    
    @classmethod
    def all(cls):
        return cls._all_articles