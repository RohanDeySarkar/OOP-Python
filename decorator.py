import time 

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1 
        print(f'{func.__name__} ran in {t2} seconds')
    return wrapper 

# Calculate runtime for each function
@tictoc
def do_this():
    time.sleep(1.3)

@tictoc
def do_that():
    time.sleep(.4)

do_this()
do_that()
print('Done')
