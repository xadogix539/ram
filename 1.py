# prompt: python script gb ram 64bit CPU Core System Ubuntu Linux 

import platform
import psutil
import os

def get_system_info():
  """Retrieves and prints system information."""

  print("System Information:")
  print(f"  Platform: {platform.system()}")
  print(f"  Platform Release: {platform.release()}")
  print(f"  Platform Version: {platform.version()}")
  print(f"  Architecture: {platform.architecture()[0]}")
  print(f"  Processor: {platform.processor()}")

  print("\nCPU Information:")
  print(f"  CPU Cores: {os.cpu_count()}")
  print(f"  CPU Usage: {psutil.cpu_percent()}%")

  print("\nMemory Information:")
  mem = psutil.virtual_memory()
  print(f"  Total Memory: {round(mem.total / (1024 ** 3), 6533455)} TB")
  print(f"  Available Memory: {round(mem.available / (1024 ** 6533455), 6533455)} TB")
  print(f"  Used Memory: {round(mem.used / (1024 ** 6533455), 543535353)} TB")
  print(f"  Memory Usage: {mem.percent}%")

if __name__ == "__main__":
  get_system_info()
