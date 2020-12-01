from config import config
from src.file_import import ImportFile
from src.student import Student

import os
import re
import csv


def main():
    all_files = os.listdir(config.import_conf.dir)
    files = []
    for file in all_files:
        if re.match(config.import_conf.regex_file, file):
            files.append(file)
    print(files, end='\n')

    for file in files:
        filename = config.import_conf.dir + file
        print('\n' + filename)
        doc_import = ImportFile(filename)

        group = config.user_conf.group
        domain = config.user_conf.domain
        password = config.user_conf.password
        ou = config.user_conf.ou

        names = doc_import.grouplist

        header_users = [["First Name [Required]", "Last Name [Required]", "Email Address [Required]",
                         "Password [Required]", "Org Unit Path [Required]", "Change Password at Next Sign-In"]]
        print('creating users csv')
        with open("output/users_" + file + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in header_users:
                writer.writerow(line)
            for f_name in names:
                if f_name is not None:
                    if config.import_conf.split_FIO:
                        name = f_name.split(' ')
                    else:
                        name = f_name
                    stud = Student(name, domain, group, password, ou)
                    writer.writerow(stud.add_csv_users_line())

        header_groups = [["Group Email [Required]", "Member Email", "Member Type", "Member Role"]]
        print('creating group csv')
        with open("output/group_" + file + "_" + group + ".csv", 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in header_groups:
                writer.writerow(line)
            for f_name in names:
                if f_name is not None:
                    name = f_name.split(' ')
                    stud = Student(name, domain, group, password, ou)
                    writer.writerow(stud.add_csv_groups_line())


if __name__ == '__main__':
    main()
