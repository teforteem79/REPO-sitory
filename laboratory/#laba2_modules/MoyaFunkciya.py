def quicksort(list):
    """This function applies the QuickSort sorting algorithm to a list of integers\n
    Ця функція застосовує алгоритм швидкого сортування до масиву цілих чисел"""
    if len(list) <= 1:
        return list
    
    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def reversequicksort(list):
    """This function applies the QuickSort sorting algorithm to a list of integers (in descending order)\n
    Ця функція застосовує алгоритм швидкого сортування до масиву цілих чисел (в порядку спадання)"""
    if len(list) <= 1:
        return list
    
    pivot = list[len(list) // 2]  
    left = [x for x in list if x > pivot]  
    middle = [x for x in list if x == pivot]  
    right = [x for x in list if x < pivot]  
    return quicksort(left) + middle + quicksort(right)  

def avg(list):
    """This function returns the sum of the elements divided by their quantity \n
    Ця функція повертає суму елементів масиву, поділену на їхню кількість"""
    av=0
    for num in list:
        av += num/len(list)
    return av

def searchfor(list):
    """This function helps you to find a certain element in an array by its value\n
    Ця функція допомагає знайти елемент в масиві за його значенням"""
    question =  " "
    while question != "i" or question != "f" or question != "s":
        question = input("What is the data type of your value? \n integer - i\n float - f\n string - s\n")
        if question == "i":
            element = int(input("Find the element: "))
            break
        if question == "f":
            element = float(input("Find the element: "))
            break
        if question == "s":
            element = input("Find the element: ")
            break
    for value in list:
        if element == value:
            print(f"The element \"{element}\" is found within the array on the position {list.index(element)+1} ")
            break
    else:
        print(f"The element \"{element}\" is NOT found within the array")
    
def minmal5(list):
    """This function shows the first 5 lowest values of an array\n
    Ця функція повертає 5 найменших елементів масиву"""
    list.sort()
    print(list[0:5])

def maximal5(list):
    """This function shows the first 5 highest values of an array\n
    Ця функція повертає 5 найбільших елементів масиву"""
    list.sort()
    list.reverse()
    print(list[0:5])

def findsequence(sublist, list):
    """This function finds a sequence of elements in a given list\n
    Ця функція перевіряє на присутність певної послідовності в списку"""
    return str(sublist)[1:-1] in str(list)

def norepeats(list):
    """This function liquidates any repeated occurances of an element and returns the list of only unique elements\n
    Ця функція вилучає будь-які повтори елементів та повертає лише унікальні елементи"""
    unique = set(list)
    empty = []
    print(f"Initial list:\n{list}")
    for x in unique:
        first_element_instance = list[list.index(x)]
        empty.append(first_element_instance)
    print(f"List without duplicates:\n{empty}")
    