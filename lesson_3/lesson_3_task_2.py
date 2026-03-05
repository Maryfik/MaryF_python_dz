from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S24", "+79123456789"),
    Smartphone("Apple", "iPhone 15", "+79234567890"),
    Smartphone("Xiaomi", "14 Pro", "+79345678901"),
    Smartphone("Google", "Pixel 8", "+79456789012"),
    Smartphone("OnePlus", "12", "+79567890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
