total_score = 0
total_credit = 0

for i in range(0, 20):
    subject, credit, score = input().split()
    credit = float(credit)

    if score == "P":
        pass
    elif score == "A+":
        total_score += credit * 4.5
        total_credit += credit
    elif score == "A0":
        total_score += credit * 4.0
        total_credit += credit
    elif score == "B+":
        total_score += credit * 3.5
        total_credit += credit
    elif score == "B0":
        total_score += credit * 3.0
        total_credit += credit
    elif score == "C+":
        total_score += credit * 2.5
        total_credit += credit
    elif score == "C0":
        total_score += credit * 2.0
        total_credit += credit
    elif score == "D+":
        total_score += credit * 1.5
        total_credit += credit
    elif score == "D0":
        total_score += credit * 1.0
        total_credit += credit
    elif score == "F":
        total_score += credit * 0.0
        total_credit += credit

print("%.6f" % (total_score / total_credit))