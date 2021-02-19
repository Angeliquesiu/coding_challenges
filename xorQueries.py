# XOR QUERIES

# compute the XOR of elements from Li to Ri (arr[Li+1] xor arr[Li+2] xor ... xor arr[Ri])
# arr: array of positive integers
# queries: range of indexes of arr i.e. [0,3] means arr[0:4]
# arr = [1,3,4,8]
# queries = [[0,1],[1,2],[0,3],[3,3]]
# output = [2,7,14,8]
def xorQueries(arr, queries):
    import itertools
    import operator
    B = list(itertools.accumulate(arr, func = operator.xor)) + [0]
    # if a != 0 taking only B[b] would return 'too much'
    # thus B[a - 1] ^ B[b] solves this
    # if a == 0 then it will result in index -1, that is why the [0] was added above
    return (B[a - 1] ^ B[b] for a, b in queries)