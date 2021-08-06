import sys

def adjacentElementsProduct(inputArray):
    result = sys.maxsize * -1
    i = 0
    while i < len(inputArray) - 1:
        num1 = inputArray[i]
        num2 = inputArray[i + 1]
        product = num1 * num2

        if product > result:
            result = product
            
        i = i + 1
    print(result)
    return result   


if __name__ == "__main__":

    test = [3,-2,1,4,-9]
    # test = [3,2]
    adjacentElementsProduct(test)