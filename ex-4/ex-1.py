class Student(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name


def main():
    student1 = Student('Mehedi Hasan')
    student2 = Student('Hasan')

    print('Checking Equal')
    if student1 == student2:
        print("Equal")
    else:
        print('Not Equal')

    print('\nChecking Less Than')
    if student1 < student2:
        print(student1.name + " is less than " + student2.name)
    else:
        print(student1.name + " is not less than " + student2.name)

    print('\n Greater Than Or Equal Check')
    if student1 >= student2:
        print(student1.name + " is greater than or equal " + student2.name)
    else:
        print(student1.name + " is not greater than or equal " + student2.name)


if __name__ == "__main__":
    main()
