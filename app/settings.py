from cryptography.fernet import Fernet
import sys

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
        print(str(sys.argv))
        self.key = Fernet.generate_key()
        try:
            if sys.argv[1] == "dev":
                #TODO enable here the devs settings
                print("environment: dev")
            elif sys.argv[1] == "prod":
                #TODO enable here the prod settings
                print("environment: dev")
            else:
                print("raise some problem that not found the settings, or something like that.")
        except:
            raise Exception("Not possible to define the settings")

            