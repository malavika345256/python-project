def calculate_average(scores):
    return sum(scores) / len(scores)

def grade_student(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def attendance_summary(attendance_list):
    return (sum(attendance_list) / len(attendance_list)) * 100