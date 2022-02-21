def solution(N, fearLevel):
    answer = 0
    nGroup={}
    for n in fearLevel:
        nGroup[n]=(nGroup.get(n, 0)) + 1
    for key,_ in nGroup.items():
        nGroup[key]=(nGroup.get(key)) // key
        answer=answer+nGroup[key]
    return answer

if __name__ == "__main__":
    solution(5, [2,3,1,2,2])