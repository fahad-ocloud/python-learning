from persons.employee import Employee
from persons.teacher import Teacher


def main():
    tchr = Teacher("Ahmad", 19, 300000)
    emp = Employee("Rohan", 19, 100000)

    tchr.work()
    emp.work()

main()