from Models.BloodElement import BloodElement
import json


class BloodElementsRepository:

    def contains(self, name: str):

        elements = json.load(open("elements.json", "r"))
        for element in elements:
            if element["name"] == name:
                return True
            """elif element["unit"] == unit:
                return True
            elif element["max_value"] == max_value:
                return True
            elif element["min_value"] == min_value:
                return True"""
        return False

    def add(self, element):

        if self.contains(element.name):
            return False

        elements_file = open("elements.json", "r")
        elements = json.load(elements_file)
        elements_file.close()
        elements.append(element.__dict__)
        elements_file = open("elements.json", "w")
        json.dump(elements, elements_file)
        elements_file.close()
        return True

    def get(self, name : str) -> BloodElement:
        raise NotImplementedError

    def delete(self, name: str):
        raise NotImplementedError


newElement = BloodElement("name", "unit", 0, 0)
newElement.name = "krwinka"
newElement.unit = "mg/l"
newElement.max_value = 3

repository = BloodElementsRepository()

repository.add(newElement)
print(repository.contains("krwinka"))