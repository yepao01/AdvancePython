class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self): #名为self的实例
        self.day += 1

    @staticmethod
    def parse_form_string(date_str):
        year,month,day = date_str.split("-")
        return Date(int(year),int(month),int(day)) #如果类名更改，这里必须手动修改

    @staticmethod
    def valid_str(date_str):
        year, month, day = date_str.split("-")
        if int(year)>0 and (int(month)>0 and int(month)<=12) and (int(day)>0 and int(day)<=31):
            return True
        else:
            return False

    @classmethod
    def form_string(cls,date_str):
        year,month,day = date_str.split("-")
        return cls(int(year),int(month),int(day)) #不涉及到类名 无需修改

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)

if __name__ =="__main__":
    new_day = Date(2019,5,17)
    new_day.tomorrow()
    print(new_day)

    date_str = "2019-5-17"
    year,month,day = date_str.split("-")
    new_day = Date(int(year),int(month),int(day))
    new_day.tomorrow()
    print(new_day)

    # 使用staticmethod初始化
    new_day = Date.parse_form_string(date_str)
    print(new_day)
    print(new_day.year)

    #使用classmethod初始化
    new_day = Date.form_string(date_str)
    print(new_day)

    # 使用staticmethod初始化
    new_day = Date.valid_str("2019-5-2")
    print(new_day)
