from datetime import datetime
from inventory import ElectronicDeviceFactory, Inventory, InventoryManager


if __name__ == "__main__":
    # Создаем инвентарь
    inventory = Inventory()

    # Создаем менеджера инвентаря
    manager = InventoryManager()
    inventory.attach(manager)

    # Создаем устройства через фабрику
    smartphone1 = ElectronicDeviceFactory.create_device("Smartphone", "iPhone 13", 20)
    laptop1 = ElectronicDeviceFactory.create_device("Laptop", "Dell XPS 13", 15)

    # Добавляем устройства в инвентарь
    inventory.add_device(smartphone1)
    inventory.add_device(laptop1)

    # Обновляем количество устройств
    inventory.update_quantity("iPhone 13", -6)  # Уменьшаем количество
    inventory.update_quantity("Dell XPS 13", -4)  # Уменьшаем количество
    inventory.update_quantity("iPhone 13", -1)  # Уменьшаем количество