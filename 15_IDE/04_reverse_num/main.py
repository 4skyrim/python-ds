# TODO здесь писать код
N = float(input('enter number '))
K = float(input('enter number'))

def reverse(N, K):
  N = str(N)
  K = str(K)
  lengthN = len(N)
  lengthK = len(K)
  word_1 =  str(N).find('.')
  word_2 = str(K).find('.')
  print(reversed(N[int(lengthN) -int(word_1)]))


reverse(N, K)



reverse(N, K)


