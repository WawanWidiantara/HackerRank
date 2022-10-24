import math


def grade(grades):
    for i in range(len(grades)):
        rounded = 5 * math.ceil(grades[i] / 5)
        if grades[i] >= 38:
            if abs((rounded - grades[i])) < 3:
                grades[i] = rounded
    return grades


grades = [73, 67, 38, 33]

print(grade(grades))
