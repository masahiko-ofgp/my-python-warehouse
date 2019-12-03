from functools import lru_cache

@lru_cache(maxsize=128)
def tarai(x, y, z):
    if x <= y:
        return y
    else:
        return tarai(tarai(x - 1, y, z),
                     tarai(y - 1, z, x),
                     tarai(z - 1, x, y))

if __name__ == '__main__':
    tarai(12, 6, 0)
