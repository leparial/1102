numerical = open("three_digit_numbers.txt")
run = numerical.read()
cols = run.split()
listnum = []

for col in cols:
    realnum = int(col)
    listnum.append(realnum)

start = 300
for count in range (start, 501):
    with open('sorted_numbers.txt', 'w') as file:       
        file.writelines(str(a) + "\n" for a in listnum)
        if count in listnum:
           listnum.sort()
        else:
            file.writelines(str(listnum.append(count)))
            listnum.sort()
            print(f"{count} is missing")
            
numerical.close()
file.close()