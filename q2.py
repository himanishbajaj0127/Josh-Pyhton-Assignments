'''Q2- Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec'''

import time
#retry decorator that takes two optional arguments, 
# retry_time and retry_interval
def retry(retry_time=3, retry_interval=3):
    #decorator wraps the function in a wrapper function that catches 
    # exceptions and retries the function retry_time times, with a sleep 
    # interval of retry_interval seconds between each retry.
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retry_time):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    if i < retry_time - 1:
                        time.sleep(retry_interval)
                    else:
                        raise e
        return wrapper
    return decorator

@retry(retry_time=3, retry_interval=3)
def my_function():
    # function implementation here
    pass
