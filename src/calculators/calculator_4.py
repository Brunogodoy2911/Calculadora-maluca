from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List

from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
       body = request.json
       input_data = self.__validate_body(body)
       
       median = self.__calculate_median(input_data)
       total_sum = sum(input_data)
       
       self.__verify_results(median, total_sum)
       
       mean = self.__calculate_average(input_data)
       
       formated_response = self.__format_response(mean)
       return formated_response
    
    def __validate_body(self, body: Dict) -> List[float]:
       if not body or "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado!")
        
       input_data = body["numbers"]
        
       if not isinstance(input_data, list):
            raise HttpUnprocessableEntityError("O campo 'numbers' deve ser uma lista.")
            
       return input_data
    
    def __calculate_median(self, numbers: List[float]) -> float:
        median = self.__driver_handler.median(numbers)
        return median
    
    def __calculate_average(self, numbers: List[float]) -> float:
        average = self.__driver_handler.average(numbers)
        return average
    
    def __verify_results(self, median:float, soma:float) -> None:
        if median < soma:
            raise HttpBadRequestError("Falha no processo: Mediana é menor que a Soma dos elementos.")
    
    def __format_response(self, median: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": median,
                "Success": True
            }
        }