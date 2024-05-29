print(117 + 996)
print(199 - 981)

print(3 + 4)
print(3 + 4)

temperature = list(range(10, 20, 2))
print(temperature)

rainfall = list(range(10, 20, 2))
print(rainfall)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
counted_grades = len(student_grades)
print(counted_grades)

print(student_grades.count(10))

# Like the previous exercise, find the proper function or method that converts the string in username into
# lowercase letters and prints out the output.
username = "Alice"
print(username.lower())

temperature = {"morning": 10.0, "afternoon": 15.0, "evening": 20.0}
print(temperature)
temperature["morning"] = 12.0
print(temperature)

print(temperature.keys())
print(temperature.values())

print(temperature.items())

print(temperature["morning"])

print(temperature.get("morning"))

print(temperature.get("night"))


# The code below should print out the value of the key, "morning".

print(temperature["morning"])