from PyQt5.QtCore import QDate

date = QDate.currentDate()

d = QDate(2019, 12, 12)
print("Days in a month:{}: ".format(d.daysInMonth()))
print("Days in a year:{}".format(d.daysInYear()))