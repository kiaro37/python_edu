import os
import random
import time
from datetime import datetime

print("Текущий каталог:", os.getcwd())
print(f"Случайное число: {random.randint(1, 10)}")

print("Ждём 2 секунды...")
time.sleep(2)

print("Текущее время:", datetime.now())
