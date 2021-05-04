class Utilities:
    RELATIONSHIPS_TO_DICT = False

    def __iter__(self):
        return self.to_dict().items()

    def to_dict(self, rel=None):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        res = {column.key: getattr(self, attr)
               for attr, column in self.__mapper__.c.items()}
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                value = getattr(self, attr)
                if isinstance(value, list):
                    res[relation.key] = [obj.to_dict(rel=False) for obj in getattr(self, attr)]
                else:
                    if value is not None:
                        res[relation.key] = value.to_dict(rel=False)
                    else:
                        res[relation.key] = None
        return res