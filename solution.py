import datetime
from dataclasses import dataclass
from typing import List, Dict

class solution:

    @dataclass
    class user_visit:
        latitude: float
        longtitude: float
        starttime: str
        endtime: str

    # take list of user_activity; return dictionary with cooridnate as key and total minutes as value
    def calBrowsingTime(self, entries:List[user_visit]) -> Dict:
        mydict ={}
        for entry in entries:
            coordinate = str(entry.latitude)+","+str(entry.longtitude)
            s_time = datetime.datetime.strptime(entry.starttime, '%d/%m/%Y %H:%M:%S')
            e_time = datetime.datetime.strptime(entry.endtime, '%d/%m/%Y %H:%M:%S')
            # assume entries are valid, e_time always greater than s_time
            # but they might be different days
            # also need to treat corner cases when s_time is after 8 pm, e_time is before 8 am

            #Only consider the time window 8 am- 8 pm
            s_8am = s_time.replace(hour=8, minute=0, second=0, microsecond=0)
            s_8pm = s_time.replace(hour=20, minute=0, second=0, microsecond=0)
            e_8pm = e_time.replace(hour=20, minute=0, second=0, microsecond=0)
            e_8am = e_time.replace(hour=8, minute=0, second=0, microsecond=0)
            if s_time < s_8am:
                s_time = s_8am
            elif s_time > s_8pm:
                s_time = s_8am + datetime.timedelta(days=1)

            if e_time < e_8am:
                e_time =e_8pm - datetime.timedelta(days=1)

            elif e_time > e_8pm:
                e_time = e_8pm

            delta = e_time - s_time
            minutes = int((e_time - s_time).total_seconds() / 60)
            if delta.days >= 1:  # remove the 12 hours from 8 pm to 8 am next day
                minutes = minutes - delta.days * 12 * 60
            # for the case of startTime is 9 pm last night, and endTime is 7 am today
            if minutes < 0:
                minutes = 0

            if coordinate not in mydict:
                mydict[coordinate] = minutes
            else:
                mydict[coordinate] += minutes

        return mydict

    # driver
    def main(self):

        e1= self.user_visit(34.05194, -118.25812, '10/07/2020 21:12:35', '11/07/2020 08:12:35')
        e2= self.user_visit(34.05194, -118.25812, '10/07/2020 10:13:35', '10/07/2020 10:14:35')
        e3 = self.user_visit(34.05194, -118.25812, '10/07/2020 07:13:35', '10/07/2020 20:14:35')
        e4 = self.user_visit(35.05194, -118.25812, '10/08/2020 07:13:35', '10/08/2020 10:14:35')
        x = self.calBrowsingTime([e1])
        print(x)


if __name__ == '__main__':
        s = solution()
        s.main()