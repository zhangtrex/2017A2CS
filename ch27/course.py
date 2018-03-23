class Course(object):
    def __init__(self,t,m):
        self.__coursetitle = t;
        self.__maxstudents = m;
        self.__numberoflessons = 0;
        self.__courselesson = [];
        self.__courseassessment = 0;

    def addlesson(self,t,d,r):
        self.__numberoflessons = self.__numberoflessons + 1;
        self.__courselesson.append(Lesson(t,d,r));

    def addassessment(self,t,m):
        self.__courseassessment = Assessment(t,m);

    def outputcoursedetails(self):
        print(self.__coursetitle,'Maximum number: ',self.__maxstudents);
        print()
        for i in range(self.__numberoflessons):
            self.__courselesson[i].outputlessondetails()

class Lesson(object):
    def __init__(self,t,d,r):
        self.__lessontitle = t;
        self.__durationminutes = d;
        self.__requireslab = r;

    def outputlessondetails(self):
        print('Lesson details');
        print('Lesson name: ',self.__lessontitle);
        print('Duration minutes: ',self.__durationminutes);
        print('Lab requirement: ',self.__requireslab);
        print()

class Assessment(object):
    def __init__(self,t,m):
        self.__assessmenttitle = t;
        self.__maxmarks = m;

    def outputassessmentdetails(self):
        print('Assessment details');
        print('Assessment title: ',self.__assessmenttitle);
        print('Maximum Marks: ',self.__maxmarks);
        print()

C = Course('Further Math',25);
C.addlesson('Pure Math',200,False);
C.addlesson('Statistics',200,False);
C.addassessment('FM homework',100);
C.outputcoursedetails();
