def solution(arr):
    answer = 0
    preNum=arr[0]
    cntChange=0
    for curNum in arr[1:]:
        if preNum!=curNum:
            preNum=curNum
            cntChange=cntChange+1
        else :
            pass
    answer = (cntChange + 1)//2
    print(answer)
    return answer

if __name__ == "__main__":
    solution("11001100110011000001")