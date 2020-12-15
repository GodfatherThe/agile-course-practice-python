

def get_float_value(celsius):
    if isinstance(celsius, str):
        celsius = celsius.replace(',', '.')
        try:
            result = float(celsius)
        except ValueError:
            raise ValueError("Error: incorrect value")
        return result
    else:
        return float(celsius)


class TemperatureConverter:

    def __init__(self, celsius):
        self.celsius = get_float_value(celsius)

    def convert_to_fahrenheit(self):
        return float((self.celsius * 1.8)) + 32

    def convert_to_kelvin(self):
        return float(self.celsius + 273.15)

    def convert_to_newton(self):
        return float(self.celsius * 0.33)
