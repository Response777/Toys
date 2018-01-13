from datetime import date

def parse(line):
    name, date = line.split(',')
    return {"name": name, "date": date}

def load(fname):
    with open(fname) as f:
        lines = f.read().splitlines()
    dates = [parse(l) for l in lines]
    return dates

def daySince(dates):
    for m in dates:
        year, month, day = list(map(int, m['date'].split('-')))
        num_days = ( date.today() - date(year, month, day) ).days
        print("{:5} days since {}".format(num_days, m['name'])) 

if __name__ == '__main__':
    dates = load("memorials.csv")
    daySince(dates)
