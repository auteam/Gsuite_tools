from student import *
import csv

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    s = '''Банных Елизавета Алексеевна
Держун Егор Артемович
Барташ Роман Эдуардович
Дмитриева Карина Сергеевна
Дудин Станислав Олегович
Ефремова Татьяна Дмитриевна
Забродина Виктория Валентиновна
Кирьянова Алина Алексеевна
Климцева Софья Александровна
Коньков Данил Васильевич
Кочетков Константин Вячеславович
Новиков Александр Алексеевич
Подойников Эдуард Вадимович
Праздничкова Полина Михайловна
Радченко Карина Евгеньевна
Рахвалов Даниил Тимофеевич
Ситников Вячеслав Владимирович
Соколова Виктория Вадимовна
Трофимов Дмитрий Алексеевич
Трофимова Анна Вячеславовна
Чеплыгина Арина Александровна
Чижнов Евгений Витальевич
Шамсумов Эрик Ринатович
Шунайлова Екатерина Владимировна
Шуплецова Екатерина Васильевна'''

    group = 'bi-15'
    password = 'P@ssw0rd'
    ou = '/student'

    names = s.split("\n")

    header_users = [["First Name [Required]", "Last Name [Required]", "Email Address [Required]", "Password [Required]",
                    "Org Unit Path [Required]", "Change Password at Next Sign-In"]]
    with open("users_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in header_users:
            writer.writerow(line)
        for f_name in names:
            name = f_name.split(' ')
            stud = Student(name, group, password, ou)
            writer.writerow(stud.add_csv_users_line())

    header_groups = [["Group Email [Required]", "Member Email", "Member Type", "Member Role"]]
    with open("group_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in header_groups:
            writer.writerow(line)
        for f_name in names:
            name = f_name.split(' ')
            stud = Student(name, group, password, ou)
            writer.writerow(stud.add_csv_groups_line())
