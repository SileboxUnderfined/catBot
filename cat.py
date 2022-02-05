import requests

class Cat:
    @staticmethod
    def getRandomCat():
        imgarr = requests.get("https://api.thecatapi.com/v1/images/search")
        img = imgarr.json()[0]['url']
        return img

"""if __name__ in "__main__":
    a = Cat()
    print(a.getRandomCat())"""