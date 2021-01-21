# L-01: Return the last element of a list.
def last(l):
    if isinstance(l, list):
        try:
            return l[-1]
        except IndexError:
            return None
    else:
        raise ValueError("l must be list.")

#L-02: Find the last but one(last and penultimate) elements of a list.
def last_two(l):
    if isinstance(l, list):
        try:
            x = l[-1]
            y = l[-2]
            return [y, x]
        except IndexError:
            return None
    else:
        raise ValueError("l must be list.")

#L-03: Find the k's element of a list.
def at(k, l):
    if (isinstance(l, list)):
        if not k > 0:
            raise ValueError("k must be greater than 1.")
        elif k == 1:
            try:
                return l[0]
            except:
                raise ValueError("l must be list.")
        else:
            try:
                return at(k - 1, l[1:])
            except:
                raise IndexError("k is too large for l.")
    else:
        raise ValueError("l must be list.")

#L-04: Find the number of elements of a list.
def length(l):

    def aux(n, ls):
        if ls == []:
            return n
        else:
            return aux(n + 1, ls[1:])

    if isinstance(l, list):
        return aux(0, l)
    else:
        raise ValueError("l must be list.")

#L-05: Reverse a list.
def revrs(l):
    if isinstance(l, list):
        return l[::-1]
    else:
        raise ValueError("l must be list.")

#L-06: Find out whether a list is a parindrome.
def is_parindrome(l):
    if isinstance(l, list):
        return l == l[::-1]
    else:
        raise ValueError("l must be list.")

#L-07: Flatten a nested list structure.
def flatten(l):

    def aux(acc, ls):
        if ls == []:
            return acc
        else:
            if not isinstance(ls[0], list):
                return aux(acc + [ls[0]], ls[1:])
            else:
                return aux(aux(acc, ls[0]), ls[1:])

    if isinstance(l, list):
        return aux([], l)
    else:
        raise ValueError("l must be list.")

#L-08: Eliminate consecutive duplicates of list elements.
def compress(l):
    if isinstance(l, list):
        l_to_set = set(l)
        return list(l_to_set)
    else:
        raise ValueError("l must be list.")

#L-09: Pack consecutive duplicates of list elements into sublists.
def pack(l):
    pass
        
