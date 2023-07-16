from __future__ import annotations
from typing import Any
from abc import ABC, abstractmethod

class Descriptor:
    def __init__(self, _value: Any[str, int, float] = None) -> None:
        if (isinstance(_value, int) or isinstance(_value, float)) and _value < 0:
            raise ValueError("Negative integer Value")
        self.value = _value
    
    def __get__(self, instance, owner_class) -> Any[str, int, float, Descriptor, None]:
        if instance:
            return self.value
        return self
    
    def __set__(self, instance, _value) -> None:
        if isinstance(_value, int) and _value < 0:
            raise ValueError("Negative integer Value")
        self.value = _value


class Resource(ABC):
    name = Descriptor()
    manufacturer = Descriptor()
    cost = Descriptor()
    total = Descriptor()
    allocated = Descriptor()

    def __init__(self, _name: str, _manufacturer: str, _cost: int, _total: int, _allocated: int) -> None:
        self.name = _name
        self.manufacturer = _manufacturer
        self.total = _total
        self.cost = _cost
        self.allocated = _allocated
        self.category = self.__class__.__name__.lower()

    @abstractmethod
    def claim(self, m: int) -> None:
        if m <= self.total - self.allocated:
            self.allocated += m
        else:
            raise ValueError("Not enough resources available to claim.")

    
    @abstractmethod
    def feedup(self, n: int) -> None:
        if n <= self.allocated:
            self.allocated -= n
        else:
            raise ValueError("Cannot free up more resources than currently allocated.")

    
    @abstractmethod
    def died(self, n: int) -> None:
        if n <= self.total - self.allocated:
            self.total -= n
            self.allocated -= n
        else:
            raise ValueError("Not enough resources available to die.")
    
    @abstractmethod
    def purchased(self, n: int) -> None:
        self.total += n
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.manufacturer}, {self.total}, {self.allocated})"

class CPU(Resource):
    cores = Descriptor()
    interface = Descriptor()
    socket = Descriptor()
    power_watts = Descriptor()

    def __init__(self, _name: str, _manufacturer: str, _cost: int, _total: int, _allocated: int, _cores: int, _interface: str, _socket: str, _power_watts: int) -> None:
        super().__init__(_name, _manufacturer, _cost, _total, _allocated)
        self.cores = _cores
        self.interface = _interface
        self.socket = _socket
        self.power_watts = _power_watts

    def feedup(self, n: int) -> None:
        return super().feedup(n)
    
    def claim(self, m: int) -> None:
        return super().claim(m)
    
    def died(self, n: int) -> None:
        return super().died(n)
    
    def purchased(self, n: int) -> None:
        return super().purchased(n)

    def __repr__(self) -> str:
        return f"{super().__repr__()}, Cores: {self.cores}, Interface: {self.interface}, Socket: {self.socket}, PowerWatts: {self.power_watts}"

class Storage(Resource):
    capacity_GB = Descriptor()
    def __init__(self, _name: str, _manufacturer: str, _cost: int, _total: int, _allocated: int, _capacity_GB: int) -> None:
        super().__init__(_name, _manufacturer, _cost, _total, _allocated)
        self.capacity_GB = _capacity_GB

    def __repr__(self) -> str:
        return f"{super().__repr__()}, Capacity: {self.capacity_GB} GB"

class HDD(Storage):
    size = Descriptor()
    rpm = Descriptor()
    def __init__(self, _name: str, _manufacturer: str, _cost: int, _total: int, _allocated: int, _capacity_GB: int, _size: float, _rpm: int) -> None:
        super().__init__(_name, _manufacturer, _cost, _total, _allocated, _capacity_GB)
        self.size = _size
        self.rpm = _rpm
    
    def feedup(self, n: int) -> None:
        return super().feedup(n)
    
    def claim(self, m: int) -> None:
        return super().claim(m)
    
    def died(self, n: int) -> None:
        return super().died(n)
    
    def purchased(self, n: int) -> None:
        return super().purchased(n)

    def __repr__(self) -> str:
        return f"{super().__repr__()}, Size: {self.size}, RPM: {self.rpm}"


class SSD(Storage):
    interface = Descriptor()
    def __init__(self, _name: str, _manufacturer: str, _cost: int, _total: int, _allocated: int, _capacity_GB: int, _interface: str) -> None:
        super().__init__(_name, _manufacturer, _cost, _total, _allocated, _capacity_GB)
        self.interface = _interface

    def feedup(self, n: int) -> None:
        return super().feedup(n)
    
    def claim(self, m: int) -> None:
        return super().claim(m)
    
    def died(self, n: int) -> None:
        return super().died(n)
    
    def purchased(self, n: int) -> None:
        return super().purchased(n)

    def __repr__(self) -> str:
        return f"{super().__repr__()}, Interface: {self.interface}"

