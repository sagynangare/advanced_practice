def data_type(a):
    if isinstance(a, int):
        print "Integer"
    if isinstance(a, float):
        print "Float"
    if isinstance(a, str):
        print "String"
    if isinstance(a, list):
        print "List"
    if isinstance(a, dict):
        print "Dictionary"

data_type("a")

