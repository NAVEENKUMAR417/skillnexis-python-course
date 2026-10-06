marks_english=float(input("Enter marks in English:"))
marks_Maths=float(input("Enter marks in Maths:"))
marks_science=float(input("Enter marks in Science:"))
marks_hindi=float(input("Enter marks in Hindi:"))

def CalcAverage(marks):
    return sum(marks) / len(marks)

marks=[marks_english+marks_Maths+marks_science+marks_hindi]
result=CalcAverage(marks)

if result>=90:
        grade="A"
elif result>=80:
        grade="B"
elif result>=70:
        grade="C"
elif result>=60:
        grade="D"
elif result>=50:
        grade="E"
else:
        grade="F"




print("grade",grade)
print("result",result)

