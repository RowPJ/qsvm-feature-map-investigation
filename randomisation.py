import numpy as np

def randomize_labels(fraction, labels, seed=22):
    """Randomly picks a fraction of the labels (amount determined by
    fraction argument) without replacement, then shuffles their positions
    in the array."""
    # copy the array to prevent destructive modification
    labels = np.copy(labels)

    # create rng instance for deterministic randomness
    rng = np.random.default_rng(seed)

    #calculate number of indices to shuffle
    size = len(labels)
    number_to_shuffle = int(np.floor(size * fraction))

    # special cases: no shuffling and total shuffling
    if number_to_shuffle == 0:
        return labels
    if number_to_shuffle == size:
        rng.shuffle(labels)

    # pick the required number of indices without replacement
    indices = np.array(range(size))
    indices_to_shuffle = rng.choice(indices, number_to_shuffle, replace=False)  # ensure no replacement

    # shuffle a copy of the chosen indices
    shuffled = np.copy(indices_to_shuffle)
    rng.shuffle(shuffled)

    # swap the values at the original indices with the values at the shuffled indices
    for (old, new) in zip(indices_to_shuffle, shuffled):
        labels[old], labels[new] = labels[new], labels[old]

    return labels
