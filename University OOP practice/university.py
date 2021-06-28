class UniMember:
    def __init__(self, id, name, age, course):
        """Method for initializing a UniMemobject

        Args: 
            id (str)
            name (str)
            age (int)

            course(str)

        Attributes:
            id (str): student id
            name (str): student name
            age (int): student age

            course enrolled (str): student enrolled course subject
        """
        self.id = id
        self.name = name
        self.age = age
        self.course = course

    def update_age(self):
        """The update age method When 1 year had passed through

        Args: None

        Returns: None
        """
        self.age += 1

    def swap_course(self, new_course):
        """The swap course method to update when Object change their course module

        Args: 
            new_course (str): the new course appointed to student object

        Returns: None
        """
        self.course = new_course


class Student(UniMember):
    """Student class represent students record in the university
    """

    def __init__(self, id, name, age, nationality, course):
        """
        Args:
            nationality (str)

        Attributes:
            nationality (str): student nationality
        """
        UniMember.__init__(self, id, name, age, course)
        self.nationality = nationality


class Lecturer(UniMember):
    """Lecturer class represent lecturers record in the university
    """

    def __init__(self, id, name, age, expertise, course):
        """
        Args: 
            expertise (int)

        Attributes:
            expertise (int): lecturer expertise (1 Beginner, 2 Intermediate, 3 Expert)
        """
        UniMember.__init__(self, id, name, age, course)
        self.expertise = expertise

    def upgrade(self, new_expertise):
        """The upgrade method When lecturer expertise met a target

        Args: 
            new_expertise (int): the new expertise acquired by the lecturer object

        Returns: None
        """
        self.expertise = new_expertise
