from Address import Address
from Mailing import Mailing

sender = Address(111111,"Perm","Pushcina","14","88")
recipient = Address(2222222,"New-York","Colotushcina","9","11")

package = Mailing(recipient, sender, 500, "Pushcina - Colotushcina")

print("Отправление", package.track, "из", package.from_address.Index,",",package.from_address.Syti,",",package.from_address.Street,",", package.from_address.House," - ", package.to_address.Index,",",package.to_address.Syti,",",package.to_address.Street,",", package.to_address.House,". Стоимость ", package.cost, "рублей")