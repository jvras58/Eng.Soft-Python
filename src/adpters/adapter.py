class FakeNotificationService:
    def notify(self, msg: str):
        print(f"Notificação enviada: {msg}")
        return True

class NotificationServiceAdapter:
    def __init__(self, service):
        self.service = service

    def send_notification(self, message: str):
        return self.service.notify(message)
