def celsiusToFahrenheit(celsius: float) -> float:
    return celsius * 9.0 / 5.0 + 32


celsius = float(input('Celsius: '))
print('Fahrenheit: %.2f' % celsiusToFahrenheit(celsius))
