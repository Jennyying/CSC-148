from typing import Any, Dict, List


class Registry:
    """A registry of runners in a 5K race.  Each runner is identified by
    their email address and is registered in a speed category.

    === Attributes ===
    groups - runners grouped by category
    """
    groups: Dict[str, list]
    runners: Dict[str, str]

    # The names of the speed CATEGORIES for a race.
    CATEGORIES = ['<20', '<30', '<40', '>=40']

    def __init__(self) -> None:
        """ Initialize a new race registry with no runners entered.
        """
        self.groups = {}
        self.runners = {}
        for c in Registry.CATEGORIES:
            self.groups[c] = []

    def __eq__(self, other: Any) -> bool:
        """
        Return whether Registry self has same value as other.
        """
        if type(self) != type(other):
            return False
        for c in Registry.CATEGORIES:
            if self.groups[c] != other.groups[c]:
                return False
        # note that runners contains the same information
        # as groups, so we don't have to explicitly compare.
        return True

    def register(self, email: str, category: str) -> None:
        """ Register runner with email andd category.
        """
        # remove the runner from all categories they are
        # currently in.
        for c in Registry.CATEGORIES:
            if email in self.groups[c]:
                self.groups[c].remove(email)
        self.groups[category].append(email)
        self.groups[category].sort()
        self.runners[email] = category

    def get_runner_category(self, email: str) -> str:
        """ Return what speed category a given runner is in.
        """
        return self.runners[email]

    def get_runners_in_category(self, category: str) -> List[str]:
        return self.groups[category]

class Patient_Rooster:
    """A doctor has patients, each of whom has an OHIP number,
    family name, first name and gender.  The doctor has a limit on the number
    of patients they can take.  The doctor may have a gender balance rule:
    a limit on the difference between the number of male and female patients
    they are willing to have.  When a patient asks to register with the
    doctor, they will be successful only if the doctor is not at his or her
    limit and the patient will not violate the doctor's gender balance rule.
    Sometimes patients move, change doctors, or die, and in those cases they
    need to be removed from the doctor's list.
    === Attributes ===
    groups - patients grouped by gender
    """
    def __init__(self, limit: int, balance: float) -> None:
        """
        Initialize a new register with no patients
        """
        self.limit = limit
        self.balance = balance
        self.male = {}
        self.female = {}

    def __eq__(self, other: Any) -> bool:
        """
        Return whether self and other has the same information
        """
        if self.type != other.type:
            return False
        for p in self.male:
            if self.male[p] != other.male[p]:
                return False
        for p in self.female:
            if self.female[p] != other.female[p]:
                return False
        return True

    def register(self, number: int, family_n: str, first_n: str, gender: str) -> None:
        if len(self.male) + len(self.female) <= self.limit:
            if gender == 'male':
                if abs((len(self.male) + 1) - len(self.female)) < self.balance:
                    self.male[number] = (family_n, first_n)
            if gender == 'female':
                if abs(len(self.male) - (len(self.female) + 1)) < self.balance:
                    self.female[number] = (family_n, first_n)

    def remove(self, name: tuple):
        for p in self.male:
            if self.male[p] == name:
                self.male.__delitem__(p)
        for p in self.female:
            if self.female[p] == name:
                self.female.__delitem__(p)

class ClassList:
    """
    A course has students in it. Each student is identified by a unique
    student number. There is a limit on how many students can register,
    but that limit can change.  Students are allowed to add and drop the
    course.
    === Attribute ===
    students - a group of students enrolled in that course
    """
    def __init__(self) -> None:
        self.students = {}

    def __str__(self) -> str:
        rep = ''
        for s in self.students:
            rep += ('Surname: {}, Name: {}, Student Number:{}').format\
                (self.students[s][1], self.students[s][2], self.students[s][0])

    def register(self, student: list) -> None:
        """
        register the student into ClassList
        """
        self.students[student[0]] = student[1:]

    def remove(self, student: list) -> None:
        """
        remove the student who drop the course
        """
        del(self.students[student[0]])

class Player:
    """
    A player has a name and a history of the last 100 scores they've
    achieved in the game.  We need to keep track of new scores they
    get so we can determine their top score and their average score
    on their most recent n games, where n is some positive whole number.
    === Attribute ===
    history: a list of the last 100 scores
    """
    def __init__(self, name) -> None:
        self.name = name
        self.history = []

    def add(self, score: int) -> None:
        """
        Add the player's new score
        """
        if len(self.history) == 100:
            self.history.remove(self.history[0])
        self.history.append(score)

    def calculate_average(self, n: int) -> int:
        """
        return the average score of last n times
        """
        total = 0
        counter = 0
        i = 0
        while counter != n:
            total += self.history[i]
            i += 1
            counter += 1
        return counter / n

class InventoryItem:
    """
    Items are for sale, each one at its own price.  Items are identified
    by their item number, and they also have a text description, such as
    "bath towel".  There are categories that items belong to, such as
    "housewares" and "books".  We need to be able to print a suitable
    price tag for an item (you can decide the exact format).  Sometimes
    an item is discounted by a certain percentage.  We need to be able
    to compare two items to see which is cheaper.
    """
    def __init__(self, number: int, description: str, category: str, price: float) -> None:
        self.number = number
        self.des = description
        self.cat = category
        self.price = price

    def discount(self, discount: float) -> None:
        """
        Modify the price with its discount
        """
        self.price = self.price * discount

    def __lt__(self, other):
        return self.price < other.price
