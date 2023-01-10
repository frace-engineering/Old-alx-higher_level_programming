def multiple_returns(sentence):
    if sentence != '':
        tuple_s = (len(sentence), sentence[0])
    else:
        tuple_s = (0, None)
    print(tuple(tuple_s))
