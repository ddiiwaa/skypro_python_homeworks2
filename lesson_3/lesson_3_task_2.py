from smartphone import Smartphone

catalog = []
catalog.append(Smartphone(brand="Apple", model="iPhone 55", phone_number="+79224996644"))
catalog.append(Smartphone(brand="Samsung", model="Galaxy A32", phone_number="+79898664165"))
catalog.append(Smartphone(brand="Xiaomi", model="13T Pro", phone_number="+79397774646"))
catalog.append(Smartphone(brand="Nokia", model="Pixel 5", phone_number="+79760763258"))
catalog.append(Smartphone(brand="Apple", model="16 Pro Max", phone_number="+78397502077"))

for phone in catalog:
    print(phone)