def longest_word_length(word_list):
    return len(max(word_list, key=len, default=""))

# Example usage:
words = ["apple", "banana", "orange", "grapefruit"]
result = longest_word_length(words)
print("Length of the longest word:", result)