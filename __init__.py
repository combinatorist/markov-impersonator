import re
from collections import namedtuple
from collections import defaultdict
from random import choice
from sys import argv


def compress(text):
    return re.findall(r"[\w]+|[^\s\w]", text)


tokens = defaultdict(int)
tokens['frog'] = 1
tokens



def tokenize(text):
    return re.findall(r"[\w]+|[^\s\w]", text)


def compress(tokenized):
    tokens = set(tokenized)
    index2token = {i: t for i, t in enumerate(sorted(tokens))}
    token2index = {t: i for i, t in index2token.items()}
    compressed = [token2index[token] for token in tokenized]
    return CompressedText(index2token, compressed)


CompressedText = namedtuple('CompressedText', ['index2token', 'compressed_text'])
text = 'Hello, this is a string!'
compress(tokenize(text))


def sliding(collection, n):
    return (tuple(collection[i: i + n]) for i in range(len(collection) - n + 1))


test5 = range(5)
tuple(sliding(test5, 1))
tuple(sliding(test5, 2))
tuple(sliding(test5, 3))
tuple(sliding(test5, 4))
tuple(sliding(test5, 5))
tuple(sliding(test5, 6))
tuple(sliding(test5, 7))


def find_chains(compressed, prefix_length):
    prefix2options = defaultdict(list)
    for phrase in sliding(compressed, prefix_length + 1):
        prefix2options[phrase[:-1]].append(phrase[-1])
    return prefix2options

compressed = compress(tokenize(text))
find_chains(compressed, 2)
compressed
tuple(sliding(compressed, 2))
find_chains(compressed.compressed_text, 2)



def analyze(compressed):
    saturated = False
    chains_by_length = {}
    n = 1
    while not saturated and n < len(compressed):
        n_chains = find_chains(compressed, n)
        chains_by_length[n] = n_chains
        saturated = max(len(opts) for k, opts in n_chains.items()) == 1
        n += 1
    return chains_by_length


analyze(compressed.compressed_text)
analyze([1, 2, 1, 3, 1, 2, 4])


def next(analysis, said=[]):
    if not said:
        random_prefix_length_dict = choice(tuple(analysis.values()))
        said = choice(tuple(random_prefix_length_dict.keys()))
    while True:
        n = len(said)
        options = []
        while n > 1 and len(options) <= 1:
            if n in analysis:
                options = analysis[n][said[-n:]]
            n -= 1
        token = choice(options)
        yield token
        said += (token,)
        
        
def main(text_file_path, word_count=500):
    with open(text_file_path, 'r') as f:
        text = f.read()
    compressed_text = compress(tokenize(text))
    analyzed_text = analyze(compressed_text.compressed_text)
    conversation = next(analyzed_text)
    text = ' '.join(compressed_text.index2token[conversation.__next__()] for x in range(word_count))
    print(text)


if __name__ == '__main__':
    main(*argv[1:])
