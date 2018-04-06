import numpy as np

def vectorizeParams(*args):
    vect = np.array([])
    for matrix in args:
        vect = np.hstack([vect, matrix.ravel()])
    return vect

def constructCompactDictionary(trees):
    # Take a tree lists and union all words
    #  note: have a "*UNK*" to deal with previously unseen words
    dictionary = set()
    dictionary = dictionary.union(['*UNK*'])
    for tree in trees:
        dictionary = dictionary.union(tree.word_yield().split(' '))
    return dictionary

def constructDictionary(*args):
    # Take a list of tree lists and union all words
    dictionary = set()
    for tree_split in args:
        for trees in tree_split:
            for tree in trees:
                dictionary = dictionary.union(tree.word_yield().split(' '))
    return dictionary