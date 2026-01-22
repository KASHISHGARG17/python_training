d = { "name" : "kashish " , "gender" : "female" ,"age" :20 , "city" : "hisar"}
print(d)

print(d["name"])  #2

print(list(d.values()))#3

d["age"] = 21
print(d)#4

for key in d:#5
    print(d.keys())

student = {
    "student1": {"name": "Adhikansh", "age": 20},
    "student2": {"name": "Kashish", "age": 21},
    "student3": {"name": "niki", "age": 22}
}
print(student)#6

dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = {"c": 3}
combined_dict = {
    "dict1": dict1,
    "dict2": dict2,
    "dict3": dict3
}
print(combined_dict)#7

list1 = ["name", "age", "gender"]
list2 = ["Kashish", 21, "Female"]
result_dict = dict(zip(list1, list2))
print(result_dict)#8

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = dict1 | dict2   # 9
print(merged_dict)
#print(dict1.update (dict2))

sample_dict = {
    "C": 92,
    "Java": 66,
    "Python": 85
}

lowest_key = min(sample_dict.items(), key=lambda x:x[1])
print("Key with lowest value:", lowest_key) #10




