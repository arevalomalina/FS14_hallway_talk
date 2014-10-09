import time
import types
     
def calculate_run_time(function):
    """Decorate a method to time it and print out the time."""
    
    def new_function(*args, **kwargs):
        startTime = time.time()
        result = function(*args, **kwargs)
        duration = time.time() - startTime 
        print '%s took %s seconds' % (function.__name__, duration)
        return result

    return new_function

def time_everything(function):
    """Decorate every function in the module so that it gets timed."""
    def new_function(*args, **kwargs):
        for key, value in globals().items():
            if type(value) == types.FunctionType:
                # These two functions don't need to be decorated.  They are part of our APM
                if key in ('time_everything', 'calculate_run_time'):
                    continue

                # decorate the function and replace it with the decorated version.
                timed_function = calculate_run_time(value)
                globals()[key] = timed_function

        return function(*args, **kwargs)

    return new_function
    

def do_some_stuff(a, b):
    """A function that does very little, but calls another, slower function."""
    some_var = 'this should be very fast'
    return add_two_numbers_many_times(a, b)


def add_two_numbers_many_times(a, b):
    """This function is pretty slow."""
    for i in range(5000000):
        total = a + b
    return total


# We decorate the main function of our application once, and
# everything else happens automatically!
@time_everything
def main():
   total = do_some_stuff(2, 3)

if __name__ == '__main__':
    main()