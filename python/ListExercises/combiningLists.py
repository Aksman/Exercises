# EXERCISE
# A demonstration of different ways to combine lists.

subjectsA = ['Math', 'Biology']
subjectsB = ['Literature', 'Georgraphy']

# Method #1: the '+' operator.

subjectsA1 = subjectsA.copy()
subjectsB1 = subjectsB.copy()

print(f"List A: {subjectsA1}")
print(f"List B: {subjectsB1}")
print(f"Combined with '+': {subjectsA1 + subjectsB1}")
print(f"List A unaltered: {subjectsA1}")
print(f"List B unaltered: {subjectsB1}")

# Method #2: the .extend() method
subjectsA2 = subjectsA.copy()
subjectsB2 = subjectsB.copy()

print(f"List A: {subjectsA2}")
print(f"List B: {subjectsB2}")
subjectsA2.extend(subjectsB2)
print(f"List A now combined with List B: {subjectsA2}")
print(f"List B unaltered: {subjectsB2}")

# Not a good method: .append()
# This results in the list being appended as a single element, like this:
# ['Math', 'Biology', ['Literature', 'Georgraphy']]

subjectsA3 = subjectsA.copy()
subjectsB3 = subjectsB.copy()

print(f"List A: {subjectsA3}")
print(f"List B: {subjectsB3}")
subjectsA3.append(subjectsB3)
print(f"This is not what we intended for List A: {subjectsA3}")
print(f"List B unaltered: {subjectsB3}")

