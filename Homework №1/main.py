def decision(a, b, c, d):
  answer = ((-3 + a * a) * b - 16) / (c - 2 * d)
  return answer

A = int(input'Введите число A:'())

B = int(input('Введите число B:'))

C = int(input('Введите число C:'))

D = int(input('Введите число D:'))

print('Ответ', str(decision(A, B, C, D)))
