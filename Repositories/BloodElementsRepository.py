from Models.BloodElement import BloodElement

class BloodElementsRepository:
    def add(self, element: BloodElement) -> BloodElement:
        raise NotImplementedError

    def get(self, name : str) -> BloodElement:
        raise NotImplementedError

    def delete(self, name: str):
        raise NotImplementedError
