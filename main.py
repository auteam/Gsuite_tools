from student import *
from docx_import import ImportDoc
import re
import csv
import os


if __name__ == '__main__':
    dir_files = 'source/'
    all_files = os.listdir(dir_files)
    doc_format = 'n1'   # n1 (several files), n2 (all in one: (text(group) + table)*n )
    files = []
    for file in all_files:
        if doc_format == 'n1':
            if re.match(r'.*\w+-\d\d\d\.docx', file):
                files.append(file)
        elif doc_format == 'n2':
            if re.match(r'n2\.docx', file):
                files.append(file)
        # elif doc_format == 'n3':
        #     if re.match(r'n3\.docx', file):
        #         files.append(file)
    print(files, end='\n')

    for file in files:
        filename = dir_files + file
        print('\n' + filename)
        doc_import = ImportDoc(filename, doc_format)

        domain = 'urtt.ru'
        password = 'P@ssw0rd'
        ou = '/students'
        header_users = [
            ["First Name [Required]", "Last Name [Required]", "Email Address [Required]", "Password [Required]",
             "Org Unit Path [Required]", "Change Password at Next Sign-In"]]
        header_groups = [["Group Email [Required]", "Member Email", "Member Type", "Member Role"]]

        groups = doc_import.groups
        names = doc_import.grouplist
        groups_dict = {}

        if doc_format == 'n1':
            for i in range(len(groups)):
                groups_dict[groups[0]] = names
        elif doc_format == 'n2':
            for i in range(len(groups)):
                groups_dict[groups[i]] = names[i]
        # elif doc_format == 'n3':
        #     for i in range(len(groups)):
        #         groups_dict[groups[i]] = names[i]

        for group in groups:
            with open("output/users_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for line in header_users:
                    writer.writerow(line)
                for f_name in groups_dict.get(group):
                    if f_name is not None:
                        name = f_name
                        stud = Student(name, domain, group, password, ou)
                        writer.writerow(stud.add_csv_users_line())

            with open("output/group_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for line in header_groups:
                    writer.writerow(line)
                for f_name in groups_dict.get(group):
                    if f_name is not None:
                        name = f_name
                        stud = Student(name, domain, group, password, ou)
                        writer.writerow(stud.add_csv_groups_line())
