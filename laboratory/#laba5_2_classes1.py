#laba5-2 класи
# Завдання 2 "Успішність студента"
class Student:
    def __init__(self, name):
        self.name = name

    def labGrades(self, gradelab):
        self.gradelab = gradelab
        gradelab = kurs_settings['amountLabs'] * kurs_settings['maxLabGrade']
        return gradelab

    def konkursGrade(self, gradekonkurs):
        self.gradekonkurs = gradekonkurs
        gradekonkurs = kurs_settings['maxGradeKonkurs']
        return gradekonkurs
    
    def sumAndResult(self, suma, automat):
        self.suma = suma
        self.automat = automat
        suma = self.gradelab*kurs_settings['amountLabs'] + self.gradekonkurs
        automat = 0.8 * kurs_settings['potochka']
        if suma >= automat:
            return f"Чи має студент автомат: {True}, із балом {suma}"
        else:
            return f"Чи має студент автомат: {False}, із балом {suma}"
        
kurs_settings = {'amountLabs': 6, 'maxLabGrade': 5, 'konkurs': 1, 'maxGradeKonkurs': 10, 'potochka': 40}
labGradeUpdate = int(input("Введіть оцінку за лабораторні: "))
kurs_settings.update({'maxLabGrade': labGradeUpdate})
konkursGradeUpdate = int(input("Введіть оцінку за творче завдання: "))
kurs_settings.update({'maxGradeKonkurs': konkursGradeUpdate})
student = Student("пітон")
print("Поточні налаштування курсу:")
print(kurs_settings)
print(f"Для отримання автомату, потрібно набрати мінімум 32 бали")
print(student.labGrades(labGradeUpdate))
print(student.konkursGrade(konkursGradeUpdate))
print(student.sumAndResult(1,automat=0))
