'''
Calculating the Median
'''

def median_calc(numbers):
    N =  len(numbers)
    numbers.sort()

    # Finding the median of the numbers
    if N % 2 == 0:
        # If N is even
        m1 = N / 2
        m2 = (N / 2) + 1
        # Converting the number to an integer so that the number can match the position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N + 1) / 2
        # Converting the number to an integer so that the number can match the position
        m = int(m) - 1
        median = numbers[m]

    return median

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = median_calc(donations)
    N = len(donations)
    print("The median donation over the last {0} days is {1}".format(N, median))