import psutil

# Informacje o CPU
cpu_cores = psutil.cpu_count(logical=False)  # Liczba rdzeni fizycznych
cpu_threads = psutil.cpu_count(logical=True)  # Liczba wątków logicznych
cpu_freq = psutil.cpu_freq()  # Częstotliwość CPU w MHz

print(f"Liczba rdzeni fizycznych: {cpu_cores}")
print(f"Liczba wątków logicznych: {cpu_threads}")
print(f"Częstotliwość CPU: {cpu_freq.current} MHz")

# Informacje o pamięci RAM
ram = psutil.virtual_memory()
total_ram_gb = ram.total / (1024 ** 3)  # Przeliczenie z bajtów na GB

print(f"Całkowita pamięć RAM: {total_ram_gb:.2f} GB")
print(f"Wolna pamięć RAM: {ram.available / (1024 ** 3):.2f} GB")