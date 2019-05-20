numBuckets = 47  #this is ugly.  We will see a better way soon

def create():
    global numBuckets
    hSet = []
    for i in range(numBuckets):
        hSet.append([])
    return hSet

def hashElem(e):
    global numBuckets
    return e%numBuckets

def insert(hSet, i):
    hSet[hashElem(i)].append(i)

def remove(hSet, i):
    newBucket = []
    for j in hSet[hashElem(i)]:
        if j != i:
            newBucket.append(j)
    hSet[hashElem(i)] = newBucket

def member(hSet, i):
    return i in hSet[hashElem(i)]