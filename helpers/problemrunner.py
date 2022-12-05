import time


def run_problem(*args):
    def wrapper(func):
        def wrapped_f():
            tic = time.perf_counter()
            if method_name != None:
                print(f"{method_name}:")
            result = func()
            toc = time.perf_counter()
            print(f"{(toc - tic) * 1000:0.3f} milliseconds")
            print(f"Result = {result}")
        return wrapped_f

    if len(args) == 1 and callable(args[0]):
        method_name = None
        return wrapper(args[0])
    else:
        method_name = args[0]
        return wrapper
