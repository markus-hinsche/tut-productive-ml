from glob import glob
import os

import dask.dataframe as dd
from distributed import Client
import numpy as np
from palladium.util import timer
import pandas
from tqdm import tqdm


def create_csvs(n_csvs, n_rows, n_cols):
    for i in tqdm(range(n_csvs)):
        data = np.random.random((n_rows, n_cols))
        df = pandas.DataFrame(data)
        fname = 'data_{}.csv'.format(i)
        df.to_csv(fname, index=False)
    df.info()


def compute_mean_pandas():
    total = 0
    total_len = 0
    for fname in glob('data_*.csv'):
        df = pandas.read_csv(fname)
        total += df.sum()
        total_len += len(df)
    return total / total_len


def compute_mean_dask():
    df = dd.read_csv('data_*.csv')
    return df.mean().compute()


def main():
    # Client('127.0.0.1:8786')  # use distributed scheduler

    if not os.path.exists('data_0.csv'):
        with timer(print, "create_csvs"):
            create_csvs(10, int(1e6), 4)

    with timer(print, "compute_mean_pandas"):
        print(compute_mean_pandas())

    with timer(print, "compute_mean_dask"):
        print(compute_mean_dask())


if __name__ == '__main__':
    main()
