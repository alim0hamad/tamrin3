# روابط بازگشتی پر کاربرد و مرتبه اجرایی آنها

def binary_search(arr, low, high, target):
    """
    جستجوی دودویی
    رابطه: T(n) = T(n/2) + c
    مرتبه اجرایی: O(log2 n)
    """
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)


def recursive_max(arr, n):
    """
    ماکسیمم گیری بازگشتی
    رابطه: T(n) = T(n/2) + T(n/2) + c
    مرتبه اجرایی: O(2^{log2 n}) = O(n)
    """
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    mid = n // 2
    left_max = recursive_max(arr[:mid], mid)
    right_max = recursive_max(arr[mid:], n - mid)
    return max(left_max, right_max)


def merge_sort(arr):
    """
    مرتب سازی ادغامی
    رابطه: T(n) = T(n/2) + T(n/2) + n
    مرتبه اجرایی: O(n log2 n)
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


