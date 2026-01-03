from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Тверская", "15", "42")
from_addr = Address("654321", "Санкт-Петербург", "Невский", "89", "11")

mailing = Mailing(to_addr, from_addr, 1955, "TRK123456789RU")

print(f"""Отправление {mailing.track} из {mailing.from_address.index},
      {mailing.from_address.city},
      {mailing.from_address.street},
      {mailing.from_address.house} - {mailing.from_address.apartment} в
      {mailing.to_address.index},
      {mailing.to_address.city}, {mailing.to_address.street},
      {mailing.to_address.house} - {mailing.to_address.apartment}.
      Стоимость {mailing.cost} рублей.""")
