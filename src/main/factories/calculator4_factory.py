from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_4 import Calculator4

def calculator4_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator4(numpy_handler)
    return calc