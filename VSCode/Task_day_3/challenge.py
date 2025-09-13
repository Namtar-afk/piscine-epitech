### CIBLES ###

words = ["cat","garden","mice"]
patterns = []

for word in words:
    patterns.append(word)
    patterns.append(word[::-1])

### NORMALISATION ###

sentences = [
    "the CataCat attaCk a Cat",
    "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
]
sentences_lowered = []

for s in sentences:
    sentences_lowered.append(s.lower())
  
### STRATEGIE DE COMPTAGE ###

def count_occurrences(text, sub):
    count = 0
    start = 0
    while True:
        pos = text.find(sub, start)
        if pos == -1:
            break
        else:
            count += 1
            start = pos + len(sub)
    return count

### BALAYAGE DES PHRASES ###

count_occurrences(sentences_lowered, patterns)

### SOMME DES PATTERNS ###

total += count_occurrences(phrase, pattern)

### RESULTAT ###

print(count_occurrences)