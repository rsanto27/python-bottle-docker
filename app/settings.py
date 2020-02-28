from cryptography.fernet import Fernet

# This is a decorator to give us the control of settings instance.
def settings(cls):
    instances = {}
    def instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return instance

# This is a singleton to give us always the same settings instance, used to generate our env    
@settings
class Settings:
    def __init__(self):
        self.key = Fernet.generate_key()