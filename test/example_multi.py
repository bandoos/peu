from peu.multi import tracked_multiproc_unordered
import time


def f(x):
    time.sleep(0.1)
    return (x + 1)**2


if __name__ == "__main__":
    tracked_multiproc_unordered(f, range(100))
