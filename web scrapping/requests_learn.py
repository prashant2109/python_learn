import requests

# payload = {'page':2, 'count':25}
# r = requests.get('https://httpbin.org/get')
# print (r.json())
# print (r.content)

payload = {'username':'corey', 'password':'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print (r.text)
