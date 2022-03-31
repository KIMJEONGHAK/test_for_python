# 사용자로부터 성적을 입력받고 점수의 합과 평균 출력하기


print("수학 성적을 입력해 주세요: ")
math = int(input())
print("과학 성적을 입력해 주세요: ")
sci = int(input())
print("영어 성적을 입력해 주세요: ")
eng = int(input())
print("국어 성적을 입력해 주세요: ")
kor = int(input())

sum = math + sci + eng + kor
avg = sum / 4

print("당신의 점수의 총점은 %d점이고 평균은 %d점입니다." % (sum, avg))
