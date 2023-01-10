def multiple_returns(sentence):
    if sentence == '':
        tuple_s = (len(sentence), None)
    else:
        tuple_s = (len(sentence), sentence[0])
    return (tuple_s)
