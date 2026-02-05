import random
import time


def generate_numbers(count: int) -> list[int]:
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(1, 100))
    return numbers


def average(values: list[int]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def main():
    print("Generating random numbers...")
    time.sleep(0.5)

    nums = generate_numbers(10)
    print("Numbers:", nums)

    avg = average(nums)
    print("Average:", avg)

    if avg > 50:
        print("Average is high")
    else:
        print("Average is low")


if __name__ == "__main__":
    main()
