class Project:

    def __init__(self, id=None, x=None):
        self.x = x
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.x == other.x