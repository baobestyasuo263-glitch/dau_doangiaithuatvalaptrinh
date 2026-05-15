class Solution(object):

    def convertTemperature(self, celsius):

        # Kelvin
        kelvin = celsius + 273.15

        # Fahrenheit
        fahrenheit = celsius * 1.80 + 32.00

        return [kelvin, fahrenheit]
        