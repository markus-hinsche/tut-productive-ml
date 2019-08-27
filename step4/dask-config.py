{
    'grid_search': {
        '__factory__': 'dask_ml.model_selection.GridSearchCV',
        'estimator': {'__copy__': 'model'},
        'param_grid': {'__copy__': 'grid_search.param_grid'},
        'scoring': {'__copy__': 'scoring'},
        'cv': {'__copy__': 'grid_search.cv'},
        # 'scheduler': {
        #     '__factory__': 'dask.distributed.Client',
        #     'address': '127.0.0.1:8786',
        # },
        'scheduler': 'synchronous',
        'cache_cv': False,
    },
}
