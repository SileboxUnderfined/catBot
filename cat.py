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

        path = f'tempImages/{randint(1,1000000)}.jpg'
        f = open(path,'wb')
        f.write(imgreq.content)
        f.close()
        return path

    @staticmethod
    def removeTempImages():
        from os import remove,listdir
        files = listdir('tempImages/')
        for file in files:
            remove(f'tempImages/{file}')

"""if __name__ in "__main__":
    a = Cat()
    print(a.getRandomCat())"""