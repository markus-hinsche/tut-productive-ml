{
    'dataset_loader_train': {
        '__factory__': 'palladium.dataset.CSV',
        'path': 'iris.data',
        'names': [
            'sepal length',
            'sepal width',
            'petal length',
            'petal width',
            'species',
        ],
        'target_column': 'species',
        'nrows': 100,
    },

    'dataset_loader_test': {
        '__copy__': 'dataset_loader_train',
        'nrows': None,
        'skiprows': 100,
    },

    'model': {
        '__factory__': 'sklearn.linear_model.LogisticRegression',
        'C': 0.1,
    },

    'model_persister': {
        '__factory__': 'palladium.persistence.Database',
        'url': 'sqlite:///iris-model.db',
    },
}
