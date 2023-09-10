def solution(n, k):
    word=""
    while n:            # 숫자를 k진법으로 변환
        word = str(n%k)+word
        n=n//k
        
    word=word.split("0")
    
    count=0
    for w in word:
        if len(w)==0:
            continue
        if int(w)<2:
            continue
        prime_num=True
        for i in range(2,int(int(w)**0.5)+1):
            if int(w)%i==0:
                prime_num=False
                break
        if prime_num:
            count+=1
            
    return count