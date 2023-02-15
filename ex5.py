name = input('이름 : ')
kor = input('국어 : ')
eng = input('영어 : ')
math = input('수학 : ')

tot = kor + eng + math
avg = tot / 3

if 100 >= avg >=90 : grade = 'A'
elif 90 > avg >=80 : grade = 'B'
elif 80 > avg >=70 : grade = 'C'
elif 70 > avg >=60 : grade = 'D'
else : grade = 'F'

print('이름 = %s, 국어 = %d, 영어 = %d, 수학 = %d' %(name, kor, eng, math))
print('총점 = %d, 평균 = %.2f, 평점 = %s' %(tot, avg, grade))