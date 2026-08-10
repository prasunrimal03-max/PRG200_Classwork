def word_frequency(text):
    # remove punctuation
    for ch in ".,!?\"'":
        text = text.replace(ch, "")
 
    words = text.lower().split()
 
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
 
    # sort by count, descending, take top 3
    top_words = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:3]
    return top_words
 
 
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""
 
print()
print("=" * 50)
print("Question 4 - Word Frequency Counter")
print("=" * 50)
top3 = word_frequency(text)
print("Top 3 words:")
for word, count in top3:
    print(f"{word} - {count} times")