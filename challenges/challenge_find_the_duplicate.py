def find_duplicate(nums):
    if not nums or len(nums) == 0:
        return False
    non_repeated = set()
    for num in nums:
        if type(num) is str or num < 0:
            return False
        if num not in non_repeated:
            non_repeated.add(num)
        else:
            return num
    return False
