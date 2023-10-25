class InstantiateCSVError(Exception):

    def __init__(self):
        self.message = f"Файл поврежден"

    def __str__(self):
        return self.message
