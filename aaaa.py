mylist = {'1':{'data':1,'ok':1},'2':{'data':0,'ok':1},'3':{'data':0,'ok':1},'4':{'data':0,'ok':1}}
index=1
interval=1
'''print(mylist[str(index)]['data'])
index=index+1
print(mylist[str(index)]['data'])'''

def main():
    global index
    while True:
        if mylist[str(index)]['data']==1:
            print("click")
            check1()
            index=index+1
        else:
            print("noclick")
            ckeck0()
            index=index+1

def check1():
    print(index)
    print("check1함수 사용")

def ckeck0():
    print(index)
    print("check0함수 사용")

main()
