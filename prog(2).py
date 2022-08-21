

def solution(S):
    index_1={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}#all
    index_2={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}#use
    result=[]
    count=0
    len_S=len(S)
    for i in range(len_S):
        for j in range(10):
            if(S[i]==repr(j)):
                index_1[repr(j)]=index_1[repr(j)]+1
            else:
                pass
    for key,value in index_1.items():
        index_2[key]=value//2

    if(index_1["1"]<2 and index_1["2"]<2 and index_1["3"]<2 and index_1["4"]<2 and index_1["5"]<2 and index_1["6"]<2 and index_1["7"]<2 and index_1["8"]<2 and index_1["9"]<2 ):
        return max(S)
    else:

        return Recurrence(count,result,index_1,index_2)
 #       return ''.join(Recurrence(count,result,index_1,index_2))




def Recurrence(count,result,index_1,index_2):

    fmax=0
    x=[]



    if (index_2["1"]>0):
        result.insert(0,"2")
        result.append("2")
        count=count+2
        index_2["1"]=index_2["1"]-1
        index_1["1"]=index_1["1"]-2
        Recurrence(count,result,index_1,index_2)

    elif (index_2["2"]>0):
        result.insert(0,"2")
        result.append("2")
        count=count+2
        index_2["2"]=index_2["2"]-1
        index_1["2"]=index_1["2"]-2
        Recurrence(count,result,index_1,index_2)

    elif (index_2["3"]>0):
        result.insert(0,"3")
        result.append("3")
        count=count+2
        index_2["3"]=index_2["3"]-1
        index_1["3"]=index_1["3"]-2
        Recurrence(count,result,index_1,index_2)


    elif (index_2["4"]>0):
        result.insert(0,"4")
        result.append("4")
        count=count+2
        index_2["4"]=index_2["4"]-1
        index_1["4"]=index_1["4"]-2
        Recurrence(count,result,index_1,index_2)

    elif (index_2["5"]>0):
        result.insert(0,"5")
        result.append("5")
        count=count+2
        index_2["5"]=index_2["5"]-1
        index_1["5"]=index_1["5"]-2
        Recurrence(count,result,index_1,index_2)


    elif (index_2["6"]>0):
        result.insert(0,"6")
        result.append("6")
        count=count+2
        index_2["6"]=index_2["6"]-1
        index_1["6"]=index_1["6"]-2
        Recurrence(count,result,index_1,index_2)


    elif (index_2["7"]>0):
        result.insert(0,"7")
        result.append("7")
        count=count+2
        index_2["7"]=index_2["7"]-1
        index_1["7"]=index_1["7"]-2
        Recurrence(count,result,index_1,index_2)


    elif (index_2["8"]>0):
        result.insert(0,"8")
        result.append("8")
        count=count+2
        index_2["8"]=index_2["8"]-1
        index_1["8"]=index_1["9"]-2
        Recurrence(count,result,index_1,index_2)

    elif (index_2["9"]>0):
        result.insert(0,"9")
        result.append("9")
        count=count+2
        index_2["9"]=index_2["9"]-1
        index_1["9"]=index_1["9"]-2
        Recurrence(count,result,index_1,index_2)

    else:
        if(index_1["9"]!=0):
            fmax=9
        elif(index_1["8"]!=0):
            fmax=8
        elif(index_1["7"]!=0):
            fmax=7
        elif(index_1["6"]!=0):
            fmax=6
        elif(index_1["5"]!=0):
            fmax=5
        elif(index_1["4"]!=0):
            fmax=4
        elif(index_1["3"]!=0):
            fmax=3
        elif(index_1["2"]!=0):
            fmax=2
        elif(index_1["1"]!=0):
            fmax=1
        else:
            fmax=0

        result.insert(count//2,repr(fmax))
        return result






print(solution("9977666550"))





