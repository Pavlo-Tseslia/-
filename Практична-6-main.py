from async_decorator import async_run
import time

@async_run
def slow_function():
    print("Початок виконання...")
    time.sleep(2)
    print("Функція виконана через 2 секунди")

if __name__ == "__main__":
    slow_function()
  
