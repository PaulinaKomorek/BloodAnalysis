class Disease:
    name: str
    description: str
    symptoms: list
    depends: list

    def __str__(self):
        return self.name + " " + self.description
