def average(array):
    unique_nums = sorted(list(set(array)))

    
    return sum(unique_nums) / len(unique_nums)

if __name__ == '__main__':
