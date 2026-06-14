passage = input("Enter the passage : ")
words = passage.split()
word_frequency = {"Cat":5,
                  "food":3,
                  "pet":2,
                  "plays":4  }
for word in words:
    word_frequency[word] = word_frequency.get(word,0)+1
    sorted_words = sorted(word_frequency,
                      key=word_frequency.get,
                      reverse=True)

print("Top 5 Frequent Words:")

for word in sorted_words[:5]:
    print(word, "=", word_frequency[word])

