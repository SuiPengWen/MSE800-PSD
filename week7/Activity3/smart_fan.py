from device import Device

SPEED_LEVELS = ("Low", "Medium", "High")


class SmartFan(Device):
    ICON = "🌀"

    def __init__(self, device_id: str, name: str, location: str):
        super().__init__(device_id, name, location)
        self.speed = "Low"
        self.oscillation = False

    def turn_on(self) -> str:
        self.status = True
        osc = "oscillating" if self.oscillation else "fixed"
        return f"{self.ICON} {self.name} turned ON (speed: {self.speed}, {osc})"

    def turn_off(self) -> str:
        self.status = False
        return f"{self.ICON} {self.name} turned OFF"

    def set_speed(self, speed: str) -> str:
        speed = speed.strip().title()
        if speed not in SPEED_LEVELS:
            raise ValueError(f"Speed must be one of: {', '.join(SPEED_LEVELS)}")
        self.speed = speed
        return f"{self.ICON} {self.name} speed set to {speed}"

    def toggle_oscillation(self) -> str:
        self.oscillation = not self.oscillation
        state = "ON" if self.oscillation else "OFF"
        return f"{self.ICON} {self.name} oscillation turned {state}"

    def display_status(self) -> dict:
        info = self._base_info()
        info.update({
            "Speed": self.speed,
            "Oscillation": "ON" if self.oscillation else "OFF",
        })
        return info
