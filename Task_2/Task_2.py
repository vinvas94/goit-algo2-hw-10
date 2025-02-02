# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = []
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, email: {self.email}"
    

def create_schedule(subjects, teachers):
    schedule = []
    
    while subjects:
        # Вибір викладача, який може покрити найбільшу кількість непокритих предметів
        best_teacher = None
        best_teacher_coverage = 0
        
        for teacher in teachers:
            if teacher.assigned_subjects:
                continue  # пропускаємо вже призначених викладачів

            # Кількість предметів, які може викладати викладач і які ще не покриті
            coverage = len(subjects & teacher.can_teach_subjects)
            
            # Вибір викладача, який покриває найбільше предметів
            if coverage > best_teacher_coverage or (coverage == best_teacher_coverage and teacher.age < best_teacher.age):
                best_teacher = teacher
                best_teacher_coverage = coverage

        if best_teacher is None:
            print("Неможливо покрити всі предмети наявними викладачами.")
            return []

        # Призначаємо предмети кращому викладачу
        assigned_subjects = best_teacher.can_teach_subjects & subjects
        best_teacher.assigned_subjects.extend(assigned_subjects)
        
        # Видаляємо покриті предмети зі списку
        subjects -= assigned_subjects
        
        # Додаємо викладача в розклад
        schedule.append(best_teacher)

    return schedule

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
