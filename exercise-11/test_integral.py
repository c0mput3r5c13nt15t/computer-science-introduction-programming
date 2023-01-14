import math
import pytest
from integral import differentiate, integrate


def test_differentiate():
    # Test the derivative of x^n at different points for n = 1, 2, 3
    for exp in range(1, 100):
        print(f"Testing derivative of x^{exp}")
        for x in range(-100, 100):
            print(f"Testing at x = {x}")
            print(f"Expected: {exp * x ** (exp - 1)}")
            print(f"Actual: {differentiate(lambda x: x ** exp, 1e-2)(x)}")
            assert differentiate(
                lambda x: x ** exp, 1e-6)(x) == pytest.approx((lambda x: exp * x ** (exp - 1))(x), rel=1e-3)

    # Test the derivative of e^x at different points
    print(f"Testing derivative of e^x")
    for x in range(-100, 100):
        print(f"Testing at x = {x}")
        print(f"Expected: {math.exp(x)}")
        print(f"Actual: {differentiate(lambda x: math.exp(x), 1e-2)(x)}")
        assert differentiate(
            lambda x: math.exp(x), 1e-6)(x) == pytest.approx((lambda x: math.exp(x))(x), rel=1e-3)

    # Test the derivative of sin(x) at different points
    print(f"Testing derivative of sin(x)")
    for x in range(-100, 100):
        print(f"Testing at x = {x}")
        print(f"Expected: {math.cos(x)}")
        print(f"Actual: {differentiate(lambda x: math.sin(x), 1e-2)(x)}")
        assert differentiate(
            lambda x: math.sin(x), 1e-6)(x) == pytest.approx((lambda x: math.cos(x))(x), rel=1e-3)


def test_integral():
    # Test the integral of x^n from 0 to 1 for n = 1, 2, 3
    for exp in range(1, 100):
        print(f"Testing integral of x^{exp}")
        for x in range(-100, 100):
            print(f"Testing at x = {x}")
            print(f"Expected: {x ** (exp + 1) / (exp + 1)}")
            print(f"Actual: {integrate(lambda x: x ** exp, 40)(0, x)}")
            assert integrate(
                lambda x: x ** exp, 50)(0, x) == pytest.approx((lambda x: x ** (exp + 1) / (exp + 1))(x), rel=1e-2)

    # Test the integral of e^x from 0 to 1
    for x in range(-100, 100):
        print(f"Testing integral of e^x")
        print(f"Testing at x = {x}")
        print(f"Expected: {math.exp(x) - 1}")
        print(f"Actual: {integrate(lambda x: math.exp(x), 40)(0, x)}")
        assert integrate(
            lambda x: math.exp(x), 50)(0, x) == pytest.approx((lambda x: math.exp(x) - 1)(x), rel=1e-2)

    # Test the integral of sin(x) from 0 to 1
    for x in range(-10, 10):
        print(f"Testing integral of sin(x)")
        print(f"Testing at x = {x}")
        print(f"Expected: { - math.cos(x) + 1}")
        print(f"Actual: {integrate(lambda x: math.sin(x), 40)(0, x)}")
        assert integrate(
            lambda x: math.sin(x), 50)(0, x) == pytest.approx((lambda x: - math.cos(x) + 1)(x), rel=1e-2)
