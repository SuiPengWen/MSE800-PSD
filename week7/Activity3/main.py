"""
IoT Smart Office Device Management System
Entry point – menu-driven CLI
"""

import sys

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    print("colorama not found. Run: pip install colorama")
    sys.exit(1)

from device_factory import DeviceFactory
from config_manager import ConfigManager
from smart_light import SmartLight
from smart_fan import SmartFan, SPEED_LEVELS
from smart_ac import SmartAC, AC_MODES

# ── colour helpers ─────────────────────────────────────────────────────────────

def c(text, colour=Fore.WHITE, bold=False):
    return (Style.BRIGHT if bold else "") + colour + str(text) + Style.RESET_ALL

def success(msg): print(c("  ✔  " + msg, Fore.GREEN))
def warn(msg):    print(c("  ⚠  " + msg, Fore.YELLOW))
def error(msg):   print(c("  ✘  " + msg, Fore.RED))
def info(msg):    print(c("  ℹ  " + msg, Fore.CYAN))
def rule(char="─", width=60): print(c(char * width, Fore.BLUE))

DEVICE_ICONS = {"light": "💡", "fan": "🌀", "ac": "❄️ "}

# ── banner ─────────────────────────────────────────────────────────────────────

def print_banner():
    rule("═")
    title = "  🏢  IoT Smart Office Device Management System  🏢"
    print(c(title, Fore.CYAN, bold=True))
    cfg = ConfigManager()
    print(c(f"  {cfg.get('system_name')}  |  {cfg.get('office_location')}", Fore.WHITE))
    rule("═")

# ── main menu ──────────────────────────────────────────────────────────────────

MENU = [
    ("1", "💡🌀❄️  Add new device"),
    ("2", "📋       List all devices"),
    ("3", "🎛️        Control a device"),
    ("4", "⚙️        View system configuration"),
    ("5", "🔁       Demonstrate Singleton pattern"),
    ("6", "🚪       Exit"),
]

def print_menu():
    print()
    rule()
    print(c("  MAIN MENU", Fore.MAGENTA, bold=True))
    rule()
    for key, label in MENU:
        print(f"  {c(f'[{key}]', Fore.YELLOW, bold=True)}  {label}")
    rule()

# ── device table printer ───────────────────────────────────────────────────────

def _status_colour(on: bool) -> str:
    return c("ON ", Fore.GREEN, bold=True) if on else c("OFF", Fore.RED)

def print_device_row(idx: int, device):
    status = _status_colour(device.status)
    dtype = type(device).__name__.replace("Smart", "").lower()
    icon = DEVICE_ICONS.get(dtype, "🔌")
    print(
        f"  {c(str(idx).rjust(2), Fore.YELLOW)}. "
        f"{icon} {c(device.name.ljust(20), Fore.WHITE, bold=True)}"
        f"[{status}]  "
        f"{c(device.location, Fore.CYAN)}"
        f"  ID:{c(device.device_id, Fore.MAGENTA)}"
    )

def print_status_block(device):
    rule()
    dtype = type(device).__name__.replace("Smart", "").lower()
    icon = DEVICE_ICONS.get(dtype, "🔌")
    print(c(f"  {icon}  {device.name}  —  Status Details", Fore.CYAN, bold=True))
    rule()
    for k, v in device.display_status().items():
        val_colour = Fore.GREEN if v in ("ON", "ON ") else (Fore.RED if v == "OFF" else Fore.WHITE)
        print(f"    {c(k.ljust(15), Fore.YELLOW)}: {c(v, val_colour)}")

# ── input helpers ──────────────────────────────────────────────────────────────

def prompt(msg, colour=Fore.CYAN) -> str:
    return input(c("  → " + msg + ": ", colour)).strip()

def prompt_int(msg, lo=None, hi=None) -> int:
    while True:
        raw = prompt(msg)
        try:
            val = int(raw)
            if lo is not None and val < lo:
                warn(f"Must be ≥ {lo}.")
                continue
            if hi is not None and val > hi:
                warn(f"Must be ≤ {hi}.")
                continue
            return val
        except ValueError:
            warn("Please enter a valid integer.")

def pick_device(devices: list):
    """Print numbered list and return chosen device or None."""
    if not devices:
        warn("No devices registered yet.")
        return None
    rule()
    print(c("  Select a device:", Fore.MAGENTA, bold=True))
    for i, d in enumerate(devices, 1):
        print_device_row(i, d)
    rule()
    idx = prompt_int("Enter device number", lo=1, hi=len(devices))
    return devices[idx - 1]

# ── option handlers ────────────────────────────────────────────────────────────

_device_counter = 0

def add_device(devices: list):
    global _device_counter
    cfg = ConfigManager()
    if len(devices) >= cfg.get("max_devices"):
        error(f"Device limit ({cfg.get('max_devices')}) reached. Update config to add more.")
        return

    rule()
    print(c("  ADD NEW DEVICE", Fore.MAGENTA, bold=True))
    supported = DeviceFactory.supported_types()
    print(c(f"  Supported types: {', '.join(supported)}", Fore.CYAN))
    rule()

    device_type = prompt("Device type (light / fan / ac)").lower()
    name = prompt("Device name")
    location = prompt("Location (e.g. Meeting Room 1)")

    if not name:
        warn("Name cannot be empty.")
        return

    try:
        _device_counter += 1
        device_id = f"DEV-{_device_counter:03d}"
        device = DeviceFactory.create_device(device_type, device_id, name, location)
        devices.append(device)
        success(f"Device '{name}' ({device_id}) added successfully!")
    except ValueError as exc:
        error(str(exc))


def list_devices(devices: list):
    rule()
    print(c("  ALL REGISTERED DEVICES", Fore.MAGENTA, bold=True))
    rule()
    if not devices:
        warn("No devices registered yet.")
    else:
        for i, d in enumerate(devices, 1):
            print_device_row(i, d)
    rule()


def control_device(devices: list):
    device = pick_device(devices)
    if device is None:
        return

    print_status_block(device)
    print()

    # Build control menu dynamically
    options = [
        ("1", "Turn ON"),
        ("2", "Turn OFF"),
    ]
    if isinstance(device, SmartLight):
        options += [("3", "Set brightness"), ("4", "Set color")]
    elif isinstance(device, SmartFan):
        options += [("3", "Set speed"), ("4", "Toggle oscillation")]
    elif isinstance(device, SmartAC):
        options += [("3", "Set temperature"), ("4", "Set mode")]
    options.append((str(len(options) + 1), "Back to main menu"))

    print(c("  CONTROLS", Fore.MAGENTA, bold=True))
    for key, label in options:
        print(f"    {c(f'[{key}]', Fore.YELLOW)}  {label}")
    print()

    choice = prompt("Choose action")

    try:
        if choice == "1":
            success(device.turn_on())
        elif choice == "2":
            success(device.turn_off())
        elif choice == "3":
            if isinstance(device, SmartLight):
                val = prompt_int("Brightness (0–100)", lo=0, hi=100)
                success(device.set_brightness(val))
            elif isinstance(device, SmartFan):
                print(c(f"  Levels: {', '.join(SPEED_LEVELS)}", Fore.CYAN))
                val = prompt("Speed (Low / Medium / High)")
                success(device.set_speed(val))
            elif isinstance(device, SmartAC):
                val = prompt_int("Temperature (16–30°C)", lo=16, hi=30)
                success(device.set_temperature(val))
        elif choice == "4":
            if isinstance(device, SmartLight):
                val = prompt("Color (e.g. Warm White, Blue)")
                success(device.set_color(val))
            elif isinstance(device, SmartFan):
                success(device.toggle_oscillation())
            elif isinstance(device, SmartAC):
                print(c(f"  Modes: {', '.join(AC_MODES)}", Fore.CYAN))
                val = prompt("Mode (Cool / Heat / Fan)")
                success(device.set_mode(val))
        elif choice == str(len(options)):
            return
        else:
            warn("Invalid option.")
            return
    except (ValueError, KeyError) as exc:
        error(str(exc))
        return

    # Show updated status
    print()
    print_status_block(device)


def view_config():
    cfg = ConfigManager()
    rule()
    print(c("  SYSTEM CONFIGURATION", Fore.MAGENTA, bold=True))
    rule()
    for k, v in cfg.display_config().items():
        print(f"    {c(k.ljust(20), Fore.YELLOW)}: {c(v, Fore.WHITE)}")
    print()
    print(c(f"  Python object id : {id(cfg)}", Fore.CYAN))
    rule()
    print()
    want_edit = prompt("Edit a setting? (y/n)").lower()
    if want_edit != "y":
        return
    key = prompt("Setting key")
    value = prompt("New value")
    try:
        result = cfg.update_setting(key, value)
        success(result)
    except (KeyError, ValueError) as exc:
        error(str(exc))


def demo_singleton():
    rule()
    print(c("  SINGLETON PATTERN DEMO", Fore.MAGENTA, bold=True))
    rule()
    info("Creating two ConfigManager references...")
    print()
    a = ConfigManager()
    b = ConfigManager()
    print(f"    {c('Reference A  id', Fore.YELLOW)}: {c(id(a), Fore.WHITE)}")
    print(f"    {c('Reference B  id', Fore.YELLOW)}: {c(id(b), Fore.WHITE)}")
    print(f"    {c('a is b       ', Fore.YELLOW)}: {c(a is b, Fore.GREEN if a is b else Fore.RED, bold=True)}")
    print()
    if a is b:
        success("Both references point to the SAME object — Singleton confirmed! ✔")
    else:
        error("References differ — Singleton is broken!")
    print()
    info("Modifying system_name via reference A ...")
    original = a.get("system_name")
    a.update_setting("system_name", "SmartOffice DEMO")
    print(f"    {c('Via A', Fore.YELLOW)}: {c(a.get('system_name'), Fore.WHITE)}")
    print(f"    {c('Via B', Fore.YELLOW)}: {c(b.get('system_name'), Fore.WHITE)}")
    print()
    success("Change made through A is visible through B — same instance!")
    # restore
    a.update_setting("system_name", original)
    rule()

# ── main loop ──────────────────────────────────────────────────────────────────

def main():
    # Ensure ConfigManager is initialised early (first call creates the singleton)
    ConfigManager()

    devices: list = []

    print_banner()

    while True:
        print_menu()
        choice = prompt("Your choice", colour=Fore.MAGENTA)

        if choice == "1":
            add_device(devices)
        elif choice == "2":
            list_devices(devices)
        elif choice == "3":
            control_device(devices)
        elif choice == "4":
            view_config()
        elif choice == "5":
            demo_singleton()
        elif choice == "6":
            rule("═")
            print(c("  👋  Goodbye! Smart Office system shutting down…", Fore.CYAN, bold=True))
            rule("═")
            sys.exit(0)
        else:
            warn("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
