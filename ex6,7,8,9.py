사람의_종류 = 10
x = f"세상에는 {사람의_종류} 종류의 사람이 있어요."

이진수 = "'이진수'"
모르는 = "모르는"
y = f"{이진수}를 아는 사람과 {모르는} 사람."

print(x)
print(y)

print(f"'{x}'라고 했어요.")
print(f"'{y}'이라고도 했죠.")

웃김 = False
농담_평가 = "웃기는 농담 아니에요?! {}"
print(농담_평가, format(웃김))

w = "이 문자열의 왼쪽 ->"
e = "<-이 문자열의 오른쪽"

print(w + e)

#ex7.py

print("영희에겐 꼬마 양이 있지")
print("양털은 {}처럼 새하얗네." .format('눈'))
print("그리고 영희가 가는 곳마다.")
print("." * 10) #어떻게 될까요?

end1 = "맛"
end2 = "있"
end3 = "는"
end4 = "치"
end5 = "즈"
end6 = "버"
end7 = "거"

# 마지막에 있는 end 매개변수를 살펴보세요 (end='')
# 지워보고 무슨 일이 일어나는지도 보세요

print(end1 + end2 + end3, end='')
print(end4 + end5 + end6 + end7)

# ex8.py

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("하나", "둘", "셋", "넷"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "난 이게 있죠.",
    "지금 막 써 주신 그것.",
    "하지만 '노래'하진 않아요,",
    "그러니까 잘 자요."
))

# ex9.py

요일 = "월 화 수 목 금 토 일"
달 = "1월\n2월\n3월\n4월\n5월\n6월\n7월\n8월"

print("요일 목록: ", 요일)
print("달 목록: ", 달)

print("""
여기 무언가가 있어요
세 개의 따옴표 안에요.
쓰고 싶은 만큼 쓸 수 있어요.
4줄이든, 5줄이든, 6줄이든 원하는 만큼.
""")
