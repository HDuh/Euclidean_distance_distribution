from dataclasses import dataclass, field


@dataclass
class Params:
    _minimum: float = field(repr=True, default=float('inf'))
    _min_pair: tuple = field(repr=True, default=tuple())
    _maximum: float = field(repr=True, default=0.0)
    _max_pair: tuple = field(repr=True, default=tuple())
    _mean: float = field(repr=True, default=0.0)
    distances_map: dict = field(repr=True, default_factory=dict)

    @property
    def minimum(self):
        return self._minimum

    @property
    def maximum(self):
        return self._maximum

    @property
    def mean(self):
        return self._mean

    @property
    def max_pair(self):
        return self._max_pair

    @property
    def min_pair(self):
        return self._min_pair

    @minimum.setter
    def minimum(self, values: tuple):
        new_min, vector_1, vector_2 = values
        if self._minimum > new_min:
            self._minimum = new_min
            self._min_pair = (vector_1, vector_2)

    @maximum.setter
    def maximum(self, values: tuple):
        new_max, vector_1, vector_2 = values
        if self._maximum < new_max:
            self._maximum = new_max
            self._max_pair = (vector_1, vector_2)

    @mean.setter
    def mean(self, values: float):
        self._mean = values

    def update_params(self, distance: float, vector_1, vector_2):
        if distance > self._maximum:
            self.maximum = (distance, vector_1, vector_2)
        elif distance < self._minimum:
            self.minimum = (distance, vector_1, vector_2)
