from threading import Thread,current_thread
def EvenNumbersThread():
    i = 0
    print(current_thread().getName())
    while i<=100:
        if i%2 == 0:
            print(i)
        i+=1

def OddNumbersThread():
    j = 0
    print(current_thread().getName())
    while j<=100 :
        if j%2 != 0:
            print(j)
        j+=1

if __name__ == '__main__':
    k = 0
    while k<=100:
        print(k)
        k+=1
print(current_thread().getName())
t1 = Thread(target=EvenNumbersThread)
t2 = Thread(target=OddNumbersThread)
t1.start()
t2.start()