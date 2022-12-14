# https://leetcode.com/problems/my-calendar-iii/description/

class MyCalendarThree:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> int:
        self.calendar.append((start,1))
        self.calendar.append((end,-1))
        self.calendar.sort()

        maxi = 0
        count = 0

        for event,val in self.calendar:
            count += val
            maxi = max(count,maxi)

        return maxi



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
