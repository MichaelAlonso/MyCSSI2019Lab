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

# names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]

# Slice of the entire list from beginning to end, except reversed:# => ["Robb", "Jon", "Sansa", "Arya", "Bran", "Rickon"]

# print(names[::-1])
# # slice of reversed list, starting
# print(names[4:2:-1])
# print(names[::2])

state1 = "New York"
abb1 = "NY"
state2 = "California"
abb2 = "CA"
state3 = "Texas"
abb3 = "TX"
print(abb2, " is short for ", state2)
labeled_states = ["NY: New York", "CA: California", "TX: Texas"]

print(labeled_states[1])
states = ["New York", "California", "Texas"]
abbvs = ["NY", "CA", "TX"]

print(abbvs[1] + " is short for " + states[1])

states = {"NY": "New York", "CA": "California", "TX": "Texas"}

states = {
"NY": "New York",
"CA": "California",
"TX": "Texas"
}

for abbreviation in states:
    print (abbreviation + " is short for " + states[abbreviation])
