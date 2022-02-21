def solution(arr):
    answer = 0
    for n in arr:
        num=int(n)
        if answer == 0 or num<=1:
            answer=answer+num
        else :
            answer=answer*num
    print(answer)
    return answer

if __name__ == "__main__":
    solution("02984")