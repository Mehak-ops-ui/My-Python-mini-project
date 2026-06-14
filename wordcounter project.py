#WORD COUNTER AND ANALYZER
# Take a paragraph as input count the number of words in paragraphs . find the longest word, count the vowels using string 
# string method and loops
# ------------------------------------------------------------------------------ 
paragraph = input("Enter a paragraph: ")

words = paragraph.split()
words_count = len(words)

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

vowels = "aeiouAEIOU"
vowels_count = 0

for ch in paragraph:
    if ch in vowels:
        vowels_count += 1

print("Total words:", words_count)
print("Longest word:", longest_word)
print("Total vowels:", vowels_count)

    
        



