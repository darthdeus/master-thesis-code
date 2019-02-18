import abc
import os
import numpy as np

from typing import List, Tuple
from bopt.basic_types import Hyperparameter
from bopt.runner.abstract import Job


class Model(abc.ABC):
    @abc.abstractmethod
    def predict_next(self, samples: "SampleCollection") -> Tuple[dict, "Model"]:
        pass

    @abc.abstractmethod
    def to_serializable(self) -> "Model":
        pass

    @abc.abstractmethod
    def from_serializable(self) -> "Model":
        pass


class Sample:
    param_values: dict
    job: Job
    model: Model

    def __init__(self, param_values: dict, job: Job, fitted_model: Model) -> None:
        self.param_values = param_values
        self.job = job
        self.model = fitted_model

    def to_xy(self, output_dir: str) -> Tuple[np.ndarray, float]:
        x = np.zeros(len(self.param_values), dtype=np.float64)

        for i, key in enumerate(sorted(self.param_values)):
            value = self.param_values[key]

            x[i] = value

        y = self.job.get_result(output_dir)

        assert isinstance(x, np.ndarray)
        assert isinstance(y, float)

        return x, y

    def get_result(self, meta_dir: str) -> float:
        import os
        # TODO: fuj
        output_dir = os.path.join(meta_dir, "output")
        return self.job.get_result(output_dir)

    def to_serializable(self) -> "Sample":
        return Sample(self.param_values, self.job, self.model.to_serializable())

    def from_serializable(self) -> "Sample":
        return Sample(self.param_values, self.job, self.model.from_serializable())


class SampleCollection:
    samples: List[Sample]
    meta_dir: str

    def __init__(self, samples: List[Sample], meta_dir: str) -> None:
        self.samples = samples
        self.meta_dir = meta_dir

    def to_xy(self) -> Tuple[np.ndarray, np.ndarray]:
        assert all([s.job.is_finished() for s in self.samples])

        num_samples = len(self.samples)

        y_sample = np.zeros([num_samples], dtype=np.float64)

        xs = []

        # TODO: "output" as a global constant
        output_dir = os.path.join(self.meta_dir, "output")

        for i, sample in enumerate(self.samples):
            x, y = sample.to_xy(output_dir)

            xs.append(x)
            y_sample[i] = y

        X_sample = np.array(xs, dtype=np.float32)

        return X_sample, y_sample