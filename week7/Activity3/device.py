from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self, device_id: str, name: str, location: str):
        self.device_id = device_id
        self.name = name
        self.status = False  # False = off, True = on
        self.location = location

    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass

    @abstractmethod
    def display_status(self) -> dict:
        pass

    def _base_info(self) -> dict:
        return {
            "ID": self.device_id,
            "Name": self.name,
            "Location": self.location,
            "Status": "ON" if self.status else "OFF",
        }
