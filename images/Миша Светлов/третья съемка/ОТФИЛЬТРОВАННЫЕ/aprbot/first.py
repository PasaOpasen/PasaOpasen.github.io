

from collections import defaultdict

import spacy
from spacy.matcher import Matcher



text = input()

counts = defaultdict(int)


nlp = spacy.load("en_core_web_sm")
doc = nlp(text)



matcher = Matcher(nlp.vocab)

pattern = [{"IS_DIGIT": True}]
matcher.add("task1", [pattern])

matches = matcher(doc)


for match_id, start, end in matches:
    
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    
    span = doc[start:end]  # The matched span

    counts[span.text] += 1
    
    


def extract_proper_nouns(doc):
    
    pos = [tok.i for tok in doc if tok.pos_ == "PROPN"]
    consecutives = []
    current = []
    
    for elt in pos:
        if len(current) == 0:
            current.append(elt)
        else:
            if current[-1] == elt - 1:
                current.append(elt)
            else:
                consecutives.append(current)
                current = [elt]
    if len(current) != 0:
        consecutives.append(current)
    
    return [doc[consecutive[0]:consecutive[-1]+1] for consecutive in consecutives]


for noun in extract_proper_nouns(doc):
    
    counts[noun.text] += 1




with open('Paskofirst.html', 'w') as f:
    print('<table>', file = f)
    for sublist in counts.items():
        print ('  <tr><td>', file = f)
        print ('    </td><td>'.join(map(str, sublist)), file = f)
        print ('  </td></tr>', file = f)
    print ('</table>', file = f)


