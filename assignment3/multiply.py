import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    
    i = 0 
    N = 5
    k= 0
    list = []
    mat = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    
    while k < N:
        if (mat == "a"):
            mr.emit_intermediate((row, k),(col, val))
        else:
            mr.emit_intermediate((k, col) ,(row, val))
        k += 1
        
   # mr.emit_intermediate(record[0] + "_" + str(record[1])+str(record[2]), record[3])
    #for (i, j, a_ij) in record:
    #    mr.emit_intermediat(i, a_ij * v[j])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    i = 0
    list_mapped = {}
    
    ## map value from matrix A and matrix B by Colunm of Matrix A and Row of Matrix B
    for v in list_of_values: 
        list_mapped.setdefault(v[0], [])
        list_mapped[v[0]].append(v[1])
    
    ## for each mapped value in the key, sum up the multiple result
    for u in list_mapped:
        val = list_mapped[u]
        if len(val) == 2:
              total += val[0] * val[1]
              
    #print key, list_mapped
    mr.emit((key[0], key[1], total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
