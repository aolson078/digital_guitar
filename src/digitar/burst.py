from typing import Protocol
import numpy as np
import temporal

class BurstGenerator(Protocol):
    def __call__(self, num_samples: int, sampling_rate: temporal.Hertz) -> np.ndarray:
        ...

class WhiteNoise:
    def __call__(self, num_samples: int, sampling_rate: temporal.Hertz) -> np.ndarray:
        return np.random.uniform(-1.0, 1.0, num_samples)
