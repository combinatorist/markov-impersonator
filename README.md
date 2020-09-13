# markov-impersonator

# prequisites
This requires nltk module, which separately downloads data.

It downloaded the following (in the home directory):

```
nltk_data/
├── corpora
│   └── treebank
│       ├── combined
│       ├── parsed
│       ├── raw
│       └── tagged
├── taggers
│   └── averaged_perceptron_tagger
└── tokenizers
    └── punkt
        └── PY3
```

I believe the 3rd level items need to be installed like so:
```
import nltk;
nltk.download(['treebank', 'averaged_perceptron_tagger', 'punkt'])
```

A custom nix experssion could probably do this data download.
Perhaps someone else will include this soon: https://github.com/NixOS/nixpkgs/issues/56094#issuecomment-638247266.

# usage
Start a Nix shell with:
```
nix-shell -p 'python35.withPackages(ps: with ps; [ nltk ])'
```

The run the following inside:
```
python3 __init__.py <your input file path>
```

# todo
- ignore case (at least in analysis)
- consider frequency of suffixes (or rather compress on them)
- consider grammar tree: https://www.nltk.org/
