from src.adpters.adapter import FakeNotificationService, NotificationServiceAdapter

class NotificationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
            cls._instance.adapter = NotificationServiceAdapter(FakeNotificationService())
        return cls._instance

    def notify(self, message: str):
        self.adapter.send_notification(message)
