import requests
import logging
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen


save_dir='images/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


query='Richa singh'
#url=https://www.google.com/search?sxsrf=AB5stBjdPmdBk0qymCQyxna6N8VKOAW4Sg:1690691119180&q={query}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiCqNWcy7WAAxXU_7sIHTNnC1sQ0pQJegQIDhAB&biw=1536&bih=754&dpr=1.25

response=requests.get(f'https://www.google.com/search?sxsrf=AB5stBjdPmdBk0qymCQyxna6N8VKOAW4Sg:1690691119180&q={query}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiCqNWcy7WAAxXU_7sIHTNnC1sQ0pQJegQIDhAB&biw=1536&bih=754&dpr=1.25')



soup=BeautifulSoup(response.content,'html.parser')

image_tags=soup.find_all('img')
del image_tags[0]
print(image_tags)
print(len(image_tags))

for i in image_tags:
    print(i['src'])
    image_url=i['src']
    image_data=requests.get(image_url).content
    print(image_data)
    with open(os.path.join(save_dir,f"{query}_{image_tags.index(i)}.jpg"),'wb') as f:
       
        f.write(image_data)



