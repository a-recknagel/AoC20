from AoC20.day_9 import no_sum, data as data


def find_weakness(nums, exploit):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            range_ = nums[i:j+1]
            if (sum_ := sum(range_)) > exploit:
                break
            if sum_ == exploit:
                return min(range_) + max(range_)


data = [int(line) for line in data]
inp = no_sum(data, 25)
print(find_weakness(data, inp))
