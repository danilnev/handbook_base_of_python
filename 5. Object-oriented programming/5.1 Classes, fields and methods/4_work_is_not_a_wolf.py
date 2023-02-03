class Programmer:
    def __init__(self, programmer_name, programmer_post):
        self.name = programmer_name
        self.post = programmer_post
        self.work_time = 0
        self.salary = 0
        match self.post:
            case 'Junior':
                self.salary_in_hour = 10
            case 'Middle':
                self.salary_in_hour = 15
            case 'Senior':
                self.salary_in_hour = 20

    def work(self, time):
        self.work_time += time
        self.salary += self.salary_in_hour * time

    def rise(self):
        match self.post:
            case 'Junior':
                self.post = 'Middle'
                self.salary_in_hour = 15
            case 'Middle':
                self.post = 'Senior'
                self.salary_in_hour = 20
            case 'Senior':
                self.salary_in_hour += 1

    def info(self):
        return f'{self.name} {self.work_time}ч. {self.salary}тгр.'


# programmer = Programmer('Васильев Иван', 'Junior')
# programmer.work(750)
# print(programmer.info())
# programmer.rise()
# programmer.work(500)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())
