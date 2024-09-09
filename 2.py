class Integer:
    def __init__(self, value: int):
        self.value = value

    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value))

    def from_roman(cls, value: str):
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        int_value = 0
        prev_value = 0
        for char in reversed(value):
            current = roman_to_int[char]
            if current >= prev_value:
                int_value += current
            else:
                int_value -= current
            prev_value = current
        return cls(int_value)


    def from_string(cls, value):
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value

    def __repr__(self):
        return str(self.value)
