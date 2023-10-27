class InstantiateCSVError(Exception):

    def __init__(self, message = "Файл поврежден"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
