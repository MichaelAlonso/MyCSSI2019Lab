# students = ["Alice", "Javi", "Damien", "Javi"]
# students.remove("Javi")
# print(students)
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "Pablo", "NoobMaster69", "Bruce", "Jason", "Tim"]
# for name in smith_siblings:
#     print(name + " Smith")
# print(len(smith_siblings))
# for index in range(len(smith_siblings)):
#     smith_siblings[index]
#
# superheroes = ["Captain Marvel", "Wonder Woman", "Storm", "Kamla Khan", "Bumblebee", "Jessica Jone"]
# demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5"))
# if demoted_hero in superheroes:
#     superheroes.remove(demoted_hero)
#     print("Top 5 heroes:", superheroes)
# else:
#     print("Hero not found.")

names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]

# Slice of the entire list from beginning to end, except reversed:# => ["Robb", "Jon", "Sansa", "Arya", "Bran", "Rickon"]

print(names[::-1])
# slice of reversed list, starting
print(names[4:2:-1])
print(names[::2])
