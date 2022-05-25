class Instructor:

    def __init__(self, name, roles, availability):
        self.name = name

        self.president = roles[0]
        self.member = roles[1]
        self.secretary = roles[2]
        self.cs = roles[3]
        self.ee = roles[4]

        self.interval_list = availability

    # for debugging
    def tostring(self):
        print(self.name)
        print('president:', self.president)
        print('member:', self.member)
        print('secretary:', self.secretary)
        print('cs:', self.cs)
        print('ee:', self.ee)
        print('availabilities:')
        for interval in self.interval_list:
            print('\t', interval)