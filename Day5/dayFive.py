from string import ascii_lowercase

with open("input.txt") as file:
    inputs = [list(line.rstrip()) for line in file]

with open("input.txt") as file:
    inputString = file.read()

inputs = inputs[0]


def partOne(inputs):
    i = 0
    while i < len(inputs) - 1:
        j = i + 1
        if inputs[i] != inputs[j] and inputs[i].upper() == inputs[j].upper():
            inputs = inputs[:i] + inputs[i+2:]
            i = max(0, i-1)
        else:
            i += 1

    return len(inputs)

def partTwo(inputs):
    minLen = len(inputs)
    for letter in ascii_lowercase:
        x = inputs.replace(letter, "").replace(letter.upper(), "")
        minLen = min(minLen, partOne(x))

    return minLen


print("Part One:", partOne(inputString))
print("Part Two:", partTwo(inputString))
