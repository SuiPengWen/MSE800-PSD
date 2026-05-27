from device import Device


class SmartLight(Device):
    ICON = "💡"

    def __init__(self, device_id: str, name: str, location: str):
        super().__init__(device_id, name, location)
        self.brightness = 50   # 0–100 %
        self.color = "White"

    def turn_on(self) -> str:
        self.status = True
        return f"{self.ICON} {self.name} turned ON (brightness {self.brightness}%, color: {self.color})"

    def turn_off(self) -> str:
        self.status = False
        return f"{self.ICON} {self.name} turned OFF"

    def set_brightness(self, value: int) -> str:
        if not 0 <= value <= 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.brightness = value
        return f"{self.ICON} {self.name} brightness set to {value}%"

    def set_color(self, color: str) -> str:
        self.color = color.strip().title()
        return f"{self.ICON} {self.name} color set to {self.color}"

    def display_status(self) -> dict:
        info = self._base_info()
        info.update({
            "Brightness": f"{self.brightness}%",
            "Color": self.color,
        })
        return info
