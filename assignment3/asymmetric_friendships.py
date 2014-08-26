import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (person, friend) / (friend, person)
    # value: +/- 1
    i = 0
    #while i < len(record):
    key = record[0]
    value = record[1]
    #    mr.emit_intermediate(record[i],record[len(record)-(1+i)])
    print key + "," + value, 1
    print value + "," + key, -1
    mr.emit_intermediate(key + "," + value, 1)
    mr.emit_intermediate(value + "," + key, -1)
        
def reducer(key, list_of_values):
    # key: person
    # value: friend
    
    ## sum up the tuple values
    total = sum(list_of_values)
    ## split the key into dictionary object
    dict = key.split(",")
    
    print key, list_of_values
    
    # output if it is not asymmetric relation (total not equal to 0)
    if total <> 0:
        mr.emit((dict[0], dict[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
