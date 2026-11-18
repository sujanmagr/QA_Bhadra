#create post using request 
import requests
url="https://jsonplaceholder.typicode.com/posts/1"
payload=  {
    "body": "THis is api automation"
  }

headers={
    "Authorization":"token sdkjfhaiuejdkskfdjklkaf"
}
response=requests.patch(url, json=payload, headers=headers)

print(response.json())
print(response.status_code)

assert response.status_code==200, "Post is not created"
print("Post is updated successfully")