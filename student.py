from transliterate import translit


class Student:
    # TODO Check FIO by regex and exception list
    full_name_ru = ['Свирепов', 'Денис', 'Дмитриевич']
    full_name_en = ['Svirepov', 'Denis', 'Dmitrievich']
    domain = 'urtt.ru'
    group = 'bi-15'
    password = 'P@ssw0rd'
    email = 'svirepov.dd@urtt.ru'
    group_email = 'bi-15@urtt.ru'
    ou = '/'
    member_type = "USER"
    member_role = "MEMBER"

    def __init__(self, full_name, domain, group, password, ou):
        self.full_name_ru = full_name
        if len(self.full_name_ru) == 2:
            for i in range(2):
                self.full_name_en[i] = translit(full_name[i], 'ru', reversed=True)
        elif len(self.full_name_ru) == 3:
            for i in range(3):
                self.full_name_en[i] = translit(full_name[i], 'ru', reversed=True)

        self.domain = domain
        self.group = group
        self.group_email = group + '@' + domain
        self.password = password
        self.ou = ou

        group_ = group + '.'
        familia = (self.full_name_en[0].lower()).replace('\'', '')
        io = '.' + (self.full_name_en[1].lower()).replace('\'', '')[0] + \
             (self.full_name_en[2].lower()).replace('\'', '')[0]
        self.email = group_ + familia + io + '@urtt.ru'

    def create_email(self):
        group_ = self.group + '.'
        familia = (self.full_name_en[0].lower()).replace('\'', '')
        io = '.' + (self.full_name_en[1].lower()).replace('\'', '')[0] + \
             (self.full_name_en[2].lower()).replace('\'', '')[0]
        self.email = group_ + familia + io + '@urtt.ru'
        return self.email

    def add_csv_users_line(self):
        if len(self.full_name_ru) == 2:
            return [self.full_name_ru[1], self.full_name_ru[0], self.email, self.password, self.ou, 'True']
        elif len(self.full_name_ru) == 3:
            return [self.full_name_ru[1] + ' ' + self.full_name_ru[2], self.full_name_ru[0],
                    self.email, self.password, self.ou, 'True']

    def add_csv_groups_line(self):
        return [self.group_email, self.email, self.member_type, self.member_role]


# class Group():
#     students = []  # list of Student objects
#
#     def __init__(self, students):
#         self.students = students
