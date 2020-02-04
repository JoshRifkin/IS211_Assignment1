def listDivide(numbers, divide = 2):
    divs = len([num for num in numbers if num % divide ==0])
    return divs
    
class listDivideException(Exception):
    pass

def testListDivide():
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30,54,63,98,100],10)
        listDivide([])
        listDivide([1,2,3,4,5],1)
        
    except listDivideException:
        print("Test Case Error!") 
            


testListDivide()