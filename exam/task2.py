__author__ = 'Independence'


file0 = open("dict.txt", "r")
words = file0.read().split("\n")
# adjectives, nouns and verbs accordingly:
lexicon_count = (0, 0, 0)
lexicon_count = list(lexicon_count)
for word in words:
    if word[len(word)-2:] == "yo":
        lexicon_count[0] += 1
    elif word[len(word)-2:] == "ka":
        lexicon_count[1] += 1
    else:
        lexicon_count[2] += 1


def factorial(x):
    y = 1
    for i in range(x):
        y *= (i+1)*1
    return y

# calculating combinations of adjectives
n = lexicon_count[0]
if n < 7:
    k = n
else:
    k = 7
adjectives_combs = 0
for i in range(k):
    adjectives_combs += factorial(n)/(factorial(n-(i+1)))
# calculating sentences
sentences = adjectives_combs * lexicon_count[1] * lexicon_count[2]
print(int(sentences))
