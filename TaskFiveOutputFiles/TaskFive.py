import re
from collections import Counter

# Open txt file and save contents in string array contents[]
with open("../two_cities_ascii.txt", 'r') as f:
    contents = f.readlines()

entire_text = []
# Read each line and remove all instances of any non-space or non-latin characters.
i = 0
for line in contents:
    pattern = re.compile("[^A-Za-z\s]")
    result = re.sub(pattern, "", contents[i])
    pattern2 = re.compile("[ ]{2,}")
    result2 = re.sub(pattern2, " ", result)
    contents[i] = result2.strip().lower()
    entire_text.append(contents[i])
    i += 1

# Remove all '' elements in list and join them into one string, then split on every word for ease of use.
entire_text = [i for i in entire_text if i]
entire_text = ' '.join(entire_text)
entire_arr = entire_text.split(' ')

# Returns the 10 most commonly used words. In case of equal no. of words, the word that occurs first is ranked higher.
counter_results = Counter(entire_arr).most_common(10)

# Copy the initial array into two new ones (must be done as simple '=' would just be a pointer to entire_arr)
entire_twos = entire_arr.copy()
entire_threes = entire_arr.copy()

# Remove all unsuited elements with list comprehension
entire_twos[:] = [x for x in entire_twos if len(x) > 1]
entire_threes[:] = [x for x in entire_threes if len(x) > 2]

# Get the first 2 and 3 letters of every word in the text when applicable.
for i in range(len(entire_twos)):
    entire_twos[i] = entire_twos[i][0:2]

for i in range(len(entire_threes)):
    entire_threes[i] = entire_threes[i][0:3]

# Similar to counter_results.
counter_twos = Counter(entire_twos).most_common(3)
counter_threes = Counter(entire_threes).most_common(3)

print("10 most common words: ")
print(counter_results)
print("3 most common initial 2-letter combos: ")
print(counter_twos)
print("3 most common initial 3-letter combos: ")
print(counter_threes)