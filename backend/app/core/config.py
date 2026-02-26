class Settings:
    def __init__(self):
        self.configurations = {
            'DEBUG': False,
            'DATABASE_URL': 'sqlite:///db.sqlite3',
            'SECRET_KEY': 'your_secret_key_here',
        }

    def get(self, key):
        return self.configurations.get(key)

    def set(self, key, value):
        self.configurations[key] = value
