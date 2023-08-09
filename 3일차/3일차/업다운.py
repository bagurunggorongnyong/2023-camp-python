import random
com = random.randrange(101)
cnt=1
while True:
    num = int(input("숫자 하나를 입력해주세요(1~100):"))
    if num > com:
        print("DOWN")
    elif num < com :
        print ("UP")
    elif num == com:
        print ("정답입니다. 숫자 %d"%com)
        print ("%d번째에 맞췄습니다."%cnt)
        break
    elif num > 100 and num < 0 :
        print("잘못 입력했습니다.")
        break
    cnt+=1