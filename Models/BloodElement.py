class BloodElement:

    def __init__(self, name: str, unit: str, minValue: float, maxValue: float):
        self.name = name
        self.unit = unit
        self.minValue = minValue
        self.maxValue = maxValue

    name: str
    unit: str
    minValue: float
    maxValue: float
