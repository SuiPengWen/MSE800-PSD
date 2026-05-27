from device import Device

AC_MODES = ("Cool", "Heat", "Fan")


class SmartAC(Device):
    ICON = "❄️"

    def __init__(self, device_id: str, name: str, location: str):
        super().__init__(device_id, name, location)
        self.temperature = 24  # °C, range 16–30
        self.mode = "Cool"

    def turn_on(self) -> str:
        self.status = True
        return f"{self.ICON} {self.name} turned ON ({self.mode} mode, {self.temperature}°C)"

    def turn_off(self) -> str:
        self.status = False
        return f"{self.ICON} {self.name} turned OFF"

    def set_temperature(self, temp: int) -> str:
        if not 16 <= temp <= 30:
            raise ValueError("Temperature must be between 16°C and 30°C.")
        self.temperature = temp
        return f"{self.ICON} {self.name} temperature set to {temp}°C"

    def set_mode(self, mode: str) -> str:
        mode = mode.strip().title()
        if mode not in AC_MODES:
            raise ValueError(f"Mode must be one of: {', '.join(AC_MODES)}")
        self.mode = mode
        return f"{self.ICON} {self.name} mode set to {mode}"

    def display_status(self) -> dict:
        info = self._base_info()
        info.update({
            "Temperature": f"{self.temperature}°C",
            "Mode": self.mode,
        })
        return info
