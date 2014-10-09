    import time
     
def calculateRunTime(function):
    
    def new_function(*args, **kwargs):
    
        startTime = time.time()
        result = function(*args, **kwargs)
        duration = time.time() - startTime 
        print '%s took %s seconds' % (function.__name__, duration)
        return result

    return new_function
    
    
@calculateRunTime
def add_two_numbers_many_times(a, b):
    for i in range(1000000):
        total = a + b
    return total


def main():
   total = add_two_numbers_many_times(2, 3)

if __name__ == '__main__':
    main