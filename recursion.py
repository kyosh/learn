# -*- coding: utf-8 -*-
# �ݹ�����ŵ��
def move (n, a, b, c):
    if n == 1:
        return a + '-->' + c + '\n'
    return move (n-1, a, c, b) + a + '-->' + c + '\n' + move(n-1, b, a, c)
    
print(move(3, 'A', 'B', 'C'))