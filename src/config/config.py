class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        self.SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"
        self.NOTIFICATION_SERVICE_URL = "http://fake-notification-service"
