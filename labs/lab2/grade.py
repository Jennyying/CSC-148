from typing import Any, Dict, Tuple


class GradeEntry:
    """a student record system at U of T that keeps track of course identifier, course weight and course grade
    === Attributes ===
    name - the course in which the grade was earned
    weight - how many credits
    grade - grade points according to a 4.0 scale
    """
    name: str
    weight: float
    grade: Any

    def __init__(self, name: str, grade: Any, weight: float) -> None:
        """ Initialize a new GradeEntry
        >>> new = GradeEntry('csc108', 98, 1.0)
        >>> new.records
        ('csc108', 1.0, 98)
        """
        self.name = name
        self.weight = weight
        self.grade = grade

    def __eq__(self, other: Any) -> bool:
        """ Return whether GradeEntry has the same value as others
        >>> g1 = GradeEntry({'csc108': (98, 1.0)}
        >>> g2 = GradeEntry({'csc148':(88, 1.0)}
        >>> g1 == g2
        False
        """
        if type(self) != type(other):
            return False
#        for course in self.records:
#            if self.records[course] != other.records[course]:
#                return False
#        return True
        return self.name == other.name and self.weight == other.weight and self.grade == other.grade

    def __str__(self) -> str:
        """ Return a string representation of GradeEntry
        >>> print('csc108', 1.0, 98)
        csc108: (98, 1.0)  csc148:(88, 1.0)

        """
        new = ''
#        for course in self.records:
        return 'Name:{}, Weight:{}, Grade:{}'.__format__(self.name, self.grade, self.weight)

    def convert(self) -> Any:
        raise NotImplementedError


class NumericGradeEntry(GradeEntry):
    """ A GradeEntry that has numerical grades
    """
    def __init_(self, name: str, grade: int, weight: float) -> None:
        GradeEntry.__init__(self, name, grade, weight)

    def convert(self) -> None:
        """ Convert numerical grades to 4.0 scale
        >>> n1 = NumericGradeEntry('csc108', 98, 1.0)
        >>> n1.convert()
        >>> n1
        {'csc108': (1.0, 4.0)}
        """

        score = self.grade
        if score >= 85:
           self.grade = 4.0
        elif score >= 80:
            self.grade = 3.7
        elif score >= 77:
            self.grade = 3.3
        elif score >= 73:
            self.grade = 3.0
        elif score >= 70:
            self.grade = 2.7
        elif score >= 67:
            self.grade = 2.3
        elif score >= 63:
            self.grade = 2.0
        elif score >= 60:
            self.grade = 1.7
        elif score >= 57:
            self.grade = 1.3
        elif score >= 50:
            self.grade = 1.0
        else:
            self.grade = 0.0

class LetterGradeEntry(GradeEntry):
    """ A GradeEntry that has numerical grades
    """
    def __init_(self, name: str, grade: int, weight: float) -> None:
        GradeEntry.__init__(self, name, grade, weight)

    def convert(self) -> None:
        score = self.grade
        if score == 'A+':
            self.grade = 4.0
        if score == 'A':
           self.grade = 4.0
        elif score == 'B+':
            self.grade = 3.7
        elif score == 'B':
            self.grade = 3.3
        elif score == 'B-':
            self.grade = 3.0
        elif score == 'C+':
            self.grade = 2.7
        elif score == 'C':
            self.grade = 2.3
        elif score == 'C-':
            self.grade = 2.0
        elif score == 'D+':
            self.grade = 1.7
        elif score == 'D':
            self.grade = 1.3
        elif score == 'D-':
            self.grade = 1.0
        else:
            self.grade = 0.0
