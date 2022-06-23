import argparse

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


def generate_csv(number_of_vectors: int,
                 dimension: int) -> None:
    """Generating a CSV file"""
    vectors = np.random.uniform(-1, 1, size=(number_of_vectors, dimension))
    np.savetxt("vectors.csv", vectors, delimiter=",")
    print(f'File vectors.csv successfully generated. Number of vectors: {number_of_vectors}, dimension: {dimension}')


if __name__ == '__main__':
    N, m = parse_args()
    generate_csv(N, m)
