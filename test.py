import numpy as np

import numpy as np

def percentileofscore_np(a, score, kind='rank'):
    """
    Calculate the percentile rank of a score within a dataset using NumPy.

    Parameters:
    - a (array-like): The dataset.
    - score (float or array-like): The value(s) for which to calculate the percentile rank.
    - kind (str, optional): The method used to calculate the percentile rank. Default is 'rank'.
        - 'rank': Returns the rank as a percentage from 0 to 100.
        - 'rankstrict': Same as 'rank', but returns NaN for scores outside the range.
        - 'rankweak': Same as 'rank', but returns 100 for scores outside the range.

    Returns:
    - percentile_rank (float or array-like): The percentile rank(s) of the score(s) within the dataset.

    Note:
    This function calculates the percentile rank of a score in a dataset. 
    The percentile rank is the percentage of scores in the dataset that are less than or equal to the given score.
    """
    a = np.asarray(a)
    score = np.asarray(score)

    if kind == 'rank':
        rank = (np.sum(a <= score) / len(a)) * 100
    elif kind == 'rankstrict':
        if score < a.min() or score > a.max():
            rank = np.nan
        else:
            rank = (np.sum(a <= score) / len(a)) * 100
    elif kind == 'rankweak':
        if score < a.min() or score > a.max():
            rank = 100
        else:
            rank = (np.sum(a <= score) / len(a)) * 100
    else:
        raise ValueError("Invalid 'kind' parameter. Use 'rank', 'rankstrict', or 'rankweak'.")

    return rank

# Example usage:
b = np.array([1, 2, 3, 4, 5])
bi = 2.5
percentile_rank = percentileofscore_np(b, bi, kind='rank')
print(f"The percentile rank of {bi} in 'b' is {percentile_rank}%")
