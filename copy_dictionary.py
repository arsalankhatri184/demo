dict = {
    id:100,
    "name":"Arsalan",
    "field":"Analytics"
}
new_dict = dict 
# remove id key-value pair in new_dict
new_dict.pop(id)
# print original dictionary
print(dict)
# print dublicate/copy dictionary
print(new_dict)
# print keys and values from dictionary
print(dict.keys())
print(dict.values())
# print both keys and values by using for loop
for key, value in dict.items():
    print(f"{key}: {value}")