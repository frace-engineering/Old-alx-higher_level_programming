def multiple_returns(sentence):
    if sentence is None:
        sentence[0] = 'None'
    else:
        tuple_s = (len(sentence), sentence[0])
    return tuple_s
