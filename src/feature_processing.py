import pandas as pd
import numpy as np
from src import config


def feature_processing(data: pd.DataFrame):
    df = pd.read_csv(data)
    print(df.head())


feature_processing(config.DATASET)
