from sys import stdin
from re import findall

# Getting the input
raw_data = stdin.read()

# Treating the input
data = ' '.join((raw_data[:-1]).split())

# numbers = [int(i) for i in data.split(' ') if i.isdigit()]
numbers = [i for i in findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", data)]

# Rule 1
if (len(numbers) >= 1):
    for _ in range(data.count("Bien à vous")):
        numbers[0] = str(int(numbers[0]) * 3)

# Rule 2
if (data.count("cherchant") >= 1) and (len(numbers) >= 2):
    numbers[1] = str(int(numbers[1]) * 0)

# Rule 3
if (len(numbers) >= 3):
    for _ in range(data.count("montagnes")):
        numbers[2] = str(int(numbers[2]) + 1)

# Rule 4
if (len(numbers) >= 4):
    for _ in range(data.count("ciel et terre")):
        new_number = ""
        for digit in numbers[3]:
            new_number += str((int(digit) + 1) % 10)
        numbers[3] = new_number

# Rule 5
for _ in range(data.count("roses")):
    numbers.reverse()

# Tango Bravo, going Base 27
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

pieces = []
for num in numbers:
    new_base = numberToBase(int(num), 27)
    pieces.append(new_base)

grid = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

string = ""
for piece in pieces:
    for char in piece:
        string += grid[char]

print(string)
