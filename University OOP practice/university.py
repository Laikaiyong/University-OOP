class Student:
    """Student class represent students record in the university
    """

    def __init__(self, stud_id, stud_name, stud_age, stud_nationality, stud_course):
        """Method for initializing a Student object

        Args: 
            id (str)
            name (str)
            age (int)
            nationality (str)
            course enrolled (str)

        Attributes:
            id (str): student id
            name (str): student name
            age (int): student age
            nationality (str): student nationality
            course enrolled (str): student enrolled course subject
        """

        self.id = stud_id
        self.name = stud_name
        self.age = stud_age
        self.nationality = stud_nationality
        self.course_enrolled = stud_course

    def swap_course(self, new_course):
        """The swap course method to update when Student change their course module

        Args: 
            new_course (str): the new course enrolled by the student object

        Returns: None
        """
        self.course_enrolled = new_course

    def update_age(self):
        """The update age method When 1 year had passed through

        Args: None

        Returns: None
        """
        self.age += 1


class Lecturer:
    """Lecturer class represent lecturers record in the university
    """

    def __init__(self, lec_id, lec_name, lec_age, lec_expertise, lec_course):
        """Method for initializing a Lecturer object

        Args: 
            id (str)
            name (str)
            age (int)
            expertise (int)
            course taught (str)

        Attributes:
            id (str): lecturer id
            name (str): lecturer name
            age (int): lecturer age
            expertise (int): lecturer expertise (1 Beginner, 2 Intermediate, 3 Expert)
            course taught (str): lecturer teach course subject
        """

        self.id = lec_id
        self.name = lec_name
        self.age = lec_age
        self.expertise = lec_expertise
        self.course_taught = lec_course

    def teach_course(self, new_course):
        """The teach course method when lecturer teach other course module

        Args: 
            new_course (str): the new course taught by the lecturer object

        Returns: None
        """
        self.course_taught = new_course

    def update_age(self):
        """The update age method When 1 year had passed through

        Args: None

        Returns: None
        """
        return self.age + 1

    def upgrade(self, new_expertise):
        """The upgrade method When lecturer expertise met a target

        Args: 
            new_expertise (int): the new expertise acquired by the lecturer object

        Returns: None
        """
        self.expertise = new_expertise
