import json
from collections import Iterable
with open('p10/data.json','r', encoding='utf-8') as f:
    content=f.read()
print(content)
py_dict=json.loads(content)#转换成python可解析的格式
print(py_dict)
print(isinstance(py_dict,dict))
list1 = []
print(type(list1))
def aaa(py_dict):
    if isinstance(py_dict,dict):
        for k,v in py_dict.items():
            if isinstance(v,int):
                list1.append([k,v])
            if isinstance(py_dict,dict):
                aaa(v)
            if isinstance(py_dict,list):
                aaa(v)
    if isinstance(py_dict,list):
        for i in py_dict:
            if isinstance(i,int):
                pass
            if isinstance(py_dict,dict):
                aaa(i)
            if isinstance(py_dict,list):
                aaa(i)
aaa(py_dict)
list2 = sorted(list1,key= lambda x:x[1],reverse=True)
print(list2)
with open("p2.txt",'w',encoding="utf-8") as f:
    for i in list2:
        f.write(i[0]+":"+str(i[1])+"\n")