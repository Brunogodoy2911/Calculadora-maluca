from abc import ABC, abstractmethod

class NotificationSender(ABC):
    
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

# Definir a regra de construção
class EmailNotificationSender(NotificationSender):
    
    def send_notification(self, message: str) -> None:
        print(f"Email message - {message}")

# Definir a regra de construção        
class SMSNotificationSender(NotificationSender):
    
    def send_notification(self, message: str) -> None:
        print(f"SMS message - {message}")
        
class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender
    
    def send(self, message: str) -> None:
        #Validação de dados
        self.__notification_sender.send_notification(message)
    
obj = Notificator(SMSNotificationSender())
obj.send("Hello World")