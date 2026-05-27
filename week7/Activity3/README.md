# 🏢 IoT Smart Office Device Management System

A Python CLI application that simulates managing IoT devices in a smart office environment.
It demonstrates two classic OOP design patterns — **Factory** and **Singleton** — alongside
inheritance and abstract classes.

---

## Project Structure

```
Activity3/
├── main.py            # Entry point – menu-driven CLI (colorama UI)
├── device.py          # Abstract base class: Device
├── smart_light.py     # Concrete class: SmartLight 💡
├── smart_fan.py       # Concrete class: SmartFan 🌀
├── smart_ac.py        # Concrete class: SmartAC ❄️
├── device_factory.py  # Factory Pattern implementation
├── config_manager.py  # Singleton Pattern implementation
└── README.md
```

---

## Design Patterns Explained

### Factory Pattern (`device_factory.py`)

**Intent:** Define an interface for creating objects, but let a single factory method
decide which class to instantiate. Callers are decoupled from concrete constructors.

**How it works here:**

```python
device = DeviceFactory.create_device("light", "DEV-001", "Desk Lamp", "Room A")
```

- `DeviceFactory.create_device()` inspects the `device_type` string and maps it to the
  correct class (`SmartLight`, `SmartFan`, or `SmartAC`).
- Adding a new device type only requires registering it in `_REGISTRY` — no changes
  anywhere else.
- Raises `ValueError` for unsupported types, keeping error handling centralised.

**Benefits:** Open/Closed Principle (open for extension, closed for modification),
cleaner `main.py` with no `if/elif` device chains.

---

### Singleton Pattern (`config_manager.py`)

**Intent:** Ensure a class has only one instance and provide a global access point to it.

**How it works here:**

```python
class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            ...          # initialise once
        return cls._instance
```

- `__new__` is called before `__init__`. On the first call it creates and stores
  the instance; every subsequent call returns the same object.
- `ConfigManager()` called from anywhere in the codebase always returns the same
  Python object (same `id()`).
- The Singleton Demo (Menu Option 5) proves this live by comparing two references.

**Benefits:** One source of truth for system configuration, no risk of diverging
settings across modules.

---

## How to Run

### 1. Install dependency

```bash
pip install colorama
```

### 2. Run the application

```bash
cd path/to/Activity3
python main.py
```

> Requires **Python 3.10+** (uses `list[str]` type hints without `from __future__`).

---

## Menu Options

| # | Option | Description |
|---|--------|-------------|
| 1 | Add new device | Prompts for type (light/fan/ac), name, location; uses Factory |
| 2 | List all devices | Colour-coded table of all registered devices and their status |
| 3 | Control a device | Turn on/off; change brightness, speed, temperature, etc. |
| 4 | View / edit config | Shows Singleton config; optionally update a setting |
| 5 | Singleton demo | Creates two references, proves `a is b` and shared state |
| 6 | Exit | Graceful shutdown |

---

## Sample Output Descriptions

### Banner
```
════════════════════════════════════════════════════════════
  🏢  IoT Smart Office Device Management System  🏢
  SmartOffice v1  |  Building A, Floor 3
════════════════════════════════════════════════════════════
```
Displayed in **cyan** on startup, showing the system name and office location pulled
from the `ConfigManager` singleton.

### Add Device (Option 1)
The CLI prompts for type, name, and location, then prints a green success message:
```
  ✔  Device 'Desk Lamp' (DEV-001) added successfully!
```

### List Devices (Option 2)
Each device appears on one line with its icon, coloured ON/OFF badge, location, and ID:
```
   1. 💡 Desk Lamp            [ON ]  Room A   ID:DEV-001
   2. 🌀 Ceiling Fan          [OFF]  Lobby    ID:DEV-002
   3. ❄️  Server Room AC       [ON ]  IT Room  ID:DEV-003
```

### Control Device (Option 3)
After selecting a device, a status block shows current attributes; the user picks an
action (e.g., set brightness to 80%), and the updated status block is printed:
```
  ✔  💡 Desk Lamp brightness set to 80%
```

### Singleton Demo (Option 5)
```
    Reference A  id : 2157432891584
    Reference B  id : 2157432891584
    a is b        : True
  ✔  Both references point to the SAME object — Singleton confirmed! ✔
```
Both `id()` values are identical, confirming a single instance.

---

## Error Handling

- Non-integer input where a number is expected → re-prompts with a warning.
- Out-of-range values (brightness > 100, temperature outside 16–30) → `ValueError` caught and displayed in red.
- Unknown device type or config key → descriptive error message in red, no crash.
- Device limit exceeded → warning message before attempting creation.
