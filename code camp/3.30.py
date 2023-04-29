import string

# open the file and read the contents
with open('Hamlet.txt', 'r') as f:
  contents = f.read()

# split the contents into words
words = contents.split()

# list of archaic words
archaic_words = []

# list of obsolete words
obsolete_words = []

# define a set of archaic word endings
archaic_endings = {'-eth', '-est', '-st'}

# loop through each word in the text
for word in words:
  # remove punctuation from the word
  word = word.translate(str.maketrans('', '', string.punctuation))

  # check if the word ends with an archaic ending
  if any(word.endswith(ending) for ending in archaic_endings):
    archaic_words.append(word)
  elif word.lower() in ['thou', 'thee', 'thy', 'thine']:
    archaic_words.append(word)
  elif word.lower() in ['mayst', 'art', 'wert', 'hath', 'doth']:
    archaic_words.append(word)

# print the archaic words
print("Archaic words:")
print(archaic_words)

# print the obsolete words
print("Obsolete words:")
print(obsolete_words)

