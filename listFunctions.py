lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Kong", "Jim", "Oscar", "Timmy"]
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("Bobby")
print(friends)

friends.insert(2, "Louis")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kong"))

friends.append("Oscar")
print(friends.count("Oscar"))

friends = ["Kevin", "Kong", "Jim", "Oscar", "Timmy"]
friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

print(friends.clear())

lucky_numbers.reverse()
print(lucky_numbers)

friends = ["Kevin", "Kong", "Jim", "Oscar", "Timmy"]
friends2 = friends.copy()
print(friends2)


