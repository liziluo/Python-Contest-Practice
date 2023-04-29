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



import re

# Define a dictionary mapping archaic words to modern equivalents
word_dict = {
      "abate": "reduce",
    "abbey": "monastery",
    "abide": "stay",
    "ablutions": "cleaning",
    "abode": "residence",
    "abroad": "overseas",
    "abundance": "plenty",
    "accouterments": "equipment",
    "accursed": "damned",
    "addled": "confused",
    "adieu": "farewell",
    "adjure": "urge",
    "admiral": "commander",
    "admonish": "warn",
    "adorn": "decorate",
    "adversary": "opponent",
    "aery": "nest",
    "affright": "frighten",
    "afresh": "again",
    "afterward": "later",
    "agate": "semiprecious stone",
    "aglet": "shoelace tip",
    "ail": "hurt",
    "airship": "blimp",
    "alack": "alas",
    "alas": "unfortunately",
    "alehouse": "pub",
    "allay": "reduce",
    "alms": "charity",
    "aloft": "above",
    "amain": "quickly",
    "amiss": "wrong",
    "an": "if",
    "anatomy": "structure",
    "angel": "coin",
    "angle": "fish",
    "anon": "soon",
    "ape": "imitate",
    "apothecary": "pharmacist",
    "apparel": "clothing",
    "appertaining": "belonging",
    "apprehend": "understand",
    "approbation": "approval",
    "apt": "suitable",
    "argosy": "large merchant ship",
    "arm-gaunt": "thin",
    "armour": "armor",
    "arrant": "complete",
    "arrogance": "pride",
    "art": "are",
        "anon": "soon",
    "art": "are",
    "belike": "probably",
    "ere": "before",
    "forsooth": "indeed",
    "haply": "perhaps",
    "hark": "listen",
    "hast": "have",
    "hath": "has",
    "henceforth": "from now on",
    "hither": "here",
    "methinks": "I think",
    "nigh": "near",
    "oft": "often",
    "perchance": "perhaps",
    "sith": "since",
    "thence": "from there",
    "thine": "yours",
    "thou": "you",
    "thy": "your",
    "twas": "it was",
    "verily": "truly",
    "whence": "from where",
    "wherefore": "why",
    "whilst": "while",
    "whither": "where",
    "yon": "that",
    "yonder": "over there"
    'hath': 'has',
    'dost': 'do',
    'ere': 'before',
    'thence': 'from there',
    'tis': 'it is',
    'hie': 'hurry',
    'doth': 'does',
    'thither': 'there',
    'whence': 'from where',
    'wherefore': 'why',
    'perforce': 'necessarily',
    'whither': 'where',
    'fain': 'gladly',
    'ne\'er': 'never',
    'th': 'the',
    'aught': 'anything',
    'erst': 'formerly',
    'whilst': 'while',
    'erewhile': 'formerly',
    'mayst': 'may',
    'ope': 'open',
    'thou': 'you',
    'naught': 'nothing',
    'troth': 'truth',
    'yclept': 'called',
    'hark': 'listen',
    'haps': 'happens',
    'hight': 'named',
    'belike': 'probably',
    'egad': 'oh my god',
    'o\'er': 'over',
    'methought': 'I thought',
    'hither': 'here',
    'howbeit': 'however',
    'eftsoons': 'soon after',
    'sirrah': 'sir',
    'howsoever': 'however',
    'therewithal': 'with that',
    'verily': 'truly',
    'yonder': 'there',
    'oho': 'oh',
    'wherewith': 'with which',
    'howsoever': 'however',
    'oft': 'often',
    'henceforward': 'from now on',
    'mayhap': 'perhaps',
    'where\'er': 'wherever'
}

# Read in the contents of the Hamlet.txt file
with open('Hamlet.txt', 'r') as file:
    hamlet_text = file.read()

# Replace archaic words with modern equivalents using regular expressions
for old_word, new_word in word_dict.items():
    hamlet_text = re.sub(r'\b' + old_word + r'\b', new_word, hamlet_text)

# Write the updated text to a new file
with open('Hamlet_updated.txt', 'w') as file:
    file.write(hamlet_text)
    
print('Updated text saved to Hamlet_updated.txt')
