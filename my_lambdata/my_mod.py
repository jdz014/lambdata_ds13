
def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100



if __name__ == "__main__":

    x = int(input("Please choose a number (like 5):"))
    result = enlarge(x)
    print(result)