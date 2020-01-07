from Models.BloodElement import BloodElement
import json


class BloodElementsRepository:

    def contains(self, name: str):

        elements = json.load(open("elements.json", "r"))
        for element in elements:
            if element["name"] == name:
                return "Repository already contains " + name
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
        json.dump(elements, elements_file, indent=4)
        elements_file.close()
        return True

    def get(self, name: str) -> BloodElement:
        raise NotImplementedError

    def delete(self, name: str):
        elements_file = open("elements.json", "r")
        elements = json.load(elements_file)
        elements_file.close()
        for element in elements:
            if element["name"] == name:
                elements.remove(element)
        elements_file = open("elements.json", "w")
        json.dump(elements, elements_file)
        elements_file.close()

    def display(self, show=True):
        elements = json.load(open("elements.json", "r"))
        if show:
            for element in elements:
                if len(elements) > 0:
                    for i in range(len(elements)):
                        print(str(i+1) + ": " + element["name"] + " " + element["unit"])
                else:
                    print("Repository contains nothing.")
        """else:
            for element in elements:
                yield element["name"]"""


newElement = BloodElement("Plytki krwi", "tys/mm3", 140, 450)


repository = BloodElementsRepository()

repository.add(newElement)

"""

repository = BloodElementsRepository()

repository.display()"""
