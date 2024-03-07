import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """troceame esta"""
    try:
        assert len(np.array(family).shape) == 2, "not a bidimensional matrix"
        print(f"My shape is : {np.array(family).shape}")
        family = family[start:end]
        print(f"My new shape is : {np.array(family).shape}")
        return family

    except AssertionError as ae:
        print(f"{type(ae).__name__}: {ae}")
