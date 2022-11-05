class Mentor:
    def __init__(self, name, surname ):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = {}

    def estimation(self, lecturer, course,  grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def aver_grades(self):
        for key,value in self.grades.items():
            self.average_grades[key] = round(sum(value)/len(value), 2)

    def __str__(self):
        Stu = f" Имя: {self.name} \n Фамилия: {self.surname}\n " \
              f"Средний балл за лекции: {round(sum(self.average_grades.values())/len(self.average_grades.values()), 1)}\n" \
              f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершенные лурсы: {', '.join(self.finished_courses)}"
        return Stu

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не является студентом")
            return
        return round(sum(self.average_grades.values())) / len(self.average_grades.values()) < \
               round(sum(other.average_grades.values())) / len(other.average_grades.values())

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__( name, surname)
        self.grades = {}
        self.ad_grades = {}

    def average_score(self):
        for key,value in self.grades.items():
            self.ad_grades[key] = round(sum(value)/len(value), 2)



    def __str__(self):
        lec = f" Имя: {self.name} \n Фамилия: {self.surname} \n " \
              f"Средний балл за лекции: {round(sum(self.ad_grades.values())/len(self.ad_grades.values()), 1)}"
        return lec

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не является лектором")
            return
        return round(sum(self.ad_grades.values())) / len(self.ad_grades.values()) < \
               round(sum(other.ad_grades.values())) / len(other.ad_grades.values())

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
    def __str__(self):
        res = f" Имя: {self.name} \n Фамилия: {self.surname}"
        return res

######студенты
John = Student(" John", " Travolta", "Man")
John.finished_courses += ["French"]
John.courses_in_progress += ["JS"]
John.courses_in_progress += ["Python"]
John.courses_in_progress += ["GIT"]
Uma = Student("Uma", "Thurman", "Woman")
Uma.finished_courses += ["JS"]
Uma.courses_in_progress += ["Python"]
Uma.courses_in_progress += ["Django"]
Uma.courses_in_progress += ["French"]
Bruce = Student("Brucey", "Willis", "Man")
Bruce.finished_courses += ["Django"]
Bruce.courses_in_progress += ["English"]
Bruce.courses_in_progress += ["Python"]
Bruce.courses_in_progress += ["GIT"]
####ревьюер
Quentin = Reviewer("Quentin", " Tarantino")
Quentin.courses_attached += ["Python", "GIT"]
Luc = Reviewer("Luc", "Besson")
Luc.courses_attached += ["French", "Django"]
Allen = Reviewer("Allen", "Woody")
Allen.courses_attached += ["English", "JS"]
#####лекторы
Thom = Lecturer("Thom", "Cruise")
Thom.courses_attached += ["English", "Python"]
Bradle = Lecturer("Bradle", "Pitt")
Bradle.courses_attached += ["JS", "GIT"]
Tom = Lecturer("Tom", "Hanks")
Tom.courses_attached += ["French", "Django"]
#########ревьюеры ставят
Quentin.rate_hw(Bruce, "GIT", 10)
Quentin.rate_hw(John, "GIT", 7)
Quentin.rate_hw(Uma, "GIT", 8)
Quentin.rate_hw(Uma, "Python", 10)
Quentin.rate_hw(John, "Python", 9)
Quentin.rate_hw(Bruce, "Python", 7)

Luc.rate_hw(Bruce, "Django", 8)
Luc.rate_hw(John, "French", 8)
Luc.rate_hw(Uma, "Django", 9)
Luc.rate_hw(Uma, "French", 7)

Allen.rate_hw(John, "JS", 9)
Allen.rate_hw(Bruce, "English", 10)
Allen.rate_hw(Uma, "JS", 8)
#########студенты ставят
John.estimation(Bradle, "JS", 9)
John.estimation(Thom, "Python", 10)
John.estimation(Bradle, "GIT", 9)

Uma.estimation(Tom, "French", 7)
Uma.estimation(Thom, "Python", 9)
Uma.estimation(Tom, "Django", 9)

Bruce.estimation(Thom, "English", 10)
Bruce.estimation(Thom, "Python", 10)
Bruce.estimation(Bradle, "GIT", 10)

Thom.average_score()
Bradle.average_score()
Tom.average_score()

John.aver_grades()
Uma.aver_grades()
Bruce.aver_grades()

lt = [John, Uma, Bruce]
def st_av_gr(students, course):
    st = []
    for student in students:
       for key, value in student.average_grades.items():
           if course in key:
               st.append(value)
    return round(sum(st)/len(st), 2)

ll = [Thom, Bradle, Tom]
def le_av_gr(lecturers, course):
    le = []
    for lecturer in lecturers:
       for key, value in lecturer.ad_grades.items():
           if course in key:
               le.append(value)
    return round(sum(le)/len(le), 2)

# print(le_av_gr(ll,"Python"))
# print(st_av_gr(lt, "Python"))
# print(John.__dict__)
# print(Uma.__dict__)
# print(Bruce.__dict__)
# print(Quentin.__dict__)
# print(Luc.__dict__)
# print(Allen.__dict__)
# print(Thom.__dict__)
# print(Bradle.__dict__)
# print(Tom.__dict__)
# print(Thom)
# print(Bradle)
# print(Tom)
# print()
# print(John)
# print(Uma)
# print(Bruce)
# print(John.__lt__(Uma))
# print(John.__lt__(Bruce))
# print(Uma.__lt__(Bruce))
# print(Uma.__lt__(John))
# print(Bruce.__lt__(John))
# print(Bruce.__lt__(Uma))
