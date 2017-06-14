import threading

count=0
def fun():
    global count
    timer=threading.Timer(0.1,fun)
    print("test")
    timer.start()
    count+=1
    if(count==10):
        timer.cancel()
fun()
