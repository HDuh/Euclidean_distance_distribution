import math
import os.path

import numpy as np
import pandas as pd
import plotly.express as px
from numpy import loadtxt


class EuclideanDistanceDistribution:
    """
    Calculating the Euclidean distance between all pairs of different vectors
    from file and finding for the minimum and maximum distances and building
    histogram distribution of distances
    """

    def __init__(self):
        self.min: dict = {'value': float('inf'),
                          "pair": tuple()}
        self.max: dict = {'value': 0.0,
                          "pair": tuple()}
        self.mean: None | float = None
        self.distances_map: dict = {}

    def _check_params(self, distance_value, vector_1_num, vector_2_num) -> None:
        """Comparing values and finding: max, min."""
        if distance_value > self.max['value']:
            self.max['value']: float = distance_value
            self.max['pair'] = (vector_1_num, vector_2_num)
        elif distance_value < self.min['value']:
            self.min['value']: float = distance_value
            self.min['pair'] = (vector_1_num, vector_2_num)

    def distance_distribution(self, data_array: np.array) -> None:
        """Calculating the distribution and mean"""
        num_rows, num_cols = data_array.shape
        summa = 0  # accumulate summa for mean calculating
        for vector_i in range(num_rows - 1):
            for vector_j in range(vector_i + 1, num_rows):
                # find current distance
                distance = math.dist(data_array[vector_i], data_array[vector_j])
                summa += distance
                self._check_params(distance, vector_i, vector_j)

                # interval for histogram building
                interval = round(distance, 1)
                if interval not in self.distances_map:
                    self.distances_map[interval] = 1
                else:
                    self.distances_map[interval] += 1
        self.mean = summa / (num_rows * (num_rows - 1) / 2)

    def histogram_build(self, file_name: str):
        """Building histogram distribution of distances"""
        with open(file_name, 'rb') as file:
            data = loadtxt(file, delimiter=",")

        self.distance_distribution(data)
        df = pd.DataFrame(self.distances_map.items(), columns=['Distance', 'Frequency'])

        # params for histogram
        max_value = round(self.max['value'], 3)
        max_distance_pair = self.max['pair']
        min_value = round(self.min['value'], 3)
        min_distance_pair = self.min['pair']
        mean_value = round(self.mean, 3)

        fig = px.bar(df, x='Distance', y='Frequency',
                     color="Distance",
                     color_continuous_midpoint=mean_value, )
        fig.update_layout(
            title={
                'text': f"Max: pair {max_distance_pair}, value = {max_value}| "
                        f"Min: pair {min_distance_pair}, value = {min_value} ",
                'y': 0.98,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})

        fig.show()


if __name__ == '__main__':
    file_path = 'vectors.csv'
    if not os.path.exists(file_path):
        raise FileNotFoundError('Please generate file vectors.csv')

    euclidean_instance = EuclideanDistanceDistribution()
    print('Building histogram in progress..')
    euclidean_instance.histogram_build('vectors.csv')
