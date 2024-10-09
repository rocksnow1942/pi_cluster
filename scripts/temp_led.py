import glob
import pathlib
from time import sleep

from gpiozero import PWMLED  # type:ignore


def get_cpu_temperature() -> float:
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        return int(f.read()) / 1000


def get_ssd_temperature() -> float:
    # find file in /sys/class/hwmon/hwmon*/name that contains "nvme"
    name_files = glob.glob("/sys/class/hwmon/hwmon*/name")
    nvme_name_file = next(f for f in name_files if "nvme" in open(f).read())
    hwmon_dir = pathlib.Path(nvme_name_file).parent
    # check device model
    model_file = hwmon_dir / "device/model"
    # ensure this is a Samsung SSD
    if "samsung ssd" not in model_file.read_text().lower():
        raise RuntimeError("This is not a Samsung SSD")
    # read temperature from temp1_input
    temp_file = hwmon_dir / "temp1_input"
    return int(temp_file.read_text()) / 1000


TEMP_MIN = 30
TEMP_MAX = 60


def normalize(temp: float) -> float:
    # normalize to 0-1
    r = (temp - TEMP_MIN) / (TEMP_MAX - TEMP_MIN)
    return max(0, min(1, r))


def main() -> None:
    led = PWMLED(26)
    while True:
        cpu_temp = get_cpu_temperature()
        ssd_temp = get_ssd_temperature()
        print(f"CPU: {cpu_temp}°C, SSD: {ssd_temp}°C")
        cpu_r = normalize(cpu_temp)
        ssd_r = normalize(ssd_temp)
        led.value = min(cpu_r + ssd_r, 1)
        sleep(5)


if __name__ == "__main__":
    main()
