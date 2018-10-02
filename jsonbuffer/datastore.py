from dpath import util as dpath


class DataStore:

    data = {}

    def __init__(self):
        pass

    def get(self, path=''):
        if path == '':
            d = self.data
        else:
            # trows KeyError
            d = dpath.get(self.data, path)
        return d

    def set(self, d, path=''):
        if path == '':
            self.data = d
        else:
            # trows KeyError
            dpath.set(self.data, path, d)

