class ConfigManager:
    _instance = None

    _DEFAULTS = {
        "system_name": "SmartOffice v1",
        "version": "1.0.0",
        "office_location": "Building A, Floor 3",
        "max_devices": 20,
    }

    def __new__(cls):
        if cls._instance is None:
            obj = super().__new__(cls)
            obj._settings = dict(cls._DEFAULTS)
            cls._instance = obj
        return cls._instance

    # ── read ──────────────────────────────────────────────────────────────────

    def get(self, key: str):
        return self._settings.get(key)

    def display_config(self) -> dict:
        return dict(self._settings)

    # ── write ─────────────────────────────────────────────────────────────────

    def update_setting(self, key: str, value) -> str:
        if key not in self._settings:
            raise KeyError(f'Unknown setting "{key}". Valid keys: {list(self._settings)}')
        if key == "max_devices":
            value = int(value)
            if value < 1:
                raise ValueError("max_devices must be at least 1.")
        self._settings[key] = value
        return f'Setting "{key}" updated to "{value}".'

    # ── singleton identity ─────────────────────────────────────────────────────

    @classmethod
    def instance_id(cls) -> int:
        return id(cls._instance) if cls._instance else -1
