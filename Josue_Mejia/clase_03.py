## listas o list

to_do = ["buscar un lugar","buscar hotel","comunicar a la familia","viajar"]
print(to_do)

numbers = [1,2,3,4,"cinco"]
print(numbers)

mix = ["uno", 2,3,4, True, [1,2,3]]
print(mix)

print("Primer elemento", mix[0])
print("tercer elemento", mix[3])
print("ultimo elemento", mix[-1])

print(mix[1:5])

mix[-1].append(["a","b"])
print(mix)
