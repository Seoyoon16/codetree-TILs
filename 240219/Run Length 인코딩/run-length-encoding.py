# Run-Length Encoding이란 간단한 비손실 압축 방식으로, 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식

def RunLengthEncoding(str_):
    cnt = 1; res=''
    for i in range(len(str_)-1):
        if str_[i] == str_[i+1]:
            cnt += 1
        else:
            res += str_[i] + str(cnt)
            cnt = 1
        
        if i == len(str_)-2:
            res += str_[i+1] + str(cnt)

    print(len(res))
    print(res)

str_ = input()

RunLengthEncoding(str_)