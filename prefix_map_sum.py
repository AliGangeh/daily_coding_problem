#Google coding interview problem

#implement a prefixmapsum class with the following methods
#insert(key: str, value: int): Set a given key's value in the
#map if the key already exists, overwrite the value
#sum(prefix: str): return the sum of all values of keys that begin
#with a given prefix.

#for example you should be able to run the following code:
#mapsum.insert("columnar", 3)
#assert mapsum("col") == 3
#mapsum.insert

def prefix_map_sum (map, prefix):
    list = [(k,v) for k,v in map.items()]
    sum = 0
    #[(key, value), (key, value)]
    for i in range (len(list)):
        if prefix == list[i][0][:(len(prefix))]:
            sum += list[i][1]
    return sum

prefix_map_sum({"prom": 1, "proxy": 2, "profit": 5, "prolife": 10, "Ali": 6}, "pro")
