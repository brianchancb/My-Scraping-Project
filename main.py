import pandas as pd
from pull_data import pull_data
import numpy as np

if __name__ == '__main__':
    pull_data()
    print(pd.__version__)
    print(np.random.randint(500))
