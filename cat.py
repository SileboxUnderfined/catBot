import requests
from vk_api import VkUpload

class Cat:
    @staticmethod
    def getRandomCat(vk):
        upload = VkUpload(vk)
        imgarr = requests.get("https://api.thecatapi.com/v1/images/search")
        img = imgarr.json()[0]['url']
        photo = upload.photo_messages(img)
        photoProps = photo[0]
        attachment = f'photo{photoProps["owner_id"]}_{photoProps["id"]}_{photoProps["access_key"]}'
        return attachment

"""if __name__ in "__main__":
    a = Cat()
    print(a.getRandomCat())"""