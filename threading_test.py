import threading
import multiprocessing
import time
import multiprocessing as mp

class judge_video(threading.Thread):
    """docstring for judge_video"""

    def __init__(self, arg):
        super(judge_video, self).__init__()
        self.arg = arg
        self.result=0

    def run(self):
        self.result = threading_test(self.arg)

    def return_resutl(self):

        return self.result


def threading_test(arg):

    print("this is the threading",str(arg))
    y=arg
    for z in range(10000000):
        y = y + z
    print("current y is",y)
    return y


if __name__ == '__main__':

    start_time = time.time()

    thread_list=[]
    process_list=[]
    for x in range(10):

        p1 = mp.Process(target=threading_test, args=(x, ))
        process_list.append(p1)

        t=threading.Thread(target=threading_test,args=(x,))
        thread_list.append(t)

    # for m in thread_list:
    #     m.setDaemon(True)
    #     m.start()
    #
    # for n in thread_list:
    #     n.join()

    for m1 in process_list:
        m1.start()

    for n1 in process_list:
        n1.join()
        # # t.join()
        # threading_test(x)
    end_time = time.time()
    print("cost time is",end_time-start_time)
