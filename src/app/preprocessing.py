import os
import pandas as pd


class Preprocessing:
    def __init__(self, name):
        self.name = name.lower()
        self.data = {}

        root_dir = os.path.dirname(os.path.abspath(__file__))
        directory_template = '{root_dir}/../../data/{name}/'
        self.directory = directory_template.format(root_dir=root_dir, name=name)

        if not os.path.exists(self.directory):
            print(f'Creating "{name}" directory for you!')
            os.makedirs(self.directory)

    def load_data(self, filename, filetype='csv', *, name, **kwargs):
        filepath = f'{self.directory}/{filename}'
        df = getattr(pd, f'read_{filetype}')(filepath, **kwargs)
        self.data[name] = df
        return df

    def save(self, name, filetype='csv', **kwargs):
        filepath = f'{self.directory}/{name}.{filetype}'
        getattr(self.data[name], f'to_{filetype}')(filepath, **kwargs)

    def cleanup(self, name, *, drop=False, drop_duplicates=False):
        data = self.data[name]

        if drop is not False:
            data = data.drop(columns=drop)

        if drop_duplicates is True:
            data = data.drop_duplicates()

        self.data['clean'] = data

    def one_hot_encode(self, *, columns):
        if 'clean' not in self.data:
            print('Can not find clean data')
            return

        data = self.data['clean']
        categorical = pd.get_dummies(data[columns], dtype='int')
        data = pd.concat([data, categorical], axis=1, sort=False)
        self.data['clean'] = data

        return data

    def get(self, name):
        return self.data[name]

    def set(self, name, value):
        self.data[name] = value
