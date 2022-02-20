

def gen_ngram(text, n):
    ngram = []
    tokens = text.split()
    max_tokens = len(tokens)

    # exception: max
    if n >= max_tokens:
        ngram.append(' '.join(tokens))
        return ngram

    for i in range(len(tokens)):
        if (i+n) <= max_tokens:
            ngram.append(' '.join(tokens[i:i+n]))

    return ngram

def gen_ngram_fancy(text, n):
    # zip(a, b) is useful
    # different length of a, b ->

    tokens = text.split()
    #print(*[tokens[i:] for i in range(n)])
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return list(ngrams)


solution = gen_ngram
#solution = gen_ngram_fancy

text = 'this is my test data'
text = """
    Natural-language processing (NLP) is an area of
    computer science and artificial intelligence
    concerned with the interactions between computers
    and human (natural) languages.
"""
text = text.lower()
    
# Replace all none alphanumeric characters with spaces
import re
text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)


print(solution(text, n=5))
raise
print(solution(text, n=2))
print(solution(text, n=3))
print(solution(text, n=4))
print(solution(text, n=5))
print(solution(text, n=6))