fname = "samples/out.txt"
with open(fname) as f:
    text = f.read().splitlines()
    text = [l[::-1] for l in text]

Y = len(text[0])
raw = "".join(text[::-1])

def str2bit(s):
    return '1' if s == 'X' else '0'

num = int("".join(map(str2bit, list(raw))), 2)

print(num * Y)
