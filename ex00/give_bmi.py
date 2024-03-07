def give_bmi(height: list, weight: list) -> list:
    """dame el ancho partido de la altura al cuadrado de tu puta madre"""
    try:
        assert type(height) is list, "height is not a list"
        assert type(weight) is list, "weight is not a list"
        assert len(height) == len(weight), "h and w must have the same length"
        bmi_values = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)):
                raise TypeError("Height must be integers or floats")
            if not isinstance(w, (int, float)):
                raise TypeError("Weight must be integers or floats")
            if h <= 0:
                raise ValueError("Height must be a positive number")
            if w <= 0:
                raise ValueError("Weight must be a positive number")
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except AssertionError as ae:
        print(f"{type(ae).__name__}: {ae}")
    except TypeError as te:
        print(f"{type(te).__name__}: {te}")
    except ValueError as ve:
        print(f"{type(ve).__name__}: {ve}")


def apply_limit(bmi: list, limit: int) -> list[bool]:
    """limita a tu puta madre"""
    try:
        above_limit = []
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("BMI values must be integers or floats")
            above_limit.append(value > limit)
        return above_limit
    except TypeError as e:
        print(f"An error occurred: {e}")
        return []
    except Exception:
        print('Errorsito')
