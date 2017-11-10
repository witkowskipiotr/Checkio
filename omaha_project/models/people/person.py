class Person:
    """
    class of person
    This class not know than it is player or staff
    """

    def __init__(self, *, name: str, surname: str):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname
