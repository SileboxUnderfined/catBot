import requests
from vk_api import VkUpload
from os import environ

class Cat:
    @staticmethod
    def getRandomCat(vk):
        upload = VkUpload(vk)
        imgarr = requests.get("https://api.thecatapi.com/v1/images/search")
        img = imgarr.json()[0]['url']
        photo = upload.photo(photos=img,album_id=environ['ALBUM_ID'],group_id=environ['GROUP_ID'])
        photoProps = photo[0]
        attachment = f'photo{photoProps["owner_id"]}_{photoProps["id"]}_{photoProps["access_key"]}'
        return attachment

"""if __name__ in "__main__":
    a = Cat()
    print(a.getRandomCat())"""