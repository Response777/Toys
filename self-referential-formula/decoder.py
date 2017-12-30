def self_referential_formula(x, y, C):
    index = (-C*x)-(y%C)
    v = ((y // C) >> (-index)) & 1
    return v

def draw(Y, k):
    X = (len(bin(k)) + Y) // Y

    lines = []
    for x in range(0,X):
        line = ''
        for y in range(k,k+Y):
            if self_referential_formula(x, y, Y):
                line += 'X'
            else:
                line += ' '

        print(line)

if __name__ == '__main__':
    # x in [0,X)
    # y in [k,k+Y)
    fname = "samples/in.txt"
    with open(fname) as f:
        text = f.read().splitlines()

    Y = int(text[0])
    k = int(text[1])

    draw(Y,k)
