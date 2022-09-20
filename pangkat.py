def squared(a,b):
    if b > 1:
        return a * squared(a, b-1)

    return a

print(squared(3,2))