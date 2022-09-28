from email.mime import image
import os
from unicodedata import name
#for run this code with project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
#the famest laibrary making dummu data
from faker import Faker
#for makeing random things in data
import random
#the models we will add dummy data in them
from prouducts.models import items,cateogry,brand
#n:the numbers of dummy data will add


def seed_items(n):
    fake=Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.png','7.png','8.png','9.png','10.png',]
    flag_type=['new','features','sale']
    for _ in range(n):
        name=fake.name()
        #slice for the numbers of images randomly
        flag=flag_type[random.randint(0,2)],
        price=round(random.uniform(20.99,99.99),2),
        sku=random.randint(1,1000),
        subtitle=fake.text(max_nb_chars=250),
        vedio='https://youtu.be/LLJSfU8oD60',
        #get all cat -->we can't get relation by num -->from 1to 10 that dummy data of category was added
        Cateogry=cateogry.objects.get(id=random.randint(1,10)),
        Brand=brand.objects.get(id=random.randint(1,10)),
        img=f"items/{images[random.randint(0,9)]}"

        items.objects.create(
            name=name,
            flag=flag,
            price=price,
            sku=sku,
            subtitle=subtitle,
            vedio=vedio,
            cateogry=Cateogry,
            brand=Brand,
            itemimage=img
            )
    print(f'sucssefuly added {n} item')


#seed_brand(5)
#seed_cateogry(10)
seed_items(100)