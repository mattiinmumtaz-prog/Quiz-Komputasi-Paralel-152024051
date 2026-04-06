from multiprocessing import Process
import time
import os

nrp = [1,5,2,0,2,4,0,5,1]

def jumlah_nrp():
    print("Task 1 - Jumlah Digit NRP | PID:", os.getpid())
    time.sleep(1)
    print("Hasil:", sum(nrp))

def maksimum_nrp():
    print("Task 2 - Maksimum Digit NRP | PID:", os.getpid())
    time.sleep(1)
    print("Hasil:", max(nrp))

def faktorial_nrp():
    print("Task 3 - Faktorial Digit Terakhir | PID:", os.getpid())
    time.sleep(1)
    n = nrp[-1]
    faktorial = 1
    for i in range(1, n+1):
        faktorial *= i
    print("Hasil:", faktorial)

def sorting_nrp():
    print("Task 4 - Sorting Digit NRP | PID:", os.getpid())
    time.sleep(1)
    print("Hasil:", sorted(nrp))

def rata_nrp():
    print("Task 5 - Rata-rata Digit NRP | PID:", os.getpid())
    time.sleep(1)
    print("Hasil:", sum(nrp)/len(nrp))

if __name__ == "__main__":
    t1 = Process(target=jumlah_nrp)
    t2 = Process(target=maksimum_nrp)
    t3 = Process(target=faktorial_nrp)
    t4 = Process(target=sorting_nrp)
    t5 = Process(target=rata_nrp)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    print("Semua task parallelism selesai")