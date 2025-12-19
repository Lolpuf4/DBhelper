class DataBaseError(Exception):
    pass

class DBMSErrors(Exception):
    pass

class NoDatabaseError(DBMSErrors):
    def __init__(self):
        self.message = f"Specify Database in SQL command."
        super().__init__(self.message)

