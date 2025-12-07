from typing import Dict, List

from pytest import raises
from src.calculators.calculator_4 import Calculator4

class MockRequest:
    def __init__(self,body: Dict) -> None:
        self.json = body
        
class MockDriverHandlerError:
    def median(self, numbers: List[float]) -> float:
        return 3
    
    def average(self, numbers: List[float]) -> float:
        return 0
    
class MockDriverHandler:
    def median(self, numbers: List[float]) -> float:
        return 100000
    
    def average(self, numbers: List[float]) -> float:
        return 3
    
def test_calculate_with_median_error():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4(MockDriverHandlerError())
    
    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "Falha no processo: Mediana é menor que a Soma dos elementos."
    
def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4(MockDriverHandler())
    
    response = calculator_4.calculate(mock_request)
    
    assert response == {
        "data" : {
            "Calculator": 4,
            "value": 3,
            "Success": True
        }
    }
    print()
    print(response)