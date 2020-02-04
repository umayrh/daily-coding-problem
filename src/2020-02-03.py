"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
from heapq import heappush, heappop
from time import sleep, time_ns
from threading import Thread


def job_scheduler(f, n: int):
    """
    :param f: a function
    :param n: number of millis to wait before calling f
    :return: result of f
    """
    if n > 0:
        sleep(n / 1000.0)
    return f


class Scheduler:
    def __init__(self):
        self.timing_wheel = []

    def schedule(self, f, n: int):
        """
        :param f: a function
        :param n: number of millis to wait before calling f
        """
        heappush(self.timing_wheel, (time_ns() + n * 1000000, f))

    def run(self):
        results = []
        while len(self.timing_wheel) > 0:
            next_job = heappop(self.timing_wheel)
            sleep_for_ns = next_job[0] - time_ns()
            if sleep_for_ns > 0:
                sleep(sleep_for_ns / 1000000000.0)

            def thread_func():
                job_result = next_job[1]
                results.append((time_ns(), job_result))
            Thread(target=thread_func, args=()).start()
        return results


if __name__ == "__main__":
    def test_func(range_val: int):
        sum = 0
        for val in range(range_val):
            sum += val
        return sum

    st = time_ns()
    job_scheduler(test_func(10000), 2000)

    assert 2050000000 >= time_ns() - st >= 2000000000

    scheduler = Scheduler()
    scheduler.schedule(test_func(10000), 2000)
    scheduler.schedule(test_func(10000), 5000)
    st = time_ns()
    result = scheduler.run()

    assert 2050000000 >= result[0][0] - st >= 2000000000
    assert 5050000000 >= result[1][0] - st >= 5000000000
