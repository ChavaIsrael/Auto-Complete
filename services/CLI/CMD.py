
def cli(t, seq):
    s = seq.split()
    for word in s:
        if t.seacrh(word) == True:
            