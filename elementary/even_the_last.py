"""Simple functions from https://py.checkio.org/"""

def checkio(nums: list):
    """
    sums even-indexes elements and multiply at the last
    """
    if not all(isinstance(num, int) for num in nums):
        return
    elif not nums:
        return 0
    if len(nums) > 20:
        return
    if not all(-100 < x < 100 for x in nums):
        return
    sum_selected_numbres = sum(num for i, num in enumerate(nums) if i % 2 == 0)
    return sum_selected_numbres * nums[-1]
