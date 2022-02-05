import requests
from random import randint

class Cat:
    @staticmethod
    def getRandomCat():
        imgarr = requests.get("https://api.thecatapi.com/v1/images/search")
        img = imgarr.json()[0]['url']
        imgreq = requests.get(img)
        from os import mkdir
        from os.path import exists
        if exists('tempImages') == False:
            mkdir('tempImages')
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