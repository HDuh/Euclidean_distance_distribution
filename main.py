import math
import os.path

import numpy as np
import pandas as pd
import plotly.express as px
from numpy import loadtxt

from param import Params


class EuclideanProcessor:
    def __init__(self):
        self.params = Params()

    def add_value_to_distance_map(self, value):
        interval = round(value, 1)
        if interval not in self.params.distances_map:
            self.params.distances_map[interval] = 1
        else:
            self.params.distances_map[interval] += 1

    def distance_distribution(self, data_array: np.array) -> None:
        """Calculating the distribution and mean"""
        num_rows, num_cols = data_array.shape
        summa = 0  # accumulate summa for mean calculating
        for vector_i in range(num_rows - 1):
            for vector_j in range(vector_i + 1, num_rows):
                # find current distance
                distance = math.dist(data_array[vector_i], data_array[vector_j])
                self.params.update_params(distance, vector_i, vector_j)
                summa += distance

                # interval for histogram building
                self.add_value_to_distance_map(distance)
        self.params.mean = summa / (num_rows * (num_rows - 1) / 2)

    def histogram_build(self, file_name: str):
        """Building histogram distribution of distances"""
        with open(file_name, 'rb') as file:
            data = loadtxt(file, delimiter=",")

        self.distance_distribution(data)
        df = pd.DataFrame(self.params.distances_map.items(), columns=['Distance', 'Frequency'])
        fig = px.bar(df, x='Distance', y='Frequency',
                     color="Distance",
                     color_continuous_midpoint=self.params.mean, )
        fig.update_layout(
            title={
                'text': f"Max: pair {self.params.max_pair}, value = {self.params.maximum}| "
                        f"Min: pair {self.params.min_pair}, value = {self.params.minimum} ",
                'y': 0.98,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})

        fig.show()


if __name__ == '__main__':
    file_path = 'vectors.csv'
    if not os.path.exists(file_path):
        raise FileNotFoundError('Please generate file vectors.csv')

    euclidean_instance = EuclideanProcessor()
    print('Building histogram in progress..')
    euclidean_instance.histogram_build('vectors.csv')
