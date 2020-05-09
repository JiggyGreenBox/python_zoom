from objs.jiggyone import Jiggyone
from objs.jiggytwo import Jiggytwo


mylist = {}
mylist["Shared"] = "jiggy"

j1 = Jiggyone(mylist)
j2 = Jiggytwo(mylist)

print(j1.name)
print(j2.name)

j1.addList("test","a test")
j1.addList("te1st","b test")

print(mylist)