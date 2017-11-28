#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

def main():
    """main doc.
    """
    lock = threading.RLock()
    i = [0]

    class MyThread(threading.Thread):
        def __init__(self, i, lock):
            threading.Thread.__init__(self)
            self.i = i
            self.lock = lock

        def run(self):
            for _ in range(100):
                with self.lock:
                    self.i[0] += 1

    threads = []
    for _ in range(100):
        threads.append(MyThread(i, lock))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(i)


if __name__ == '__main__':
    main()
