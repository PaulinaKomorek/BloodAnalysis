from Models.Disease import Disease
from Repositories.DiseasesRepository import DiseasesRepository

repository=DiseasesRepository()
print(repository.contains("anemi"))

#newDisease=Disease()
#newDisease.name = "michal"
#newDisease.description = "michal@email.com"
#newDisease.symptoms = ["1234"]
#newDisease.depends = ["michal@email.com"]
#print("Added new disease: " + str(repository.add(newDisease)))
repository.remove("XDDDDDDDD")
print(repository.getbysymptoms(["lower amount of red cells"]))
print(repository.getbysymptoms(["lower amount of white cells"]))
print(repository.getbysymptoms(["lower amount of white cells", "lower amount of red cells"]))

for disease in repository.getbysymptoms(["lower amount of white cells", "lower amount of red cells"]):
    print(disease)

print(repository.get("anamia"))
print(repository.getbycondition(lambda d: "lower amount of red cells" in d["symptoms"]))
print(repository.getbycondition(lambda d: "lower amount of white cells" in d["symptoms"]))
print(repository.getbycondition(lambda d: "lower amount of pink cells" in d["symptoms"]))