import json
from dpath import util as dpath


class DataStore:

    data = {}
    store_to = None

    def __init__(self, load_from=None, store_to=None):
        self.store_to = store_to

        if load_from is not None:
            self.load(load_from)

    def load(self, file_path):
        with open(file_path) as f:
            self.data = json.load(f)

    def get(self, path=''):
        if path == '':
            d = self.data
        else:
            # throws KeyError
            d = dpath.get(self.data, path)
        return d

    def set(self, d, path=''):
        if path == '':
            self.data.update(d)
        else:
            # throws KeyError
            dpath.set(self.data, path, d)
        self.save()

    def save(self):
        if self.store_to:
            with open(self.store_to, 'w') as f:
                json.dump(self.data, f)

