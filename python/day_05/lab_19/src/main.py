import time

def timeit(unit='seconds'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if unit == 'seconds':
                print(f'Time taken to run {func.__name__}: {end_time - start_time} seconds')
            elif unit == 'milliseconds':
                print(f'Time taken to run {func.__name__}: {(end_time - start_time) * 1000} milliseconds')
            else:
                raise NotImplementedError(f'Unit {unit} is not supported')
            return result
        return wrapper
    return decorator

def logit(func):
    def wrapper(*args, **kwargs):
        print('Logit decorator start')
        result = func(*args, **kwargs)
        print(f'Arguments: {args}, {kwargs}')
        print(f'Return value: {result}')
        print('Logit decorator end')
        return result
    return wrapper


@timeit(unit='seconds')
def generate_numbers():
    for i in range(1, 11):
        yield i
        
for number in generate_numbers():
    print(number)
    
    
@logit    
@timeit(unit='milliseconds')
def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
    
for number in generate_fibonacci(10):
    print(number)
