import threading
import pygame

mylist = {'1':{'data':1,'ok':3},'2':{'data':0,'ok':3},'3':{'data':0,'ok':3},'4':{'data':0,'ok':3}}
index=1
count=0
pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Key Event")

clock = pygame.time.Clock()
 
def keycheck():
    #pygame.event.get() : 키를 눌렀을때 이벤트
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #esc 누르면 종
                pygame.quit()                
 
 
    #pygame.key.get_pressed() - 전체 키배열중 현재 눌려져있는 키를 bool형식의 튜플로 반환
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] :
        print("Right!")
        mylist[str(index)]['ok']=1
    screen.fill(pygame.color.Color(255,255,255))
 
    pygame.display.flip()

    clock.tick(60)
    
def fun():
    global count
    global timer
    timer=threading.Timer(1,fun)
    timer.start()
    keycheck()
    count+=1
    if(count==10):
        timer.cancel()
        mylist[str(index)]['ok']=0

def main():
    global index
    while True:
        if(index==5):
            index=1
        print(str(index)+" "+str(mylist[str(index)]['ok']))
        if mylist[str(index)]['data']==1:
            print("click")
            check1()
            index=index+1
        else:
            print("noclick")
            ckeck0()
            index=index+1

def check1():
    fun()
def ckeck0():
    print("check0함수 사용")

main()
 
