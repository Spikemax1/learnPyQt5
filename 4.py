from PyQt5.QtCore import QDateTime, Qt

datetime = QDateTime.currentDateTime()

print("Today date and time is: ", datetime.toString(Qt.ISODate))
print("adding 12 days to the date: {}".format(datetime.addDays(12).toString(Qt.ISODate)))
print("Subtracting 25 days: {}".format(datetime.addDays(-25).toString(Qt.ISODate)))