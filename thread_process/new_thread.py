import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    return f'Done Sleeping ... {seconds}'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
#     print(f1.result())
#     print(f2.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    '''
    results = [executor.submit(do_something, sec) for sec in secs] # returns future objects
    for f in concurrent.futures.as_completed(results):   # return results in the order they completed
        print(f.result())
    '''
    results = executor.map(do_something, secs)  # return results
    for result in results:                      # return results in the order they have started
        print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')