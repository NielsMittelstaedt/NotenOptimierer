import os
import string
import random

def store(json):
    file_name = "data/"+''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".data"
    f = open(file_name, "x")
    f.write(json)
    return file_name

def solve(json):
    file_name = store(json)
    stream = os.popen("./test " + file_name)
    output = stream.read()
    print(output)
    os.remove(file_name)

solve("30\n1,22.5\n1.3,8;1,8;1.7,6;1,6\n1,6;1.3,6;1.3,6\n1,6;1.7,7;1.7,7\n3,6;2.3,6;1,8;1,6\n1,3;1,5\n1,6;1,6;1.7,6;1.7,6\n1,6;1,6;1,6;2,4")
