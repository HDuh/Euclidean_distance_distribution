import argparse
from typing import Any

import numpy as np


def parse_args() -> tuple[int, int]:
    """Parsing args from console"""
    parser = argparse.ArgumentParser()
    parser.add_argument("N", help="number_of_vectors", nargs="+")
    parser.add_argument("M", help="dimension", nargs="+")
    args = parser.parse_args()
    number_of_vectors = args.N[0]
    dimension = args.M[0]

    return int(number_of_vectors), int(dimension)


class VectorsWorker:
    def __init__(self, vectors_number, dimension):
        self._vectors_number: int = self.validate_param(vectors_number)
        self._dimension: int = self.validate_param(dimension)
        self._vectors: Any = None

    @staticmethod
    def validate_param(value: int) -> int:
        if value <= 0:
            raise ValueError('all params must be great 0')
        else:
            return value

    def generate_vectors_array(self) -> None:
        self._vectors = np.random.uniform(-1, 1, size=(self._vectors_number, self._dimension))
        print(f'Successfully generate vectors array. '
              f'Vectors_number - {self._vectors_number}, '
              f'dimension - {self._dimension} ')

    def save_vectors(self, file_name) -> None:
        """Save vectors to 'file_name' """
        np.savetxt(f"{file_name}", self._vectors, delimiter=",")
        print(f'{file_name} successfully saved.')


if __name__ == '__main__':
    N, m = parse_args()
    vectors = VectorsWorker(N, m)
    vectors.generate_vectors_array()
    vectors.save_vectors('vectors.csv')
