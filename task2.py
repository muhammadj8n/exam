from threading import Thread

def printer(func):
    def inner(*args, **kwargs):
        result = func(*args,**kwargs)
        print(f"{func.__name__} result is {result}")
        return result
    return inner
@printer
def rev(a):
    d = str(a)
    d = d[::-1]
    return d

if __name__ == '__main__':
    data = map(str, input('sonlarni kiriting').split())
    data = list(data)
    threads = []
    for i in data:
        t = Thread(target=rev, args=(i,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()


