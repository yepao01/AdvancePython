from chapter04.class_methodwm import Date
class User:
    def __init__(self,birthday):
        self.__birthday = birthday #双下划线

    def get_age(self):
        #返回年龄
        return 2018 - self.__birthday.year

if __name__ =='__main__':
    # user = User(Date(1992,2,2))
    # print(user.get_age())
    # print(user.get_age())

    user = User(Date.form_string("1992-1-2"))
    print(user.get_age())


