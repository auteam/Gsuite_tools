from src.student import *
from src.docx_import import *
import config as cfg
import csv
import os

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    all_files = os.listdir(cfg.input_dir)
    files = []
    for file in all_files:
        if re.match(cfg.regex_input_file, file):
            files.append(file)
    print(files, end='\n')

    for file in files:
        filename = cfg.input_dir + file
        print('\n' + filename)
        doc_import = ImportDoc(filename, cfg.file_pattern)

        group = cfg.user_data['group']
        domain = cfg.user_data['domain']
        password = cfg.user_data['password']
        ou = cfg.user_data['ou']

        names = doc_import.grouplist

        header_users = [["First Name [Required]", "Last Name [Required]", "Email Address [Required]",
                         "Password [Required]", "Org Unit Path [Required]", "Change Password at Next Sign-In"]]
        print('creating users csv')
        with open("output/users_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in header_users:
                writer.writerow(line)
            for f_name in names:
                if f_name is not None:
                    name = f_name.split(' ')
                    stud = Student(name, domain, group, password, ou)
                    writer.writerow(stud.add_csv_users_line())

        header_groups = [["Group Email [Required]", "Member Email", "Member Type", "Member Role"]]
        print('creating group csv')
        with open("output/group_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in header_groups:
                writer.writerow(line)
            for f_name in names:
                if f_name is not None:
                    name = f_name.split(' ')
                    stud = Student(name, domain, group, password, ou)
                    writer.writerow(stud.add_csv_groups_line())
