#
#
#creating a calendar using tkinter

import tkinter as tk
import calendar

#root will open a window display w/the calendar 
root = tk.Tk()
root.title("Calendar")

#the fromat label that will be display in the window display
calendar_label = tk.Label(root, font=("helvetica", 45))
calendar_label.pack(fill= "both", expand= True)

#a function with the calendar libarary being used and making that text appear in the window display
def a_calander():
    yy = 2023
    mm = 9
    calendar_label.config(text= calendar.month(yy,mm)) #putting all the variables into text to display a static calendar
    

a_calander()
root.mainloop()




"""

_summary_
-Same code as the one above just a different function

    
#root will open a window display w/the calendar
root = tk.Tk()
root.title("Calendar")

#the fromat label that will be display in the window display
calendar_label = tk.Label(root, font=("helvetica", 45, "bold"))
calendar_label.pack(fill= "both", expand= True)

#a function with the calendar libarary being used and making that text appear in the window display
def b_calander():
    textcal = calendar.TextCalendar()
    year = 2022     # year
    month = 5       # month
    w = 4           # width of date columns
    l = 2           # number of lines per week
    calendar_label.config(text= textcal.formatmonth(year, month, w, l))
    

b_calander()
root.mainloop()
"""


yy = 2023
mm = 9
print(calendar.month(yy,mm))