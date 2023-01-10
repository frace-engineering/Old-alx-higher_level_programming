def multiple_returns(sentence):
    if sentence != '':
        tuple_s = (len(sentence), sentence[0])
    else:
        tuple_s = (0, None)
    print(tuple_s)
sentence = 'School' 
multiple_returns(sentence)
