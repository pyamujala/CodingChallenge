c = [0, 1]
k = 3


def print_de_bruijn_sequence(db_set, k):
    db_str = kfill(db_set[0], k)
    print(db_str)

    for i in range(0, (len(db_set) ^ k)):



def kfill(ch, k):
    s_str = ""
    for i in range(0, k):
        s_str = s_str + str(ch)

    return s_str

print_de_bruijn_sequence(c, k)
