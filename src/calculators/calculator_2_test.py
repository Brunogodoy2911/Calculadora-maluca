from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self,body: Dict) -> None:
        self.json = body
        
class MockDriverHandler:
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

def test_calculate():
    mock_request = MockRequest({ "numbers": [1.12, 2.24, 3.26]})
    
    driver = MockDriverHandler()
    calc_2 = Calculator2(driver)
    formated_response = calc_2.calculate(mock_request)
    
    assert isinstance(formated_response, dict)
    assert formated_response == { "data": { "Calculator": 2, "result": 0.33 } }

# Teste de Integração    
def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [1.12, 2.24, 3.26]})
    
    driver = NumpyHandler()
    calc_2 = Calculator2(driver)
    formated_response = calc_2.calculate(mock_request)
    
    assert isinstance(formated_response, dict)
    assert formated_response == { "data": { "Calculator": 2, "result": 0.13 } }