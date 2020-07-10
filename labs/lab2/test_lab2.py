from grade import GradeEntry, NumericGradeEntry, LetterGradeEntry
if __name__ == '__main__':
    grades = [NumericGradeEntry('csc148', 87, 0.5),
    NumericGradeEntry('mat137', 76, 1.0),
    LetterGradeEntry('his450', 'B+', 0.5)]
    for g in grades:
        g.convert()
    for g in grades:
    # Use appropriate ??? methods or attributes of g in format
        print("Weight: {}, grade: {}, points: {}".format(g.name, g.grade, g.weight))
    # Use methods or attributes of g to compute weight times points
    total = sum(  # sum of the list of...
    [g.grade * g.weight  # methods or attributes of g
    for g in grades])  # using each g in grades
    # sum up the credits
    total_weight = sum([g.weight for g in grades])
    print("GPA = {}".format(total / total_weight))
