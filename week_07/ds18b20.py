#!/usr/bin/env python3
"""
DS18B20 Temperature Reader - Starter Template (no solution)
Goal:
  - Discover the DS18B20 device directory under /sys/bus/w1/devices
  - Open the 'w1_slave' file for the first detected sensor
  - Read both lines and extract the temperature in °C
  - Return a float temperature OR None if something fails

Constraints:
  - Use the os module for directory listing and path building
  - Use open(...), read(), or readlines() for file I/O
  - Do not use external libraries beyond the standard library
"""

import os
import time


def read_temp():
    """
    Locate the DS18B20 sensor, open its data file, parse, and return °C as float.
    Return None if:
      - No sensor directory starting with '28-' is found
      - The CRC line does not contain 'YES'
      - The temperature value cannot be parsed
    """
    # TODO 1: Set the base directory path where 1-Wire devices appear.
    device_folder = "/sys/bus/w1/devices/"  # Keep as string, used with os.listdir

    # TODO 2: List all entries in device_folder and filter those starting with '28-'
    # Hint: [name for name in os.listdir(device_folder) if name.startswith("28-")]
    # If none found, return None.
    # devs = ...
    # if not devs:
    #     return None

    # TODO 3: Build the full path to the 'w1_slave' file for the FIRST sensor found.
    # Hint: you can use f-strings or os.path.join(device_folder, devs[0], "w1_slave")
    # sensor_file = ...

    # TODO 4: Open the file in read mode and read the two lines.
    # Use a 'with open(sensor_file, "r") as f:' block and call f.readlines()
    # lines = ...

    # TODO 5: Validate the first line contains 'YES' (CRC check). If not, return None.

    # TODO 6: Extract the temperature number from the second line (after 't=')
    # Convert it to a float and divide by 1000.0 to get °C.
    # Return the °C value.
    # If anything fails (missing 't=', ValueError), return None.

    # Placeholder to avoid syntax errors while students implement:
    return None


def loop():
    """
    Main loop:
      - Calls read_temp() repeatedly
      - Prints the result or an error message
      - Sleeps a bit between reads
      - Exits cleanly on CTRL-C
    """
    print("=== DS18B20 Temperature Reader ===")
    print("Reading every 3 second. Press CTRL-C to stop.\n")

    try:
        while True:
            temp_c = read_temp()
            if temp_c is None:
                # Keep this message simple; students can customize
                print("[ERROR] Could not read temperature (None). Retrying...")
            else:
                print(f"Temperature: {temp_c:.3f} °C")
            time.sleep(3.0)
    except KeyboardInterrupt:
        print("\nStopping reader. Goodbye!")


if __name__ == "__main__":
    loop()
