def celcius_to_fahrenheit(celcius: float) -> float:
    return celcius * 9 / 5 + 32


def fahrenheit_to_celcius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def celcius_to_kelvin(celcius: float) -> float:
    return celcius + 273.15


def kelvin_to_celcius(kelvin: float) -> float:
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return celcius_to_kelvin(fahrenheit_to_celcius(fahrenheit))


def kelvin_to_fahrenheit(kelvin: float) -> float:
    return celcius_to_fahrenheit(kelvin_to_celcius(kelvin))


if __name__ == "__main__":
    source_unit = input('Enter source unit [C / F / K]: ')
    source_value = float(input('Enter source value: '))
    target_unit = input('Enter target unit [C / F / K]: ')

    print()

    result = 0

    if source_unit == 'C' and target_unit == 'F':
        result = celcius_to_fahrenheit(source_value)
    elif source_unit == 'F' and target_unit == 'C':
        result = fahrenheit_to_celcius(source_value)
    elif source_unit == 'C' and target_unit == 'K':
        result = celcius_to_kelvin(source_value)
    elif source_unit == 'K' and target_unit == 'C':
        result = kelvin_to_celcius(source_value)
    elif source_unit == 'F' and target_unit == 'K':
        result = fahrenheit_to_kelvin(source_value)
    elif source_unit == 'K' and target_unit == 'F':
        result = kelvin_to_fahrenheit(source_value)
    else:
        print('Invalid unit')

    print(f'{source_value} {source_unit} corresponds to {result} {target_unit}.')
