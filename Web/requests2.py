import requests
r = requests.get('http://higpen.jellybean.jp/')
with open('download2.html', 'wb') as file:
    file.write(r.content)
