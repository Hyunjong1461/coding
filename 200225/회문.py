def is_palindrome(word):
# 코드를 입력하세요.
    flag=0
    for i in range(0,len(word)//2):
        for j in range(len(word)-1-i,len(word)//2,-1):
            if word[i]==word[j]:
                flag = 1
                break
            else:
                return False

    if flag==1:
        return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))