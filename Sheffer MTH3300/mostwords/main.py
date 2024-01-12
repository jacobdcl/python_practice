# Open the file
book = open('books.txt', 'r')

# Create an empty string to store the contents of the file
contents = ''

# Loop through the lines in the file and add them to the contents string
for line in book:
    contents += line

# Split the contents into individual words
words = contents.split()

# Create an empty dictionary to store the word counts
word_counts = {}

# Loop through each word and update its count in the dictionary
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort the words by count and print the 20 most common words
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:20]:
    print(word, count)


import random

def print_random_word(filename):
    # Open the file
    with open(filename, 'r') as file:
        # Create an empty string to store the contents of the file
        contents = ''

        # Loop through the lines in the file and add them to the contents string
        for line in file:
            contents += line

    # Split the contents into individual words
    words = contents.split()

    # Create a dictionary to store the word frequencies
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    # Compute the total number of words
    total_words = sum(freq.values())
    print(freq.values())
    print(total_words)

    # Choose a random number between 1 and the total number of words
    random_num = random.randint(1, total_words)

    # Iterate through the words in the frequency dictionary and count up to the random number
    count = 0
    for word, word_count in freq.items():
        count += word_count
        if count >= random_num:
            # Once we reach the random number, print the word and exit the loop
            print(f"The randomly chosen word is '{word}'.")
            break

print_random_word('books.txt')
