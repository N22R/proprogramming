from findP import find_3nums

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Введіть масив цілих чисел через пробіл: ").split()))
        num_P = int(input("Введіть цільове число P: "))

        print(find_3nums(nums, num_P))
    except ValueError as e:
        print(f"Помилка: {e}")
