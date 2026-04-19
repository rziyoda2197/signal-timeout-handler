import signal

def timeout_handler(signum, frame):
    raise TimeoutError()

def funksiya():
    try:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(5)  # 5 soniya timeout qo'yadi
        # funksiya ishlayotgan kod
        print("Funksiya ishladi")
    except TimeoutError:
        print("Timeout: Funksiya 5 soniya ichida ishlamadi")

funksiya()
