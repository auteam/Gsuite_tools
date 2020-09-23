from student import *
from docx_import import *
import csv

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    filename = 'source/КСи Д/Д-115.docx'
    doc_import = ImportDoc(filename)

    group = doc_import.group
    password = 'P@ssw0rd'
    ou = '/student'

    names = doc_import.grouplist

    header_users = [["First Name [Required]", "Last Name [Required]", "Email Address [Required]", "Password [Required]",
                    "Org Unit Path [Required]", "Change Password at Next Sign-In"]]
    with open("output/users_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in header_users:
            writer.writerow(line)
        for f_name in names:
            name = f_name.split(' ')
            stud = Student(name, group, password, ou)
            writer.writerow(stud.add_csv_users_line())

    header_groups = [["Group Email [Required]", "Member Email", "Member Type", "Member Role"]]
    with open("output/group_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in header_groups:
            writer.writerow(line)
        for f_name in names:
            name = f_name.split(' ')
            stud = Student(name, group, password, ou)
            writer.writerow(stud.add_csv_groups_line())
