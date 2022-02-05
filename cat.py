import requests
from random import randint

class Cat:
    @staticmethod
    def getRandomCat():
        imgarr = requests.get("https://api.thecatapi.com/v1/images/search")
        img = imgarr.json()[0]['url']
        imgreq = requests.get(img)
        f = open(f'tempImages/{randint(1,100000)}.jpg','wb')
        f.write(imgreq.content)
        return f

    @staticmethod
    def removeTempImages():
        from os import remove,listdir
        files = listdir('tempImages/')
        for file in files:
            remove(f'tempImages/{file}')

"""if __name__ in "__main__":
    a = Cat()
    print(a.getRandomCat())"""