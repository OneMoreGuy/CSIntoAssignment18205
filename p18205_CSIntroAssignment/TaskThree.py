import re, numpy

# Open txt file and save contents in string array contents[]
with open("two_cities_ascii.txt", 'r') as f:
    contents = f.readlines()

entire_text = []
# Read each line and remove all instances of any non-space or non-latin characters.
i = 0
for line in contents:
    pattern = re.compile("[^A-Za-z\s]")
    result = re.sub(pattern, "", contents[i])
    pattern2 = re.compile("[ ]{2,}")
    result2 = re.sub(pattern2, " ", result)
    contents[i] = result2.strip()
    entire_text.append(contents[i])
    i += 1

# Remove all '' elements in list and join them into one string, then split on every word for ease of use.
entire_text = [i for i in entire_text if i]
entire_text = ' '.join(entire_text)
entire_arr = entire_text.split(' ')
final_arr = []
word_count = numpy.array([0])
last = False
i = 0
# Get pairs of two words each (1/2, 3/4, etc) and ignore them if the cumulative letter count is 20.
for word in entire_arr:
    # Guard clause.
    if i >= len(entire_arr) - 1:
        break
    toCount = ''.join([entire_arr[i], entire_arr[i + 1]])
    # If length of the combination is not 20:
    if len(toCount) != 20:
        # Check if the length of any of the pair's words is bigger than the elements of the word_count array that
        # stores the no of times a n-letter word appears.
        if ((len(entire_arr[i]) > len(word_count)) or (len(entire_arr[i + 1]) > len(word_count))):
            # If yes, resize based on the longer word.
            maxnum = max(len(entire_arr[i]), len(entire_arr[i + 1]))
            word_count.resize(1, maxnum)
            word_count = word_count.flatten('F')
        # Add 1 to the i-1th position of the word_count array.
        word_count[len(entire_arr[i]) - 1] += 1
        word_count[len(entire_arr[i + 1]) - 1] += 1
        # Append the words to an array.
        final_arr.append(entire_arr[i])
        final_arr.append(entire_arr[i + 1])
    i += 2

# Add the resulting text after all 20-long letter combos are gone and the word count into text files.
final_text = ' '.join(final_arr)
stats = ' '.join(str(word_count))

f2 = open("result.txt", "w")
f2.write(final_text)
f2.close()

f3 = open("stats.txt", "w")
f3.write(stats)
f3.close()
