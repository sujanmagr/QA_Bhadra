import requests
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.delete(url)
print("The status code is: ", response.status_code)
# print(response.json())

status_code=response.status_code

# if status_code==200:
#     print("The request was successful.")

# else:
#     print("The request failed with status code: ", status_code)

assert status_code==200, "The post is not deleted"
print("Post is deleted successfully")