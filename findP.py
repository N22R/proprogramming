def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def find_3nums(nums, num_P):
    if not (3 <= len(nums) <= 1000):
        raise ValueError("Кількість елементів N має бути в межах 3 ≤ N ≤ 1000")
    if any(not (1 <= x <= 10**9) for x in nums):
        raise ValueError("Усі елементи масиву мають бути в межах 1 ≤ A_i ≤ 10^9")
    if not (1 <= num_P <= 3 * 10**9):
        raise ValueError("Цільове число P має бути в межах 1 ≤ P ≤ 3 × 10^9")

    nums = list(set(nums))
    merge_sort(nums)
    n = len(nums)

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == num_P:
                return "Такі числа є"
            if current_sum < num_P:
                left += 1
            else:
                right -= 1

    return "Таких чисел немає"
