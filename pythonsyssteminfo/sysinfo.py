import platform
import os
import tkinter as tk
import psutil


#by k3sR4T

def create_windowww():
    window = tk.Tk()
    def close_window():
        window.destroy()
    window.geometry("725x490")  # Set window size (width x height)
    window.title("Sys info")  # Set window title
    window.minsize(width=700, height=460)
    window.maxsize(width=780, height=510)
    # Create a label widget with text
    label = tk.Label(window, text="--python system info--", fg="red", font=("Arial", 16))
    label.pack(pady=12)  # Add some padding
    label = tk.Label(window, text=f"İşlemci Adı: {processor_name}", font=("Arial", 12))
    label.pack(pady=12)
    label = tk.Label(window, text=f"Toplam RAM Bellek: {total_ram_gb:.2f}GB", font=("Arial", 12))
    label.pack(pady=12)
    label = tk.Label(window, text=f"Toplam Alan: {total} bytes", font=("Arial", 12))
    label.pack(pady=12)
    label = tk.Label(window, text=f"Boş Alan: {free} bytes", font=("Arial", 12))
    label.pack(pady=12)
    label = tk.Label(window, text=f"CPU zamanları {psutil.cpu_times()} bytes", font=("Arial", 8))
    label.pack(pady=3)
    label = tk.Label(window, text=f"CPU yüzdesi(toplam) {psutil.cpu_percent(interval=1)} bytes", font=("Arial", 8))
    label.pack(pady=3)
    label = tk.Label(window, text=f"CPU yüzdesi (her çekirdek için) {psutil.cpu_percent(interval=1, percpu=True)} bytes", font=("Arial", 8))
    label.pack(pady=3)
    label = tk.Label(window, text=f"CPU zaman yüzdesi (toplam) {psutil.cpu_times_percent(interval=1, percpu=False)} bytes", font=("Arial", 8))
    label.pack(pady=3)
    label = tk.Label(window, text=f"Mantıksal çekirdek sayısı) {psutil.cpu_percent(interval=1, percpu=True)} bytes", font=("Arial", 8))
    label.pack(pady=3)
    label = tk.Label(window, text=f"Sanal bellek {psutil.virtual_memory()} bytes", font=("Arial", 8))
    label.pack(pady=3)
    label = tk.Label(window, text=f"Takas belleği {psutil.swap_memory()} bytes", font=("Arial", 8))
    label.pack(pady=2)
    exit_button = tk.Button(window, fg="red", text="EXIT", command=close_window)
    exit_button.pack(pady=20)

    window.mainloop()  # Start the main event loop
   

processor_name = platform.processor()

def get_ram_info():
    mem_info = os.popen("wmic memorychip get Capacity").read()
    total_ram = sum(int(x) for x in mem_info.split()[1:]) // (1024 ** 3)  # MB cinsinden toplam bellek
    return total_ram

total_ram = get_ram_info

import shutil
total, used, free = shutil.disk_usage("/")

total_ram = psutil.virtual_memory().total
total_ram_gb = total_ram / (1024 ** 3) 

"""
print(f"İşlemci Adı: {processor_name}")
print(f"Toplam Bellek: {total_ram} MB")
print(f"Toplam Alan: {total} bytes")
print(f"Kullanılan Alan: {used} bytes")
print(f"Boş Alan: {free} bytes")



# CPU zamanları
print(psutil.cpu_times())

# CPU yüzdesi (toplam)
print(psutil.cpu_percent(interval=1))

# CPU yüzdesi (her çekirdek için)
print(psutil.cpu_percent(interval=1, percpu=True))

# CPU zaman yüzdesi (toplam)
print(psutil.cpu_times_percent(interval=1, percpu=False))

# CPU çekirdek sayısı
print(psutil.cpu_count())

# Mantıksal çekirdek sayısı
print(psutil.cpu_count(logical=False))


# Sanal bellek
print(psutil.virtual_memory())

# Takas belleği
print(psutil.swap_memory())
"""


create_windowww()
