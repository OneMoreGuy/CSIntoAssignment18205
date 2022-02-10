import numpy as np

# Open txt file and save text in string
with open("two_cities_ascii.txt", 'r') as f:
    text = f.read()

bit_values = []
# Get the ASCII value of every character in the text.
for char in text:
    ascii_val = ord(char)
    bit_val = ''
    while ascii_val > 0:
        new_val = ascii_val % 2  # Gets the remainder of ascii_val // 2, aka modulo
        ascii_val = ascii_val // 2  # Gets the div.
        bit_val = str(new_val) + bit_val
    bit_values.append(bit_val)

four_bits = bit_values.copy()
# Pad all elements to be 7 chars long, then get the first and last two bits of each.
for i in range(len(bit_values)):
    bit_values[i] = bit_values[i].rjust(7, '0')
    first_two = ''.join(bit_values[i][0:2])
    last_two = ''.join(bit_values[i][-2:])
    four_bits[i] = first_two + last_two

# Calculate the length of a potential 16-bit array.
x = np.array(len(four_bits)/4, dtype=np.float64)
x = x.astype(np.int64)

div_2_count = 0
div_3_count = 0
div_5_count = 0
div_7_count = 0
sixteen_bits = []
# Check if each number id divisible by 2, 3, 5, and 7
for i in range(x):
    sixteen_bits.append(four_bits[i] + four_bits[i+1] + four_bits[i+2] + four_bits[i+3])
    a = int(sixteen_bits[i], 2)
    if a % 2 == 0: div_2_count += 1
    if a % 3 == 0: div_3_count += 1
    if a % 5 == 0: div_5_count += 1
    if a % 7 == 0: div_7_count += 1

# Find the percentage of resulting numbers are perfectly divided by N.
count = len(sixteen_bits)
perc_2 = (div_2_count/count)*100
perc_3 = (div_3_count/count)*100
perc_5 = (div_5_count/count)*100
perc_7 = (div_7_count/count)*100

print("Percentage of values perfectly divisible by 2:")
print(perc_2)
print("Percentage of values perfectly divisible by 3:")
print(perc_3)
print("Percentage of values perfectly divisible by 5:")
print(perc_5)
print("Percentage of values perfectly divisible by 7:")
print(perc_7)