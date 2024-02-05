class Magazine:
    pass
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        self._category = value
    
    def contributors(self):
        return list(set([article.author for article in self._articles]))
    
    def article_titles(self):
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        return [author for author in set(authors) if authors.count(author) > 2]
    
    @classmethod
    def all(cls):
        return cls._all_magazines
    
    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all_magazines:
            if magazine.name == name:
                return magazine
        return None