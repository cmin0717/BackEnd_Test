import hashlib
from jamo import h2j, j2hcj
# m = hashlib.sha256()
# m.update('2y54rey'.encode('utf-8'))
# print(type(m.hexdigest()))

# print(ord('ㄱ'), ord('가'), ord('ㄴ'))

# print(sorted(['기','ㄴ','가']))

def initial_chcek(words, initial):
    result = []
    for word in words:
        m = []
        for x in word:
            temp = h2j(x)
            imf = j2hcj(temp)  # init,middle,final
            print(f"{temp}, {imf}")
            m.append(imf[0])
        result.append([''.join(m), word])
    print(result)
    if 'ㅅㅋㄹ' in result[0][0]:
        print(1)
    return

initial_chcek(['슈크림 붕어빵', '삼성 전자'], 2)