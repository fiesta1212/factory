# 25. Фабрика и Наблюдатель в системе управления инвентарем магазина электроники:
#    - Создайте классы для представления товаров электроники (смартфоны, ноутбуки и т.д.).
#    - Реализуйте фабрику для создания объектов электроники.
#    - Используйте наблюдателей для контроля за остатками товаров и уведомления о необходимости заказа.


from datetime import datetime
from typing import List, Dict, Any
from abc import ABC, abstractmethod


# Абстрактный класс для представления товара
class ElectronicDevice(ABC):
    def __init__(self, name: str, quantity: int):
        self.name = name  # Название товара
        self.quantity = quantity  # Количество на складе

    @abstractmethod
    def __str__(self) -> str:
        pass


# Класс для представления смартфона
class Smartphone(ElectronicDevice):
    def __str__(self) -> str:
        return f"Смартфон: {self.name}, Остаток: {self.quantity}"


# Класс для представления ноутбука
class Laptop(ElectronicDevice):
    def __str__(self) -> str:
        return f"Ноутбук: {self.name}, Остаток: {self.quantity}"


# Фабрика для создания объектов электроники
class ElectronicDeviceFactory:
    @staticmethod
    def create_device(device_type: str, name: str, quantity: int) -> ElectronicDevice:
        if device_type == "Smartphone":
            return Smartphone(name, quantity)
        elif device_type == "Laptop":
            return Laptop(name, quantity)
        else:
            raise ValueError("Неизвестный тип устройства.")


# Абстрактный класс Наблюдателя
class Observer(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


# Абстрактный класс Издателя
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


# Класс для представления инвентаря
class Inventory(Subject):
    def __init__(self):
        self.devices: Dict[str, ElectronicDevice] = {}  # Словарь для хранения устройств
        self._observers: List[Observer] = []  # Список наблюдателей

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.notify("Необходим заказ на товары!")

    def add_device(self, device: ElectronicDevice):
        self.devices[device.name] = device
        print(f"Добавлено: {device}")

    def update_quantity(self, device_name: str, quantity: int):
        if device_name in self.devices:
            self.devices[device_name].quantity += quantity
            print(f"Обновлено количество для {device_name}: {self.devices[device_name].quantity}")
        else:
            print(f"Устройство {device_name} не найдено в инвентаре.")

        if self.devices[device_name].quantity < 5:  # Порог для уведомления
            self.notify()


# Класс для представления менеджера инвентаря
class InventoryManager(Observer):
    def notify(self, message: str) -> None:
        print(f"Менеджер инвентаря: {message}")