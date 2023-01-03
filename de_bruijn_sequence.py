c = ['0', '1']
k = 5


def print_de_bruijn_sequence(db_set, k):
    create_strings(db_set, "", len(db_set), k)


def create_strings(s, p, l, k):
    if k == 0:
        print(p)
        return

    for i in range(l):
        p1 = p + s[i]
        create_strings(s, p1, l, k-1)


print_de_bruijn_sequence(c, k)
