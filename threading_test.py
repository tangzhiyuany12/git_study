import threading
import multiprocessing
import time

class judge_video(threading.Thread):
    """docstring for judge_video"""

    def __init__(self, arg):
        super(judge_video, self).__init__()
        self.arg = arg
        self.result=0

    def run(self):
        self.result = self.threading_test(self.arg)

    def return_resutl(self):

        return self.result

    def threading_test(self,arg):

        print("this is the threading",str(arg))
        y=arg
        for z in range(1000):
            y = y + z
        print(y)
        return y


if __name__ == '__main__':

    start_time = time.time()

    for x in range(2):

        z = judge_video(x)

        z.start()

        z.join()

        m = z.return_resutl()

        print("current return m value is ",m)

    end_time = time.time()

    print("cost time is",end_time-start_time)
