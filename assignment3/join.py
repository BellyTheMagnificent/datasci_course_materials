import MapReduce 
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


def mapper(record):
    # key: word
    # value: document name
    key = record[1]
    #value = record[1]
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of document name
    list = []
    header = ""
    #print list_of_values
    for v in list_of_values:
        if v[0] == "order":
            header = v
        else:
            mr.emit(header + v)
            
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

# =============================
# Do not modify above this line
