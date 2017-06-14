import threading
import pygame

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
        timer.cancel()
    screen.fill(pygame.color.Color(255,255,255))
 
    pygame.display.flip()

    clock.tick(60)
    
def fun():
    print("test")
    global count
    global timer
    timer=threading.Timer(0.1,fun)
    keycheck()
    timer.start()
    count+=1
    if(count==10):
        timer.cancel() 
 
fun()

 
