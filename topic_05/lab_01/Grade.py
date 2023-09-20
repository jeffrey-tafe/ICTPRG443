class Grade():

    def set_grade(self, input):

        # If mark is not a number, error
        try:
            mark = int(input)
        except ValueError:
            return "ERROR"

        # If mark is outside valid grade range, error
        if mark < 0 or mark > 100:
            return "ERROR"

        # Switch statement to mark
        if mark >= 85:
            return "HD"
        elif mark >= 75:
            return "D"
        elif mark >= 65:
            return "C"
        elif mark >= 50:
            return "P"
        else:
            return "F"

# grade = Grade()
# print(grade.set_grade("56"))

