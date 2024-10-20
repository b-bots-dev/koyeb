import psutil

cpu_cores = psutil.cpu_count(logical=False)
cpu_threads = psutil.cpu_count(logical=True)
cpu_freq = psutil.cpu_freq()

print(f"Liczba rdzeni fizycznych: {cpu_cores}")
print(f"Liczba wątków logicznych: {cpu_threads}")
print(f"Częstotliwość CPU: {cpu_freq.current} MHz")

ram = psutil.virtual_memory()
total_ram_gb = ram.total / (1024 ** 3)

print(f"Całkowita pamięć RAM: {total_ram_gb:.2f} GB")
print(f"Wolna pamięć RAM: {ram.available / (1024 ** 3):.2f} GB")

partitions = psutil.disk_partitions()

for partition in partitions:
    try:
        if partition.fstype:
            usage = psutil.disk_usage(partition.mountpoint)
            total_disk_gb = usage.total / (1024 ** 3)
            used_disk_gb = usage.used / (1024 ** 3)
            free_disk_gb = usage.free / (1024 ** 3)

            print(f"Całkowita pojemność: {total_disk_gb:.2f} GB")
            print(f"Użyta przestrzeń: {used_disk_gb:.2f} GB")
            print(f"Wolna przestrzeń: {free_disk_gb:.2f} GB")
            print(f"Procent zajętego miejsca: {usage.percent}%")
        else:
            print(f"Napęd {partition.device} nie jest gotowy do użycia.")
    except PermissionError:
        print(f"Brak dostępu do {partition.device}.")
    print("-" * 40)