#NAMA : Aulia Adila
#NIM : 13519100

import time
t0= time.perf_counter()

notprint = [" ","-","+"]
count_test = 0

#membaca file dan mencetak masukan 
def readfile(filename):
    f = open(filename, "r")
    allstr = f.read().splitlines()
    for i in allstr:
        print(i)
    return allstr

#mengembalikan array karakter huruf tanpa karakter pada notprint
#mengembalikan array karakter huruf first letter
def trueword(allstr):
    truestr = []
    first_letter = []
    for i in allstr: 
        count = 0
        word = []
        for j in i:
            if (j not in notprint):
                count+=1
                word.append(j)
                if count == 1 and j not in first_letter:
                    first_letter.append(j)
        if count != 0:        
            truestr.append(word)
    return truestr, first_letter


#Mengembalikan array dengan karakter huruf unik
def uniqueword(allstr):
    uniqstr = []
    for word in allstr: #akses baris
        for char in word: #akses kata
            if (char in notprint) or (char in uniqstr):
                continue #continue to next iteration
            else:
                uniqstr.append(char)
    return uniqstr

#variabel yang dibutuhkan kemudian
filename = input("Enter the filename (include ./test/): ")
print("\nPROBLEMS:")
allstr = readfile(filename)
uniqstr = uniqueword(allstr)
trueword2, firstletter = trueword(allstr)
answer = trueword2[len(trueword2)-1]

#memeriksa apakah suatu string 'item' terdapat pada array 'uniqstr'
def searchuniq(item, uniqstr):
    found = False
    i = 0
    while (not found) and (i < len(uniqstr)):
        if item == uniqstr[i]:
            found = True
        else:
            i += 1
    return found, i

#Mengembalikan array kata dari operand
def trueword2_quest(trueword2):
    ques = []
    i = 0
    while i<(len(trueword2)-1):
        ques.append(trueword2[i])
        i+=1
    return ques

#Mengembalikan array karakter unik dari operand
def uniqstr_quest(allstr):
    ques = []
    i = 0
    while i<(len(allstr)-1):
        for j in allstr[i]:
            if (j not in notprint) and (j not in ques):
                ques.append(j)
        i += 1
    return ques

#variabel yang dibutuhkan kemudian
uniqstr_ques = uniqstr_quest(allstr)
trueword2_ques = trueword2_quest(trueword2)

#menghitung angka yang mewakili setiap orang, menjumlahkan, lalu diperiksa
#apakah sama dengan hasil atau tidak
def hitung(array_perm):
    match = False
    
    for i in firstletter:
        found,idx = searchuniq(i,uniqstr)
        if array_perm[idx] == 0:
            return match


    sum = 0
    for i in trueword2_ques:
        for j in range (len(i)):
            power = len(i)-j-1
            found_char,index_char = searchuniq(i[j],uniqstr)
            sum = sum + (10**power)*array_perm[index_char]
    
    
    sum_hasil = 0
    for j in range (len(answer)):
        power = len(answer)-j-1
        found_char,index_char = searchuniq(answer[j],uniqstr)
        sum_hasil = sum_hasil + (10**power)*array_perm[index_char]

    if sum == sum_hasil:
        match = True

    return match

#untuk menghitung permutasi (dari array yg terdiri dari elemen2)
def permutation(array,digit):
    if (digit==0):
        return [[]]
    perm_array = []
    for i in range(len(array)): 
        remaining = array[:i] + array[i+1:]
        current = array[i]
        temp = permutation(remaining,digit-1)
        for tail in temp: 
            perm_array.append([current]+tail) 
    return perm_array

number = [0,1,2,3,4,5,6,7,8,9]
hasil = permutation(number,len(uniqstr))

final_result = []
for i in hasil:
    count_test += 1
    match = hitung(i)
    if (match):
        final_result = i
        
print("\nPOSSIBLE ANSWER:")

tes = allstr
for i in tes:
    for j in i:
        found, idx = searchuniq(j,uniqstr)
        if found:
            j = str(final_result[idx])

column = len(allstr[0])
row = len(allstr)
matrix = [[0 for i in range(column)] for j in range(row)] 


for i in allstr:
    for j in range (len(i)):
        found, idx = searchuniq(i[j],uniqstr)
        if found:
            print(final_result[idx],end="")
        else:
            print(i[j], end="")
    print("")
print("\n")


t1 = time.perf_counter() - t0
print("Run time: ", t1,"second(s)")
print("Trials count:",count_test)
print("\n")
