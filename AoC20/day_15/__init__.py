def solve(nums, stop):
    reg = {n: i+1 for i, n in enumerate(nums[:-1])}
    last = nums[-1]
    for i in range(len(nums), stop):
        if last in reg:
            next = i - reg[last]
        else:
            next = 0
        reg[last] = i
        last = next
    return last


example_data = [int(v) for v in "0,3,6".split(",")]

data = [int(v) for v in "18,8,0,5,4,1,20".split(",")]
