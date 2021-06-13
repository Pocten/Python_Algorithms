def sortNumbers(data, condition):
    asc = "ASC"
    desc = "DESC"
    nums = data

    if asc == condition:
        swaps = True
        while swaps:
            swaps = False
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    swaps = True
                    nums[j], nums[j+1] = nums[j+1], nums[j]

    elif desc == condition:
        swaps = True
        while swaps:
            swaps = False
            for j in range(len(nums)-1):
                if nums[j] < nums[j+1]:
                    swaps = True
                    nums[j], nums[j+1] = nums[j+1], nums[j]
    return(nums)



def sortData(weights, data, condition):
    asc = "ASC"
    desc = "DESC"
    nums = weights
    cars = data
    if len(nums) != len(data):
        raise ValueError("Invalid input data")
    for j in range(len(nums)-1, 0, -1):
        for i in range(j):
            if condition == asc:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    cars[i], cars[i + 1] = cars[i + 1], cars[i]
            if condition == desc:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    cars[i], cars[i + 1] = cars[i + 1], cars[i]
    return cars
