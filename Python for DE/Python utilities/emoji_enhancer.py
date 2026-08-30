# """
#  Challenge: Emoji Enhancer for Messages

# Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

# Your program should:
# 1. Ask the user to input a message.
# 2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
# 3. Print the updated message with emojis.




# Example:
# Input:
#   I love to code and drink tea when I'm happy.

# Output:
#   I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

# Bonus:
# - Make it case-insensitive (match "Happy" or "happy")
# - Handle punctuation (like commas or periods right after keywords)

# """

#get a dictionary
emoji_map_fun = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

# get user message
message = input("Enter your message: ")

updated_words = []

# process each word

for word in message.split():
  clean_word = word.lower().strip(".,!?")
  
  emoji = emoji_map_fun.get(clean_word, "")
  
  if emoji:
    updated_words.append(f"{word} {emoji}")
  else:
    updated_words.append(word)
    

ans = " ".join(updated_words)

print(ans)


