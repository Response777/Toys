import sys

def rot13(src):
    dst = ''
    for i in src:
        dst+=chr((ord(i) - ord('a') + 13) % 26 + ord('a'))
    return dst

if __name__ == '__main__':
    string = sys.argv[1].lower()
    print(rot13(string))