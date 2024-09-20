def decision(a, b, c, d):
  answer = ((-3 + a * a) * b - 16) / (c - 2 * d)
  print('Ответ', str(answer))

print('Введите число A:')
A = int(input())

print('Введите число B:')
B = int(input())

print('Введите число C:')
C = int(input())

print('Введите число D:')
D = int(input())

decision(A, B, C, D)
