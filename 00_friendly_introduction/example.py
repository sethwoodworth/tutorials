def print_madlib(subject, object, sentence="{} {} to get that {}"):
    # I He She They
    if subject in ['I', 'They']:
        verb = 'want'
    else:
        verb = 'wants'
    print(sentence.format(subject, verb, object))

things_to_print = [ ['I', "cat's meow"], ['He', "cat's pajamas"] ]
for a, b in things_to_print:
    print_madlib(object=b, subject=a)
    print_madlib(object=b, subject=a, sentence="{} {} is wearing {}")
