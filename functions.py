import random, datetime
def getNumber():
    lst = [i for i in range(1, 38)]
    line = []
    for _ in range(6):
        line.append(lst.pop(lst.index(random.choice(lst))))
    line.sort()
    line = list(map(lambda x: str(x), line))
    st_line = ", ".join(line)
    return st_line

def getCurrentTime():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M")