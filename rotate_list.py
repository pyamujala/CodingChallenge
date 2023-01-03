lst = [1, 2, 3, 4, 5, 6]
print(lst)


def rotate_list_1(ilist, nplases):
    for i in range(0, nplases):
        for idx in range(0, len(ilist)):
            if idx+1 >= len(ilist):
                break

            print(len(ilist), idx)
            pele = ilist[idx]
            ilist[idx] = ilist[idx+1]
            ilist[idx+1] = pele

    print(ilist)


def rotate_list_2(ilist, nplases):
    for i in range(0, nplases):
        ilist.append(ilist.pop(0))

    print(ilist)


rotate_list_2(lst, 12)

