from requests import post, get
from address import url

r = get(url + '/harvey')
print(r.json())

r = get(url + '/hello/harvey')
print(r.json())

input = {
      "a": [2, 4],
      "b": [5, 6]
}
r = post(url + '/distance', json=input)
print(r.json())

