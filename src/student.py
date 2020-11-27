from transliterate import translit
from config import config


class Student:
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
        if config.user_conf.group_in_email:
            self.email = group_ + familia + io + '@' + domain
        else:
            self.email = familia + io + '@' + domain

    def create_email(self):
        group_ = self.group + '.'
        familia = (self.full_name_en[0].lower()).replace('\'', '')
        io = '.' + (self.full_name_en[1].lower()).replace('\'', '')[0] + \
             (self.full_name_en[2].lower()).replace('\'', '')[0]
        self.email = group_ + familia + io + '@' + self.domain
        return self.email

    def add_csv_users_line(self):
        return [self.full_name_ru[1] + ' ' + self.full_name_ru[2], self.full_name_ru[0],
                self.email, self.password, self.ou, 'True']

    def add_csv_groups_line(self):
        return [self.group_email, self.email, self.member_type, self.member_role]
