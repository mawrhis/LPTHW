
def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
        return aMap

def hasj_key(aMap, key):
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    return hash()