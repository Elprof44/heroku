import requests , time , random
l = 0
while True:
    ran = random.randint(100,500)
    ra = random.randint(1,50)
    url = 'http://localhost:5000/api'
    # url1 = f'http://localhost:5000/login/cap_{ra}/{ran}/capteur'
    r =requests.get(url)
    # if l < 25:
    #     d = requests.get(url1)
    #     print("statut ",d)
    #     l += 1
   
    print(r.text)