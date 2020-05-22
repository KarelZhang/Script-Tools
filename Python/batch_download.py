import requests
root = 'path for save datas'
with open('url.txt', 'r') as f:
    for line in f:
        url = line.replace('\n','')
        items = line.replace('\n', '').split('/')
        name = items[-1]
        print(name)
        r = requests.get(url, stream = True)
        with open(root + '/' + name, "wb") as code:
            for chunck in r.iter_content(chunk_size=1024*4):
                code.write(chunck)
