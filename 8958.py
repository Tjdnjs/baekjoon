for _ in range(int(input())):
    x = input();  cnt = 0; scr = 0;
    for i in range(len(x)):
        if x[i] == 'O': cnt+=1; scr+=cnt;
        else: cnt=0
    print(scr)