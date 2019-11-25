from Models.Disease import Disease
import json


class DiseasesRepository:
    def contains(self, name: str) -> bool:
        diseases = json.load(open("diseases.json", "r"))
        for disease in diseases:
            if disease["name"] == name:
                return True
        return False

    def add(self, disease: Disease)-> bool:
        if self.contains(disease.name):
            return False
        diseaseFile = open("diseases.json", "r")
        diseaseload = json.load(diseaseFile)
        diseaseFile.close()
        diseaseload.append(disease.__dict__)
        diseaseFile = open("diseases.json", "w")
        json.dump(diseaseload, diseaseFile)
        diseaseFile.close()
        return True

    def remove(self, name: str):
        diseaseFile = open("diseases.json", "r")
        diseaseload = json.load(diseaseFile)
        diseaseFile.close()
        for disease in diseaseload:
            if disease["name"] == name:
                diseaseload.remove(disease)
        diseaseFile = open("diseases.json", "w")
        json.dump(diseaseload, diseaseFile)
        diseaseFile.close()

    def get(self, name: str) -> Disease:
        diseases = json.load(open("diseases.json", "r"))
        for disease in diseases:
            if disease["name"] == name:
                return disease
        return None
            

