from smart_light import SmartLight
from smart_fan import SmartFan
from smart_ac import SmartAC
from device import Device

_REGISTRY = {
    "light": SmartLight,
    "fan": SmartFan,
    "ac": SmartAC,
}


class DeviceFactory:
    @staticmethod
    def create_device(device_type: str, device_id: str, name: str, location: str) -> Device:
        key = device_type.strip().lower()
        cls = _REGISTRY.get(key)
        if cls is None:
            supported = ", ".join(f'"{k}"' for k in _REGISTRY)
            raise ValueError(
                f'Unknown device type "{device_type}". Supported types: {supported}.'
            )
        return cls(device_id, name, location)

    @staticmethod
    def supported_types() -> list[str]:
        return list(_REGISTRY.keys())
