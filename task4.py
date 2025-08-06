import emoji
result = emoji.emojize('Python is :thumbs_up:')
print(result)
result = emoji.demojize('Python is ?')
print(result)

print(emoji.emojize('Python is :thumbs_up:', language='alias'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
print(emoji.is_emoji("👍"))