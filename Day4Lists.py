#                       0           1           2
states_of_america = ["Delaware", "Dallas", "New Jersey"]

print(states_of_america[0])

print(states_of_america[-1]) # last item in the list

# Mutate the item
states_of_america[0] = "Pennsylvania"

print(states_of_america[0])

states_of_america.append("Anas State")

print(states_of_america[-1])

states_of_america.extend(["State 1", "State 2"])

print(states_of_america)