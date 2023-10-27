

def prompt_scores():
    scores_input = input("Enter scores: ")
    scores_list = [int(number) for number in scores_input.split()]
    return scores_list


def calc_marks(scores):
    marks = []
    for score in scores:
        if score >= 90:
            marks.append("A")
        elif score >= 75:
            marks.append("B")
        elif score >= 50:
            marks.append("C")
        elif score >= 35:
            marks.append("D")
        else:
            marks.append("F")
    return marks

def output_result(scores, marks):
    for student in range(len(scores)):
        print(f"Student {student} score is {scores[student]} and grade is {marks[student]}")


def main():
    scores = prompt_scores()
    marks = calc_marks(scores)
    output_result(scores, marks)


main()
