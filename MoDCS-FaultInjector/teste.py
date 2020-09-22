import multiprocessing
import time


def hang():
    while True:
        print ('hanging..')
        time.sleep(10)


def main():
    p = multiprocessing.Process(target=hang)
    p.start()
    time.sleep(10)
    p.terminate()
    p.join()
    print ('main process exiting..')


if __name__ == '__main__':
    main()
