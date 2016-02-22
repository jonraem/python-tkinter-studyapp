from tkinter import *
import tkinter as tk
import sys

__author__ = 'Joni Rämö'
__version__ = '0.1'


class Model():
    def __init__(self, master=None):
        student = Student()
        degree = Degree()
        course = Course()

    def searched_year(self, year):
        searchitems = []
        for i[0] in Student.parse_student_info():
            if i == year:
                searchitems.append(i)
        return searchitems

    def searched_credits(self, ects):
        searchitems = []
        for i[3] in Student.parse_student_info():
            if i > ects:
                searchitems.append(i)
        return searchitems


class Student():
    def __init__(self, master=None):
        self.parse_student_info()
        self.startyears = self.choose_item(0)
        self.studentnums = self.choose_item(1)
        self.students = self.choose_item(2)
        self.totalcredits = self.choose_item(3)
        self.degrees = self.choose_item(4)
        self.majors = self.choose_item(5)

    def parse_student_info(self):
        with open('opiskelijat.txt', 'r') as src:
            self.separ = src.readlines()
            self.studentinfo = [elem.strip().split(';') for elem in self.separ]  #Forms a list of lists
            return self.studentinfo

    def choose_item(self, item):
        chosenitem = [i[item] for i in self.parse_student_info()]
        return chosenitem


class Course():
    def __init__(self, master=None):
        self.parse_course_info()
        self.studentnums = self.choose_item(0)
        self.coursecode = self.choose_item(1)
        self.coursename = self.choose_item(2)
        self.completiondate = self.choose_item(3)
        self.coursecredits = self.choose_item(4)

    def parse_course_info(self):
        with open('suoritukset.txt', 'r') as src:
            self.separ = src.readlines()
            self.courseinfo = [elem.strip().split(';') for elem in self.separ if elem.strip()]
            return self.courseinfo

    def choose_item(self, item):
        if item != 2:
            chosenitem = [i[item] for i in self.parse_course_info()]
            return chosenitem
        else:
            chosenitem = [i[item] for i in self.parse_course_info()]
            parseditem = [x.strip() for x in self.chosenitem]
            return parseditem


class Degree:
    def __init__(self, master=None):
        self.degreename = self.parse_degree_names()
        self.degreecount = self.parse_degree_count()
        self.degreeindex = self.choose_item(0)
        self.coursecode = self.choose_item(1)

    def parse_degree_count(self):
        with open('kandit.txt', 'r') as src:
            count = src.readline()
            return count

    def parse_degree_names(self):
        with open('kandit.txt', 'r') as src:
            degreenames = src.readlines()[1:4]
            strippednames = [elem.strip() for elem in degreenames]
            return strippednames

    def parse_course_codes(self):  #First is degree, second is course code
        with open('kandit.txt', 'r') as src:
            for i in range(4):
                src.__next__()
            for line in src:
                parsedcourses = [elem.strip().split() for elem in src]
                return parsedcourses

    def choose_item(self, item):
        chosenitem = [i[item] for i in self.parse_course_codes()]
        return chosenitem


class UIController(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('StudyApp')
        w = 300
        h = 350
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=False, height=False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, BrowsePage, StudentPage):
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()

    def enter_year(self):
        Model.searched_year(self.callback())

    def callback(self, year=None):
        return year.get()


class StartPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)

        self.label1 = Label(self, text="Hae opintovuoden perusteella:")
        self.label1.place(x=18, y=45)

        year = StringVar()
        self.startyear = Entry(self, bd=2, textvariable=year)
        self.startyear.place(x=20, y=70)
        self.startyear.bind("<Return>", UIController.enter_year)

        self.quitbutton = Button(self, text="Lopeta", command=sys.exit)
        self.quitbutton.pack(side="bottom", padx=5, pady=5, fill=X)

        self.searchbutton = Button(self, text="Hae", command=lambda: controller.show_frame(BrowsePage))
        #self.searchButton.bind("<Return>", UIController.enter_year)
        self.searchbutton.pack(side="bottom", padx=5, pady=0, fill=X)


class BrowsePage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)


class StudentPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)


uicontrol = UIController()
uicontrol.mainloop()