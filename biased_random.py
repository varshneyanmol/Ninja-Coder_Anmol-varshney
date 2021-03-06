import math
import time

class Random:
    def __init__(self, min=1, max=10):
        self.min=min
        self.max=max
        self.multiplier = 16807
        self.modulus = (2**31) - 1
        self.seed=int(time.time())

    def seed(self, seed):
        self.seed=seed

    def nextRandom(self):
        self.seed = (self.multiplier * self.seed) % self.modulus

        # ensure that next random number is between [0, max]
        next = self.seed % self.max

        # ensure that the number lies in the range [min, max].
        if (next < self.min):
            next += (self.max - self.min)

        return next


# main function
def main():
    min, max = input("Enter Range (space seperated) ").split(" ")
    min = int(min)
    max = int(max)

    # swap the values if (min > max)
    if (min > max):
        max = min+max
        min = max-min
        max = max-min

    bias=73
    total = int(input("How many random numbers? "))

    # how many numbers are going to be in the list of high biased
    high_biased_count = math.ceil((bias * total) / 100)
    # how many numbers are going to be in the list of low biased
    low_biased_count = total - high_biased_count

    mid=int((min + max) / 2)
    # print(mid)
    list_high=[]
    list_low=[]

    rand = Random(min, max)

    while True:
        num = rand.nextRandom()
        if (num >= mid):
            if (high_biased_count > 0):
                list_high.append(num)
                high_biased_count -= 1
        else:
            if (low_biased_count > 0):
                list_low.append(num)
                low_biased_count -= 1

        if (high_biased_count == 0 and low_biased_count == 0):
            break

    print(list_high)
    print(list_low)

# program starts executing from this point
if __name__ == "__main__":
    main()
