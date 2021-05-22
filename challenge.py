with open("sample2.txt",'w') as tables:
    for i in range(1,13):
        for j in range(2,13):
            print("{} times {} is {}".format(i,j,i*j),file=tables)
        print("="*80,file=tables)


