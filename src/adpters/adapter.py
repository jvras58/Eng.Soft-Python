class NotificationServiceAdapter:
    def __init__(self, service):
        self.service = service

    def send_notification(self, message: str):
        return self.service.notify(message)

class FakeNotificationService:
    def notify(self, msg: str):
        print(f"Notificação enviada: {msg}")
        return True

if __name__ == "__main__":
    fake_service = FakeNotificationService()
    adapter = NotificationServiceAdapter(fake_service)
    adapter.send_notification("Tarefa concluída!")
