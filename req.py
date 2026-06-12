import requests as r
import json
# url='https://jsonplaceholder.typicode.com/posts/1'
# data=r.get(url)
# for pro in data.json():
#     print(pro())

url="https://fakestoreapi.com/users"
# data=r.get(url)
# print(data.json())


# create a user 
# details={
#     'id':'11',
#     'name':'durga',
#     'city':'baptla'

# }

# res=r.post(url,details)
# print(res)


# url="http://localhost:3000/users"
# details={
#     'id':'11',
#     'name':'durga',
#     'city':'baptla'

# }

# res=r.post(url,details)
# print(res)
# data=r.get(url)
# print(data)
# print(data.json())

# details={
#     'id':'12',
#     'name':'anil',
#     'city':'poodur'

# }
# # print(type(details))
# json_data=json.dumps(details)
# # print(type(json_data))
# res=r.post(url,json_data)
# print(res)

# details={
#     'id':'15',
#     'name':'prashanth',
#     'city':'jagtial'
# }
# json_data=json.dumps(details)
# res=r.post(url,json_data)
# print(res.json())
url="http://localhost:3000/users/15"
# details={
#     'id':'15',
#     'name':'prashanth',
#     'city':'hyderabad'
# }
# json_data=json.dumps(details)
# res=r.put(url,json_data)
# print(res.json())
details={
    'id':'15',
    'batch':'d7r'
}
# json_data=json.dumps(details)
# res=r.patch(url,json_data)
# print(res)

# res=r.delete(url)
# print(res.json())
json_data=json.dumps(details)
res=r.patch(url,json_data)
print(res)
