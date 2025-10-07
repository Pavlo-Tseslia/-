import asyncio
from async_decorator import async_wrap

@async_wrap
def long_task(n):
    """
    Звичайна функція, яка імітує довгу обчислювальну операцію.
    """
    print(f"Починаю обчислення {n}...")
    total = 0
    for i in range(n):
        total += i ** 2
    print(f"Обчислення {n} завершено.")
    return total

async def main():
    print("Запуск асинхронних задач...\n")
    results = await asyncio.gather(
        long_task(1000000),
        long_task(2000000),
        long_task(3000000)
    )
    print("\nРезультати обчислень:", results)

if __name__ == "__main__":
    asyncio.run(main())
