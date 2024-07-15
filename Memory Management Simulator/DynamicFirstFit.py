
# importing modules
from tkinter import*
from tkinter import ttk
from array import*
from tkinter import messagebox
import csv
import math
import sys
import os
from subprocess import run

#from PIL import Image, ImageTk

global listbox
# end of module importing

# For the backend
import datetime
import time
from copy import deepcopy


# getting current directory of the app
try:
    currentDirectory = os.getcwd()
    ###Started(currentDirectory)
except:
    print ( " Error : Cannot find the Current Directory. " )
# end of getting current directory


# creating the tkinter root that will accommodate the UI
root = Tk()
root.title ( "DYNAMIC FIRST FIT PARTITION ALLOCATION" )
#

# Resources
def load_image(image_path):
    try:
        return PhotoImage(file=image_path)
    except Exception as e:
        print(f"Error: {e}")
        return None
#   -> Background

bg3 = PhotoImage(file = "MMWINDOWBG.png")
bg4 = PhotoImage(file = "MMWINDOWBG.png" )

windowbg = load_image("windowbg.png")
if windowbg:
    windowbg_label = Label(root, image=windowbg)
    windowbg_label.place(x=0, y=0, relwidth=1, relheight=1)
image_1 = load_image("sizebtnbg.png")
image_2 = load_image("sizebtnbg1.png")
image_3 = load_image("frontlogo.png")
image_4 = load_image("entrytopper1.png")
image_5 = load_image("entrytopper.png")
image_6 = load_image("info.png")
image_7 = load_image("homebtn.png")
image_8 = load_image("groupname.png")
image_D =  load_image("entrytopper1_Dnew.png")
image_DD = load_image("dynamicup.png")
image_first = load_image("entrytopper1_Dfirst.png")
image_best = load_image("entrytopper1_Dbest.png")

#BUTTONSCMM = load_image('BUTTONSCMM.png')
#BUTTONMPMM = load_image('BUTTONMPMM.png')
#BUTTONT3MM = load_image('BUTTONT3MM.png')
#BUTTONT4MM = load_image('BUTTONT4MM.png')
BUTTONOPT1 = load_image('HEADERB1.png')
BUTTONOPT2 = load_image('HEADERB2.png')
BUTTONOPT3 = load_image('HEADERB3.png')
BUTTONOPT4 = load_image('HEADERB4.png')
BUTTONSPEC1 = load_image('SPEC1.png')
BUTTONSPEC2 = load_image('SPEC2.png')
BUTTONSPEC3 = load_image('SPEC3.png')
BUTTONSPEC4 = load_image('SPEC4.png')

# *End of resources code block



# All the back end processes are hosted in this class.
class dynamic_firstFit_backEnd:
    def __init__( self ):
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        # summary table [ jobNum, startTime, finishTime, cpuWait ]
        self.summaryTable = {}
        self.allTime = []
        
        # Job Status [ allocated(True/False), finished(True/False), waiting ]
        self.jobStatus = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}
        self.memoryResults = []
        self.memoryResults_time = []

    # for printing data
    def print_data( self ):
        for x in self.memoryResults:
            print ( x )
        for x in self.memoryResults_time:
            print ( x[0].time(), x[1] )
        for x in list( self.summaryTable ):
            print( self.summaryTable[x][0], self.summaryTable[x][1].time(), self.summaryTable[x][2].time(), self.summaryTable[x][3] )
        return

    # for taking in the user's input into the backEnd class.
    def insert_inputs( self, memSpace, osSpace, jobDetails, memory ):
        self.memSpace = int(memSpace)
        self.osSpace = int(osSpace)
        self.memSize = int( memSpace)
        self.osSpace = int( osSpace )
        self.jobDetails = deepcopy( jobDetails )
        self.memory = deepcopy( memory )

        self.summaryTable = {}
        self.allTime = []
        # generates the all time list which will contain all the time that needs a memory map, fat, and pat.
        for job in self.jobDetails:
            self.tempTime = datetime.datetime.strptime( job[2], '%H:%M')
            self.allTime.append( self.tempTime )

        # job status [ isJobAllocated, isJobFinished, isJobWaiting ]
        self.jobStatus = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}

        # memoryResult will be used to store the data for every memory map.
        self.memoryResults = []
        # memoryResult_time will be used to store the time of every memory map.
        self.memoryResults_time = []
        return

    # returns memory list
    def get_memory( self ):
        return self.memory

    # returns summaryTable
    def get_summaryTable( self ):
        return self.summaryTable

    # returns the memoryResults
    def get_memoryResults( self ):
        return self.memoryResults

    # returns the memoryResults_time
    def get_memoryResults_time( self ):
        return self.memoryResults_time

    # for appending a certain memory list into the memory result
    def add_memoryResult( self, memory, time, timeStatus) :
        self.memoryResults.append( memory )
        self.memoryResults_time.append( [time, timeStatus] )
        return

    # sorts the list containing all the time that needs a memory result.
    def arrange_allTime( self ):
        self.allTime.sort()
        return

    # remove's the time that already have a memory result.
    def remove_time( self, time ):
        try:
            while True:
                self.allTime.remove(time)
        except ValueError:
            pass
        self.arrange_allTime()
        return

    # checks if the job fits into the available partitions.
    def check_jobFit( self, j_size ):
        # j_size: job size
        self.j_size = j_size
        # memorySpace[1]: F for free/available space and U if occupied by a certain job
        # memorySpace[0]: the size of the partition.
        for memorySpace in self.memory:
            if memorySpace[1] == "F" and memorySpace[0] > self.j_size:
                return True
        return False

    # checks a certain job's status.
    def check_jobStatus( self ):
        # checks if the jobs are already done.
        self.jobsDone = 0
        for jobNum in list(self.jobStatus):
            if self.jobStatus[jobNum][0] == True and self.jobStatus[jobNum][1]:
                self.jobsDone += 1
        if self.jobsDone == len( list(self.jobStatus) ):
            return True
        else:
            return False

    # allocates a job into a free/available partition.
    def allocate( self, memory, job ):
        # job [ job id, a/f( allocate/deallocate ), job size ]
        self.j_id = job[0]
        self.j_size = job[2]
        self.allocate_memory = memory
        # if the memory list is empty, immediately return
        if self.allocate_memory == None:
            return self.allocate_memory
        # i: id for the memory space/partition
        # m: F for free/available memory space,
        #    U for occupied memory space.
        # This loop traverses the memory list so that a job can be allocated to the 
        # first memory space which meets the needs of the job.
        for i, m in enumerate(self.allocate_memory):
            if m[1] == "F" and m[0] > self.j_size:
                self.allocate_memory.insert( i + 1, [m[0] - self.j_size, "F", -1])
                try:
                    if self.allocate_memory[i+2][1] == "F":
                        self.allocate_memory[i+1][0] += self.allocate_memory[i+2][0]
                        self.allocate_memory.pop(i+2)
                except IndexError:
                    pass

                m[0] = self.j_size
                m[1] = "U"
                m[2] = self.j_id
                return self.allocate_memory

    # for de-allocating a job out of the memory list.
    def recycle( self, memory, job ):
        self.recycle_memory = memory
        self.job = job
        # if the memory list is empty, immediately return
        if self.recycle_memory == None:
            return
        # i: id for the memory space/partition
        # m: F for free/available memory space,
        #    U for occupied memory space.
        # This loop traverses the memory list to de-allocate a job from the memory list
        # Furthermore, it also combines free memory spaces that are side by side.
        for i, m in enumerate( self.recycle_memory ):
            if m[2] == self.job[0] and m[1] == "U":
                m[1] = "F"
                m[2] = -1
                if i != 0 and self.recycle_memory[i-1][1] == "F":
                    self.recycle_memory[i-1][0] += m[0]
                    self.recycle_memory.remove(m)
                    if self.recycle_memory[i][1] == "F":
                        self.recycle_memory[i-1][0] += self.recycle_memory[i][0]
                        self.recycle_memory.pop(i)
                elif i != len(self.recycle_memory) and self.recycle_memory[i+1][1] == "F":
                    self.recycle_memory[i][0] += self.recycle_memory[i+1][0]
                    self.recycle_memory.remove( self.recycle_memory[i+1] )
        return self.recycle_memory
    
    # for generating the summary table.
    def generate_summaryTable( self ):
        self.isFinished = False
        self.arrange_allTime()
        
        while self.isFinished == False:
            # This block of code sets the needed parameters for the next process.
            # It resets the indicator 'actionTaken'. This indicator is used by the
            # program to determine if a job has been allocated/de-allocated in this iteration.
            # tempTimeStatus: contains the status of certain time periods. This could contain
            #                 job arrivals, job waiting, and job terminations.
            # currentTime: the time of a certain/this iteration.
            self.actionTaken = False
            self.tempTimeStatus = []
            try:
                self.arrange_allTime()
                self.currentTime = self.allTime[0]
            except:
                self.isFinished = True
                break
                

            # Checks if all the jobs are already finished. If it is, then stop the while loop.
            self.tempJobStatus = self.check_jobStatus()
            if self.tempJobStatus == True:
                self.isFinished = True
                break

            # Iterates through the job details to see what actions can be taken in this currentTime
            for job in self.jobDetails:
                self.jobFits = self.check_jobFit( job[0] )
                self.test_jobWaiting = True
                
                # If a certain job details from the self.jobDetails is deemed to waiting to be allocated
                # then, it will check if the currentTime meets the job's demand for allocation.
                if job[4] != False:
                    self.tempWaitUntil = job[4]
                    if self.currentTime == self.tempWaitUntil:
                        self.test_jobWaiting = False

                # If a certain job arrives, this nested condition will check whether the job needs to wait or is capable
                # of immediate allocation.
                if self.currentTime == datetime.datetime.strptime( job[2], '%H:%M') and self.jobStatus[job[1]][0] == False:
                    if self.jobFits == True:
                        self.tempTimeStatus.append( "Arrived(J{})".format( job[1] ) )
                    else:
                        self.tempTimeStatus.append( "Arrived/Wait(J{})".format( job[1] ) )
                        self.tempWaitUntil = self.tempFinishTime
                        job[4] = self.tempWaitUntil

                # This conditions checks if a certain actions could be taken.
                # The actions could be, the start/allocation or termination of certain job.
                if ( self.test_jobWaiting == False or self.currentTime == datetime.datetime.strptime( job[2], '%H:%M')) and self.jobStatus[job[1]][0] == False and self.jobFits == True:
                    self.memory = self.allocate( self.memory, [ job[1], "a" , job[0] ] )
                    self.jobStatus[job[1]][0] = True

                    self.tempStartTime = self.currentTime
                    if (self.tempStartTime - datetime.datetime.strptime( job[2], '%H:%M')).total_seconds() < 0:
                        self.tempCpuWait = "0:00:00"
                        self.tempStartTime = datetime.datetime.strptime( job[2], '%H:%M')
                    else:
                        self.tempCpuWait = self.tempStartTime - datetime.datetime.strptime( job[2], '%H:%M')
                    self.tempFinishTime = ( self.tempStartTime - self.time_zero + (datetime.datetime.strptime( job[3], '%H:%M')))
                    self.allTime.append( self.tempFinishTime )
                    self.summaryTable[job[1]] = [ job[1], self.tempStartTime, self.tempFinishTime, self.tempCpuWait ]

                    self.actionTaken = True
                    self.tempTimeStatus.append( "Started(J{})".format( job[1] ) )
                elif self.jobStatus[job[1]][0] == True and self.currentTime == self.summaryTable[job[1]][2]:
                    self.memory = self.recycle( self.memory, [ job[1], "f" , job[0] ] )
                    self.jobStatus[job[1]][1] = True
                    
                    self.actionTaken = True
                    self.tempTimeStatus.append( "Terminated(J{})".format( job[1] ) )
                else:
                    pass

            # copies the memory list of this currentTime
            self.memoryToAdd = deepcopy(self.memory)
            # appds the needed data into the memoryResult list.
            self.add_memoryResult( self.memoryToAdd, self.currentTime, deepcopy(self.tempTimeStatus) )

            # Checks if all the job are already finished. If not, then remove the current time from
            # the list of all time.
            self.tempJobStatus = self.check_jobStatus()
            if self.tempJobStatus == True:
                self.isFinished = True
                break
            else:
                self.remove_time( self.currentTime )
        
        # a miscellaneous command used for debugging.
        #self.print_data()


# Contains all the front end windows and functions
class dynamic_firstFit_frontEnd:
    def __init__( self ):
        self.memSpace = 640
        self.memSize = 640
        self.osSpace = 32
        self.osSize = 32
        # Job Details [ jobSize, jobNum, arrivalTime, runTime, isjobWaiting ]
        self.jobDetails = [ [ 10, 1, "9:00", "1:00", False],
                            [ 20, 2, "9:00", "1:00", False],
                            [ 30, 3, "9:00", "1:00", False],
                            [ 40, 4, "9:00", "1:00", False],
                            [ 50, 5, "9:00", "1:00", False]]

        self.memory = [[609,'F',-1]]
        
        self.firstFit_backEnd = dynamic_firstFit_backEnd()

        # insert_inputs( self, memSpace, osSpace, jobDetails, memory )
        self.firstFit_backEnd.insert_inputs( self.memSpace, self.osSpace, self.jobDetails, self.memory )
        self.firstFit_backEnd.generate_summaryTable()

        self.headNode = None

    # To clear the linked list of nodes.
    def clearNodes( self ):
        self.headNode = None
        return

    # To add a node into the linked list
    # ( self, memoryResult = None, memoryResult_time = None, osSize = None, memSize = None)
    def addResultNode( self, memoryResult, memoryResult_time, osSize, memSize ):
        memoryResult_time[0] = memoryResult_time[0].time()
        self.tempNode = dynamic_firstFitNode_frontEnd( memoryResult, memoryResult_time, osSize, memSize )

        if self.headNode == None:
            self.headNode = self.tempNode
        else:
            self.headNode.backPointer = self.tempNode
            self.tempNode.nextPointer = self.headNode

            self.headNode = self.tempNode
        return


    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass


    # This function returns True if timeInput is not in proper time format
    # Else, returns False if the input is in proper time format
    # Time format is HH:MM
    def isNotTimeFormat( self, timeInput):
        try:
            time.strptime( timeInput, '%H:%M')
            return False
        except ValueError:
            return True

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Poppins', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 7
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Poppins', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            self.physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Poppins', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 7
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Poppins', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 50, y = self.yCounter - 15)
            self.physicalMemWidgets.append( self.tempLBL )
        return

    def homepage(self):
        root.destroy()
        run(["python", "Single_Contig-Final.py"])

    # function which contains widget placements
    # this also takes in the user's input.
    def input1_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []

        self.bg1LBL = Label(root, image=bg4, bg="black")
        self.bg1LBL.place(x=0, y=100)
        self.basicWidgetList.append(self.bg1LBL)

        self.clockLBL = Label(root, font=('Poppins', 16), bg="#ffffff")
        self.clockLBL.place(x=730, y=165)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append(self.clockLBL)

        self.dateLBL = Label(root, font=('Poppins', 16), bg="#ffffff")
        self.dateLBL.place(x=730, y=125)
        self.current_date()
        self.basicWidgetList.append(self.dateLBL)

        self.jobLBL = Label(root, text="Job", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                            relief="raised")
        self.jobLBL.place(x=32, y=258)
        self.basicWidgetList.append(self.jobLBL)

        self.job1LBL = Label(root, text="1", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job1LBL.place(x=32, y=337)
        self.basicWidgetList.append(self.job1LBL)

        self.job2LBL = Label(root, text="2", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job2LBL.place(x=32, y=397)
        self.basicWidgetList.append(self.job2LBL)

        self.job3LBL = Label(root, text="3", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job3LBL.place(x=32, y=457)
        self.basicWidgetList.append(self.job3LBL)

        self.job4LBL = Label(root, text="4", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job4LBL.place(x=32, y=517)
        self.basicWidgetList.append(self.job4LBL)

        self.job5LBL = Label(root, text="5", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job5LBL.place(x=32, y=577)
        self.basicWidgetList.append(self.job5LBL)


        self.sizeLBL = Label(root, text="Size", font=('Poppins', 15), bg="#FFD53E", height=1, width=19, borderwidth=7,
                             relief="raised")
        self.sizeLBL.place(x=135, y=257)
        self.basicWidgetList.append(self.sizeLBL)

        self.size1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size1ENTRY.place(x=135, y=340)
        self.basicWidgetList.append(self.size1ENTRY)

        self.size2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size2ENTRY.place(x=135, y=400)
        self.basicWidgetList.append(self.size2ENTRY)

        self.size3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size3ENTRY.place(x=135, y=460)
        self.basicWidgetList.append(self.size3ENTRY)

        self.size4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size4ENTRY.place(x=135, y=520)
        self.basicWidgetList.append(self.size4ENTRY)

        self.size5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size5ENTRY.place(x=135, y=580)
        self.basicWidgetList.append(self.size5ENTRY)

        self.arrivalTimeLBL = Label(root, text="Arrival Time", font=('Poppins', 15), bg="#FFD53E", height=1, width=19,
                                    borderwidth=7, relief="raised")
        self.arrivalTimeLBL.place(x=390, y=257)
        self.basicWidgetList.append(self.arrivalTimeLBL)

        self.arrivalTime1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime1ENTRY.place(x=390, y=340)
        self.basicWidgetList.append(self.arrivalTime1ENTRY)

        self.arrivalTime2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime2ENTRY.place(x=390, y=400)
        self.basicWidgetList.append(self.arrivalTime2ENTRY)

        self.arrivalTime3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime3ENTRY.place(x=390, y=460)
        self.basicWidgetList.append(self.arrivalTime3ENTRY)

        self.arrivalTime4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime4ENTRY.place(x=390, y=520)
        self.basicWidgetList.append(self.arrivalTime4ENTRY)

        self.arrivalTime5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime5ENTRY.place(x=390, y=580)
        self.basicWidgetList.append(self.arrivalTime5ENTRY)

        self.runTimeLBL = Label(root, text="Run Time", font=('Poppins', 15), bg="#FFD53E", height=1, width=19,
                                borderwidth=7, relief="raised")
        self.runTimeLBL.place(x=640, y=257)
        self.basicWidgetList.append(self.runTimeLBL)

        self.runTime1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime1ENTRY.place(x=640, y=340)
        self.basicWidgetList.append(self.runTime1ENTRY)

        self.runTime2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime2ENTRY.place(x=640, y=400)
        self.basicWidgetList.append(self.runTime2ENTRY)

        self.runTime3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime3ENTRY.place(x=640, y=460)
        self.basicWidgetList.append(self.runTime3ENTRY)

        self.runTime4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime4ENTRY.place(x=640, y=520)
        self.basicWidgetList.append(self.runTime4ENTRY)

        self.runTime5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime5ENTRY.place(x=640, y=580)
        self.basicWidgetList.append(self.runTime5ENTRY)

        # img label for date and time
        self.datetimeSizeLBL = Label(root, image=image_2, borderwidth="0", highlightthickness="0", relief="flat",
                                activebackground="black", background="black")
        self.datetimeSizeLBL.place(x=585, y=120)
        self.basicWidgetList.append(self.datetimeSizeLBL)

        self.topper = Label(root, image=image_first, borderwidth="0", highlightthickness="0", relief="flat",
                            activebackground="black", background="black")
        self.topper.place(x=0, y=0)
        self.basicWidgetList.append(self.topper)

        self.memSizeENTRY = Entry(root, font=('Poppins', 13, 'bold'), justify="center", bg="#ffffff")
        self.memSizeENTRY.place(x=210, y=130)
        self.basicWidgetList.append(self.memSizeENTRY)

        self.osSizeLBL = Label(root, image=image_1, borderwidth="0", highlightthickness="0", relief="flat",
                               activebackground="black", background="black")
        self.osSizeLBL.place(x=68, y=120)
        self.basicWidgetList.append(self.osSizeLBL)

        self.osSizeENTRY = Entry(root, font=('Poppins', 13, 'bold'), justify="center", bg="#ffffff")
        self.osSizeENTRY.place(x=210, y=170)
        self.basicWidgetList.append(self.osSizeENTRY)

        self.computeBTN = Button(root, text='Compute', command=self.input1_computeBTN_Pressed,
                                 font=('Poppins', 16, 'bold'),
                                 width=12, bg="#eae2b7", height=1, borderwidth=5, relief="sunken")
        self.computeBTN.place(x=650, y=650)
        self.basicWidgetList.append(self.computeBTN)

        self.exitBTN = Button(root, text='Exit', font=('Poppins', 16, 'bold'), width=12, command = self.homepage,
                              activebackground="#f77f00", height=1, borderwidth=5, relief="sunken")
        self.exitBTN.place(x=80, y=650)
        self.basicWidgetList.append(self.exitBTN)


    # Executes once the user presses the compute button in the input1_window
    def input1_computeBTN_Pressed( self ):
        self.clearNodes()
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.size1 = self.size1ENTRY.get()
            self.size2 = self.size2ENTRY.get()
            self.size3 = self.size3ENTRY.get()
            self.size4 = self.size4ENTRY.get()
            self.size5 = self.size5ENTRY.get()

            self.memSize = self.memSizeENTRY.get()
            self.osSize = self.osSizeENTRY.get()

            self.memSize_Check = self.isNotInteger( self.memSize )
            self.osSize_Check = self.isNotInteger( self.osSize )
 
            self.size1_Check = self.isNotInteger( self.size1 )
            self.size2_Check = self.isNotInteger( self.size2 )
            self.size3_Check = self.isNotInteger( self.size3 )
            self.size4_Check = self.isNotInteger( self.size4 )
            self.size5_Check = self.isNotInteger( self.size5 )
            
            
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()

            self.arrivalTime1_Check = self.isNotTimeFormat( self.arrivalTime1 )
            self.arrivalTime2_Check = self.isNotTimeFormat( self.arrivalTime2 )
            self.arrivalTime3_Check = self.isNotTimeFormat( self.arrivalTime3 )
            self.arrivalTime4_Check = self.isNotTimeFormat( self.arrivalTime4 )
            self.arrivalTime5_Check = self.isNotTimeFormat( self.arrivalTime5 )

            self.runTime1 = self.runTime1ENTRY.get()
            self.runTime2 = self.runTime2ENTRY.get()
            self.runTime3 = self.runTime3ENTRY.get()
            self.runTime4 = self.runTime4ENTRY.get()
            self.runTime5 = self.runTime5ENTRY.get()
        
            self.runTime1_Check = self.isNotTimeFormat( self.runTime1 )
            self.runTime2_Check = self.isNotTimeFormat( self.runTime2 )
            self.runTime3_Check = self.isNotTimeFormat( self.runTime3 )
            self.runTime4_Check = self.isNotTimeFormat( self.runTime4 )
            self.runTime5_Check = self.isNotTimeFormat( self.runTime5 )

            # This condition checks whether the user's inputted values are acceptable.
            # If not, print the errors.
            if self.memSize_Check or self.osSize_Check :
                print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Memory or OS Size input." )
            elif int(self.memSize) < int(self.osSize):
                print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Compute Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.size1_Check or self.size2_Check or self.size3_Check or self.size4_Check or self.size5_Check:
                print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif (int(self.size1) > ( int(self.memSize) - int(self.osSize))) or (int(self.size2) > ( int(self.memSize) - int(self.osSize))) or (int(self.size3) > ( int(self.memSize) - int(self.osSize))) or (int(self.size4) > ( int(self.memSize) - int(self.osSize))) or (int(self.size5) > ( int(self.memSize) - int(self.osSize))):
                print ( "Error: Size input should not exceed ( Memory Size - OS Size )." )
                messagebox.showinfo( "Compute Error" , "Error: Size input should not exceed ( Memory Size - OS Size )." )
            elif self.arrivalTime1_Check or self.arrivalTime2_Check or self.arrivalTime3_Check or self.arrivalTime4_Check or self.arrivalTime5_Check:
                print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.runTime1_Check or self.runTime2_Check or self.runTime3_Check or self.runTime4_Check or self.runTime5_Check:
                print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                # Job Details [ jobSize, jobNum, arrivalTime, runTime, isjobWaiting ]
                # manipulates the user's input in a format that can be understood by the backEnd class.
                self.jobDetails = [ [ int(self.size1), 1, self.arrivalTime1, self.runTime1, False],
                                    [ int(self.size2), 2, self.arrivalTime2, self.runTime2, False],
                                    [ int(self.size3), 3, self.arrivalTime3, self.runTime3, False],
                                    [ int(self.size4), 4, self.arrivalTime4, self.runTime4, False],
                                    [ int(self.size5), 5, self.arrivalTime5, self.runTime5, False]]
                # Memory [ sizeTaken, F/U( Free,Taken ), -1/jobNum ]
                self.memory = [[( int(self.memSize) - int(self.osSize) ) + 1,'F',-1]]
                # insert_inputs( self, memSpace, osSpace, jobDetails, memory )
                self.firstFit_backEnd.insert_inputs( self.memSize, self.osSize, self.jobDetails, self.memory )
                self.firstFit_backEnd.generate_summaryTable()
                self.summaryTable_window()


    # the window which displays the summary table
    def summaryTable_window( self ):
        self.summaryTable = deepcopy(self.firstFit_backEnd.get_summaryTable())
        self.clearWidgets()
        self.basicWidgetList = []

        self.bg1LBL = Label(root, image=bg4, bg="black")
        self.bg1LBL.place(x=0, y=100)
        self.basicWidgetList.append(self.bg1LBL)

        self.clockLBL = Label(root, font=('Poppins', 15), bg="#eec894")
        self.clockLBL.place(x=730, y=155)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append(self.clockLBL)

        self.dateLBL = Label(root, font=('Poppins', 15), bg="#eec894")
        self.dateLBL.place(x=730, y=115)
        self.current_date()
        self.basicWidgetList.append(self.dateLBL)

        self.datetimeSizeLBL = Label(root, image=image_2, borderwidth="0", highlightthickness="0", relief="flat",
                                     activebackground="black", background="black")
        self.datetimeSizeLBL.place(x=585, y=110)
        self.basicWidgetList.append(self.datetimeSizeLBL)

        self.osSizeLBL = Label(root, image=image_1, borderwidth="0", highlightthickness="0", relief="flat",
                               activebackground="black", background="black")
        self.osSizeLBL.place(x=68, y=110)
        self.basicWidgetList.append(self.osSizeLBL)

        self.memSizeDisplay = Label(root, text=self.memSize, width=10, font=('Poppins', 13, 'bold'), justify="center",
                                    bg="#eec894")
        self.memSizeDisplay.place(x=210, y=110)
        self.basicWidgetList.append(self.memSizeDisplay)

        self.osSizeDisplay = Label(root, text=self.osSize, width=10, font=('Poppins', 13, 'bold'), justify="center",
                                   bg="#eec894")
        self.osSizeDisplay.place(x=210, y=160)
        self.basicWidgetList.append(self.osSizeDisplay)

        self.jobLBL = Label(root, text="Job", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                            relief="raised")
        self.jobLBL.place(x=32, y=230)
        self.basicWidgetList.append(self.jobLBL)

        self.job1LBL = Label(root, text="1", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job1LBL.place(x=32, y=307)
        self.basicWidgetList.append(self.job1LBL)

        self.job2LBL = Label(root, text="2", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job2LBL.place(x=32, y=377)
        self.basicWidgetList.append(self.job2LBL)

        self.job3LBL = Label(root, text="3", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job3LBL.place(x=32, y=447)
        self.basicWidgetList.append(self.job3LBL)

        self.job4LBL = Label(root, text="4", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job4LBL.place(x=32, y=517)
        self.basicWidgetList.append(self.job4LBL)

        self.job5LBL = Label(root, text="5", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7,
                             relief="raised")
        self.job5LBL.place(x=32, y=587)
        self.basicWidgetList.append(self.job5LBL)

        # Start Time Widgets
        self.startTimeLBL = Label(root, text="Start Time", font=('Poppins', 15), bg="#FFD53E", height=1, width=19,
                                  borderwidth=7, relief="raised")
        self.startTimeLBL.place(x=130, y=230)
        self.basicWidgetList.append(self.startTimeLBL)

        self.startTime1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime1ENTRY.place(x=130, y=310)
        self.startTime1ENTRY.insert(0, self.summaryTable[1][1].time())
        self.startTime1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime1ENTRY)

        self.startTime2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime2ENTRY.place(x=130, y=380)
        self.startTime2ENTRY.insert(0, self.summaryTable[2][1].time())
        self.startTime2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime2ENTRY)

        self.startTime3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime3ENTRY.place(x=130, y=450)
        self.startTime3ENTRY.insert(0, self.summaryTable[3][1].time())
        self.startTime3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime3ENTRY)

        self.startTime4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime4ENTRY.place(x=130, y=520)
        self.startTime4ENTRY.insert(0, self.summaryTable[4][1].time())
        self.startTime4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime4ENTRY)

        self.startTime5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime5ENTRY.place(x=130, y=590)
        self.startTime5ENTRY.insert(0, self.summaryTable[5][1].time())
        self.startTime5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime5ENTRY)

        # Finish Time Widgets
        self.finishTimeLBL = Label(root, text="Finish Time", font=('Poppins', 15), bg="#FFD53E", height=1, width=19,
                                   borderwidth=7, relief="raised")
        self.finishTimeLBL.place(x=380, y=230)
        self.basicWidgetList.append(self.finishTimeLBL)

        self.finishTime1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime1ENTRY.place(x=380, y=310)
        self.finishTime1ENTRY.insert(0, self.summaryTable[1][2].time())
        self.finishTime1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime1ENTRY)

        self.finishTime2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime2ENTRY.place(x=380, y=380)
        self.finishTime2ENTRY.insert(0, self.summaryTable[2][2].time())
        self.finishTime2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime2ENTRY)

        self.finishTime3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime3ENTRY.place(x=380, y=450)
        self.finishTime3ENTRY.insert(0, self.summaryTable[3][2].time())
        self.finishTime3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime3ENTRY)

        self.finishTime4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime4ENTRY.place(x=380, y=520)
        self.finishTime4ENTRY.insert(0, self.summaryTable[4][2].time())
        self.finishTime4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime4ENTRY)

        self.finishTime5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime5ENTRY.place(x=380, y=590)
        self.finishTime5ENTRY.insert(0, self.summaryTable[5][2].time())
        self.finishTime5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime5ENTRY)

        # CPU Wait Widgets
        self.cpuWaitLBL = Label(root, text="CPU Wait", font=('Poppins', 15), bg="#FFD53E", height=1, width=19,
                                borderwidth=7, relief="raised")
        self.cpuWaitLBL.place(x=630, y=230)
        self.basicWidgetList.append(self.cpuWaitLBL)

        self.cpuWait1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait1ENTRY.place(x=630, y=310)
        self.cpuWait1ENTRY.insert(0, self.summaryTable[1][3])
        self.cpuWait1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait1ENTRY)

        self.cpuWait2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait2ENTRY.place(x=630, y=380)
        self.cpuWait2ENTRY.insert(0, self.summaryTable[2][3])
        self.cpuWait2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait2ENTRY)

        self.cpuWait3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait3ENTRY.place(x=630, y=450)
        self.cpuWait3ENTRY.insert(0, self.summaryTable[3][3])
        self.cpuWait3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait3ENTRY)

        self.cpuWait4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait4ENTRY.place(x=630, y=520)
        self.cpuWait4ENTRY.insert(0, self.summaryTable[4][3])
        self.cpuWait4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait4ENTRY)

        self.cpuWait5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait5ENTRY.place(x=630, y=590)
        self.cpuWait5ENTRY.insert(0, self.summaryTable[5][3])
        self.cpuWait5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait5ENTRY)

        self.topper1 = Label(root, image=image_first, borderwidth="0", highlightthickness="0", relief="flat",
                             activebackground="black", background="black")
        self.topper1.place(x=0, y=0)
        self.basicWidgetList.append(self.topper1)

        # Buttons
        self.backBTN = Button(root, text='BACK', command=self.input1_window, font=('Poppins', 16, 'bold'), width=12,
                              bg="#f3e9dc", height=1, borderwidth=5, relief="sunken")
        self.backBTN.place(x=70, y=650)
        self.basicWidgetList.append(self.backBTN)

        self.nextBTN = Button(root, text='NEXT', command=self.summaryTable_nextBTN_Pressed,
                              font=('Poppins', 16, 'bold'), width=12, bg="#f77f00",  height=1, borderwidth=5, relief="sunken")
        self.nextBTN.place(x=680, y=650)
        self.basicWidgetList.append(self.nextBTN)

        self.exitBTN = Button(root, text='Exit', command = self.homepage, font=('Poppins', 16, 'bold'), width=12,
                              bg="#eae2b7",  height=1, borderwidth=5, relief="sunken")
        self.exitBTN.place(x=250, y=650)
        self.basicWidgetList.append(self.exitBTN)

    # This executes if the user presses the next button in the summaryTable window.
    def summaryTable_nextBTN_Pressed( self ):
        self.headNode = None
        self.tempMemoryResults = deepcopy(self.firstFit_backEnd.get_memoryResults())
        self.tempMemoryResults_time = deepcopy(self.firstFit_backEnd.get_memoryResults_time())
        for i in range(len( self.tempMemoryResults ) - 1, -1, -1):
            self.addResultNode( self.tempMemoryResults[i], self.tempMemoryResults_time[i], self.osSize, self.memSize )
        if self.headNode != None:
            self.headNode.memMap_window()
        

# This is a node class for the linked list
# the linked list contains the nodes which hosts the memory map, fat, and pat windows.
class dynamic_firstFitNode_frontEnd:
    def __init__ ( self, memoryResult = None, memoryResult_time = None, osSize = None, memSize = None):
        self.backPointer = None
        self.nextPointer = None
        self.patData = []
        self.fatData = []
        self.location = 0
        
        if memoryResult == None:
            self.memoryResult = [[500, "U", 1], [109, "F", -1]]
        else:
            self.memoryResult = memoryResult
                   
        if memoryResult_time == None:
            self.memoryResult_time = [ "09:00:00", ["Arrived(J1)", "Started(J1)"]]
        else:
            self.memoryResult_time = memoryResult_time

        if osSize == None:
            self.osSize = 32
        else:
            self.osSize = int(osSize)

        if memSize == None:
            self.memSize = 640
        else:
            self.memSize = int(memSize)

        self.location += int(self.osSize)
        self.tempColors = [ "#9AE3B7", "#E6CDA3", "#F2EAC4", "#F0A8A8", "#EAB0E3", "#95DBDA", "#9BAADD"]
        self.tempColorCounter = 0
        self.tempPercentage = float(( float(self.osSize) / float(self.memSize) ) * 100 )
        self.memMap_data = [ [ self.tempPercentage, "#B1BECD", "OS Size", self.tempPercentage, self.location, self.osSize ] ]
        self.availableCounter = 1
        self.pCounter = 1
        for certainResult in self.memoryResult:
            if certainResult[1] == "U":
                if self.location+certainResult[0] > self.memSize:
                    self.patData.append( [ certainResult[0] - 1, self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                else:
                    self.patData.append( [ certainResult[0], self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                self.location += int(certainResult[0])
                self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Allocated(P{})".format(self.pCounter), self.tempPercentage, self.location, certainResult[0] ])
                self.tempColorCounter += 1
                self.pCounter += 1
            else:
                if self.location+certainResult[0] > self.memSize:
                    self.fatData.append( [ certainResult[0] - 1, self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                    self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Available(F{})".format(self.availableCounter), self.tempPercentage, self.location - 1, certainResult[0] - 1 ])
                else:
                    self.fatData.append( [ certainResult[0], self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                    self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Available(F{})".format(self.availableCounter), self.tempPercentage, self.location, certainResult[0] ])
                    
                self.tempColorCounter += 1
                self.availableCounter += 1


        self.countPatData = len( self.patData )
        if self.countPatData != 5:
            for i in range( 5 - self.countPatData ):
                self.patData.append( ["---", "---", "---"] )
        self.countFatData = len( self.fatData )
        if self.countFatData != 5:
            for i in range( 5 - self.countFatData ):
                self.fatData.append( ["---", "---", "---"] )

        #print( self.memMap_data )
        #print( self.fatData )

        self.memMap_data2 = deepcopy( self.memMap_data )
        self.tempCount = len( self.memMap_data2 )
        if self.tempCount != 7:
            for i in range( 7 - self.tempCount ):
                self.memMap_data2.append([ "---", "#c6e3ad", "---", "---", "---", "---" ])
        # displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize, memSize )

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

            
    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Poppins', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 7
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Poppins', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            self.physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Poppins', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 7
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize ,  bg = "#E8C39E", relief = "ridge", width = 5)
            self.tempLBL.place(x = 25, y = self.yCounter - 15)
            self.physicalMemWidgets.append( self.tempLBL )

        return

    def homepage(self):
        root.destroy()
        run(["python", "Single_Contig-Final.py"])


    def memMap_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg1LBL = Label(root, image = bg4, bg= "black")
        self.bg1LBL.place(x=0, y=100)
        self.basicWidgetList.append(self.bg1LBL)

        self.topper = Label(root, image=image_first, borderwidth="0", highlightthickness="0", relief="flat",
                            activebackground="black", background="black")
        self.topper.place(x=0, y=0)
        self.basicWidgetList.append(self.topper)

        self.title3LBL  =  Label( root , text = "Physical Memory Map" , font = ('Poppins', 15, 'bold'), height=1, width=74, borderwidth=5, relief="groove", bg = "#e8dcb5")
        self.title3LBL.place(x = 0, y = 60)
        self.basicWidgetList.append( self.title3LBL )

        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Poppins', 12),  bg = "#faf0dc", relief = "ridge", width=15)
        self.title4LBL.place(x = 615, y = 120)
        self.basicWidgetList.append( self.title4LBL )
        
        self.physicalMemWidgets = []
        self.yCounter = 140
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Poppins', 10),  bg = "#E8C39E", relief = "ridge", width = 5)
        self.markLBL.place(x = 25, y = self.yCounter - 20)
        self.physicalMemWidgets.append( self.markLBL )

        for tempData in self.memMap_data:
            self.displayMap( tempData[0], tempData[1], tempData[2], tempData[3], tempData[4] )

        self.partitionLBL = Label(root, text="Number", font=('Poppins', 15), bg="#FFB448", relief="raised",
                                  borderwidth=2, width=7)
        self.partitionLBL.place(x=460, y=160)
        self.basicWidgetList.append(self.partitionLBL)

        self.partition1LBL = Label(root, text="1", font=('Poppins', 15), bg=self.memMap_data2[0][1], relief="groove",
                                   width=7)
        self.partition1LBL.place(x=460, y=210)
        self.basicWidgetList.append(self.partition1LBL)

        self.partition2LBL = Label(root, text="2", font=('TPoppins', 15), bg=self.memMap_data2[1][1], relief="groove",
                                   width=7)
        self.partition2LBL.place(x=460, y=260)
        self.basicWidgetList.append(self.partition2LBL)

        self.partition3LBL = Label(root, text="3", font=('Poppins', 15), bg=self.memMap_data2[2][1], relief="groove",
                                   width=7)
        self.partition3LBL.place(x=460, y=310)
        self.basicWidgetList.append(self.partition3LBL)

        self.partition4LBL = Label(root, text="4", font=('TPoppins', 15), bg=self.memMap_data2[3][1], relief="groove",
                                   width=7)
        self.partition4LBL.place(x=460, y=360)
        self.basicWidgetList.append(self.partition4LBL)

        self.partition5LBL = Label(root, text="5", font=('TPoppins', 15), bg=self.memMap_data2[4][1], relief="groove",
                                   width=7)
        self.partition5LBL.place(x=460, y=410)
        self.basicWidgetList.append(self.partition5LBL)

        self.partition6LBL = Label(root, text="6", font=('Poppins', 15), bg=self.memMap_data2[5][1], relief="groove",
                                   width=7)
        self.partition6LBL.place(x=460, y=460)
        self.basicWidgetList.append(self.partition6LBL)

        self.partition7LBL = Label(root, text="7", font=('Poppins', 15), bg=self.memMap_data2[6][1], relief="groove",
                                   width=7)
        self.partition7LBL.place(x=460, y=510)
        self.basicWidgetList.append(self.partition7LBL)


        # Size Widgets
        self.sizeLBL = Label(root, text="Size", font=('Poppins', 15), bg="#FFB448", relief="raised", borderwidth=2,
                             width=12)
        self.sizeLBL.place(x=560, y=160)
        self.basicWidgetList.append(self.sizeLBL)

        self.size1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=12, bg="#eccbab")
        self.size1ENTRY.place(x=560, y=210)
        self.size1ENTRY.insert(0, self.memMap_data2[0][5])
        self.size1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.size1ENTRY)

        self.size2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#eaccad", width=12)
        self.size2ENTRY.place(x=560, y=260)
        self.size2ENTRY.insert(0, self.memMap_data2[1][5])
        self.size2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.size2ENTRY)

        self.size3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#eaccad", width=12)
        self.size3ENTRY.place(x=560, y=310)
        self.size3ENTRY.insert(0, self.memMap_data2[2][5])
        self.size3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.size3ENTRY)

        self.size4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#eaccad", width=12)
        self.size4ENTRY.place(x=560, y=360)
        self.size4ENTRY.insert(0, self.memMap_data2[3][5])
        self.size4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.size4ENTRY)

        self.size5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#eaccad", width=12)
        self.size5ENTRY.place(x=560, y=410)
        self.size5ENTRY.insert(0, self.memMap_data2[4][5])
        self.size5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.size5ENTRY)

        self.size6ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#eaccad", width=12)
        self.size6ENTRY.place(x=560, y=460)
        self.size6ENTRY.insert(0, self.memMap_data2[5][5])
        self.size6ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.size6ENTRY)

        self.size7ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#eaccad", width=12)
        self.size7ENTRY.place(x=560, y=510)
        self.size7ENTRY.insert(0, self.memMap_data2[6][5])
        self.size7ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.size7ENTRY)

        # Status Widgets
        self.statusLBL = Label(root, text="Status", font=('Poppins', 15), bg="#FFB448", relief="raised", borderwidth=2,
                               width=14)
        self.statusLBL.place(x=720, y=160)
        self.basicWidgetList.append(self.statusLBL)

        self.status1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#e8c39e", width=14)
        self.status1ENTRY.place(x=720, y=210)
        self.status1ENTRY.insert(0, self.memMap_data2[0][2])
        self.status1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.status1ENTRY)

        self.status2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#e8c39e", width=14)
        self.status2ENTRY.place(x=720, y=260)
        self.status2ENTRY.insert(0, self.memMap_data2[1][2])
        self.status2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.status2ENTRY)

        self.status3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#e8c39e", width=14)
        self.status3ENTRY.place(x=720, y=310)
        self.status3ENTRY.insert(0, self.memMap_data2[2][2])
        self.status3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.status3ENTRY)

        self.status4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#e8c39e", width=14)
        self.status4ENTRY.place(x=720, y=360)
        self.status4ENTRY.insert(0, self.memMap_data2[3][2])
        self.status4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.status4ENTRY)

        self.status5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#e8c39e", width=14)
        self.status5ENTRY.place(x=720, y=410)
        self.status5ENTRY.insert(0, self.memMap_data2[4][2])
        self.status5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.status5ENTRY)

        self.status6ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#e8c39e", width=14)
        self.status6ENTRY.place(x=720, y=460)
        self.status6ENTRY.insert(0, self.memMap_data2[5][2])
        self.status6ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.status6ENTRY)

        self.status7ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", bg="#e8c39e", width=14)
        self.status7ENTRY.place(x=720, y=510)
        self.status7ENTRY.insert(0, self.memMap_data2[6][2])
        self.status7ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.status7ENTRY)

        self.backBTN  =  Button ( root , text = 'BACK',command = self.memMap_backBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#f3e9dc" )
        self.backBTN.place (x=70, y=650)
        self.basicWidgetList.append( self.backBTN )

        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.pat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#f77f00" )
        self.nextBTN.place (x=680, y=650)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = self.homepage , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#eae2b7" )
        self.exitBTN.place (x=250, y=650)
        self.basicWidgetList.append( self.exitBTN )

    def memMap_backBTN_Pressed( self ):
        if self.backPointer != None:
            self.backPointer.fat_window()
        else:
            frontEnd.summaryTable_window()

    def pat_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []

        self.bg1LBL = Label(root, image=bg4, bg="black")
        self.bg1LBL.place(x=0, y=100)
        self.basicWidgetList.append(self.bg1LBL)

        self.topper = Label(root, image=image_first, borderwidth="0", highlightthickness="0", relief="flat",
                            activebackground="black", background="black")
        self.topper.place(x=0, y=0)
        self.basicWidgetList.append(self.topper)

        self.title3LBL = Label(root, text="Partition Allocation Table", font=('Poppins', 15, 'bold'), height=1,
                               width=74, borderwidth=5, relief="groove", bg="#e8dcb5")
        self.title3LBL.place(x=0, y=60)
        self.basicWidgetList.append(self.title3LBL)

        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Poppins', 14),  bg = "#faf0dc", relief = "ridge", width=15)
        self.title4LBL.place(x = 400, y = 120)
        self.basicWidgetList.append( self.title4LBL )
        

        # PAT Number Widgets
        self.patNumLBL = Label(root, text="Partition No.", font=('Poppins', 15), bg="#FFB448", relief="raised",
                               borderwidth=2, width=12)
        self.patNumLBL.place(x=70, y=180)
        self.basicWidgetList.append(self.patNumLBL)

        self.patNum1LBL = Label(root, text="1", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.patNum1LBL.place(x=70, y=220)
        self.basicWidgetList.append(self.patNum1LBL)

        self.patNum2LBL = Label(root, text="2", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.patNum2LBL.place(x=70, y=260)
        self.basicWidgetList.append(self.patNum2LBL)

        self.patNum3LBL = Label(root, text="3", font=('TPoppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.patNum3LBL.place(x=70, y=300)
        self.basicWidgetList.append(self.patNum3LBL)

        self.patNum4LBL = Label(root, text="4", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.patNum4LBL.place(x=70, y=340)
        self.basicWidgetList.append(self.patNum4LBL)

        self.patNum5LBL = Label(root, text="5", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.patNum5LBL.place(x=70, y=380)
        self.basicWidgetList.append(self.patNum5LBL)
        
        # PAT Size Widgets
        self.patSizeLBL = Label(root, text="Size", font=('Poppins', 15), bg="#FFB448", relief="raised", borderwidth=2,
                                width=14, justify="center")
        self.patSizeLBL.place(x=257, y=180)
        self.basicWidgetList.append(self.patSizeLBL)

        self.patSize1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patSize1ENTRY.place(x=257, y=220)
        self.patSize1ENTRY.insert(0, self.patData[0][0])
        self.patSize1ENTRY.config(state="readonly", bg="#987856")
        self.basicWidgetList.append(self.patSize1ENTRY)

        self.patSize2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patSize2ENTRY.place(x=257, y=260)
        self.patSize2ENTRY.insert(0, self.patData[1][0])
        self.patSize2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patSize2ENTRY)

        self.patSize3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patSize3ENTRY.place(x=257, y=300)
        self.patSize3ENTRY.insert(0, self.patData[2][0])
        self.patSize3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patSize3ENTRY)

        self.patSize4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patSize4ENTRY.place(x=257, y=340)
        self.patSize4ENTRY.insert(0, self.patData[3][0])
        self.patSize4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patSize4ENTRY)

        self.patSize5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patSize5ENTRY.place(x=257, y=380)
        self.patSize5ENTRY.insert(0, self.patData[4][0])
        self.patSize5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patSize5ENTRY)

        # PAT Location Widgets
        self.patLocationLBL = Label(root, text="Location", font=('Poppins', 15), bg="#FFB448", relief="raised",
                                    borderwidth=2, width=14, justify="center")
        self.patLocationLBL.place(x=490, y=180)
        self.basicWidgetList.append(self.patLocationLBL)

        self.patLocation1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patLocation1ENTRY.place(x=490, y=220)
        self.patLocation1ENTRY.insert(0, self.patData[0][1])
        self.patLocation1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patLocation1ENTRY)

        self.patLocation2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patLocation2ENTRY.place(x=490, y=260)
        self.patLocation2ENTRY.insert(0, self.patData[1][1])
        self.patLocation2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patLocation2ENTRY)

        self.patLocation3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patLocation3ENTRY.place(x=490, y=300)
        self.patLocation3ENTRY.insert(0, self.patData[2][1])
        self.patLocation3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patLocation3ENTRY)

        self.patLocation4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patLocation4ENTRY.place(x=490, y=340)
        self.patLocation4ENTRY.insert(0, self.patData[3][1])
        self.patLocation4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patLocation4ENTRY)

        self.patLocation5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patLocation5ENTRY.place(x=490, y=380)
        self.patLocation5ENTRY.insert(0, self.patData[4][1])
        self.patLocation5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patLocation5ENTRY)

        # PAT Status Widgets
        self.patStatusLBL = Label(root, text="Status", font=('Poppins', 15), bg="#FFB448", relief="raised",
                                  borderwidth=2, width=14, justify="center")
        self.patStatusLBL.place(x=700, y=180)
        self.basicWidgetList.append(self.patStatusLBL)

        self.patStatus1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patStatus1ENTRY.place(x=700, y=220)
        self.patStatus1ENTRY.insert(0, self.patData[0][2])
        self.patStatus1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patStatus1ENTRY)

        self.patStatus2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patStatus2ENTRY.place(x=700, y=260)
        self.patStatus2ENTRY.insert(0, self.patData[1][2])
        self.patStatus2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patStatus2ENTRY)

        self.patStatus3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patStatus3ENTRY.place(x=700, y=300)
        self.patStatus3ENTRY.insert(0, self.patData[2][2])
        self.patStatus3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patStatus3ENTRY)

        self.patStatus4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patStatus4ENTRY.place(x=700, y=340)
        self.patStatus4ENTRY.insert(0, self.patData[3][2])
        self.patStatus4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patStatus4ENTRY)

        self.patStatus5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.patStatus5ENTRY.place(x=700, y=380)
        self.patStatus5ENTRY.insert(0, self.patData[4][2])
        self.patStatus5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.patStatus5ENTRY)

        # Listbox Widgets

        self.patListbox1 = Listbox( root, height = 6, width = 30, border = 0, justify = "center" , bg="#FDFDD2", font=('Poppins', 12))
        self.patListbox1.place( x = 150, y = 460 )
        self.basicWidgetList.append( self.patListbox1 )
        self.patListbox2 = Listbox( root, height = 6, width = 30, border = 0, justify = "center" , bg="#FFF5BD", font=('Poppins', 12))
        self.patListbox2.place( x = 500, y = 460 )
        self.basicWidgetList.append( self.patListbox2 )

        self.tempCount1 = 0
        self.tempCount2 = 0
        for allocation in self.memoryResult_time[1]:
            if allocation[0] == "A":
                self.tempCount1 += 1
                self.patListbox1.insert( self.tempCount1, allocation )
            else:
                self.tempCount2 += 1
                self.patListbox2.insert( self.tempCount2, allocation )

        # Buttons
        self.backBTN  =  Button ( root , text = 'Back',command = self.memMap_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#f3e9dc" )
        self.backBTN.place (x=70, y=650)
        self.basicWidgetList.append( self.backBTN )

        self.nextBTN  =  Button ( root , text = 'Next',command = self.fat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#f77f00" )
        self.nextBTN.place (x=680, y=650)
        self.basicWidgetList.append( self.nextBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = self.homepage , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#eae2b7" )
        self.exitBTN.place (x=250, y=650)
        self.basicWidgetList.append( self.exitBTN )


    def fat_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []

        self.bg1LBL = Label(root, image=bg4, bg="black")
        self.bg1LBL.place(x=0, y=100)
        self.basicWidgetList.append(self.bg1LBL)

        self.topper = Label(root, image=image_first, borderwidth="0", highlightthickness="0", relief="flat",
                            activebackground="black", background="black")
        self.topper.place(x=0, y=0)
        self.basicWidgetList.append(self.topper)

        self.title3LBL = Label(root, text="Free Area Table", font=('Poppins', 15, 'bold'), height=1,
                               width=74, borderwidth=5, relief="groove", bg="#e8dcb5")
        self.title3LBL.place(x=0, y=60)
        self.basicWidgetList.append(self.title3LBL)

        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Poppins', 15), bg = "#faf0dc", relief = "ridge", width=15)
        self.title4LBL.place(x = 400, y = 120)
        self.basicWidgetList.append( self.title4LBL )

        # fat Number Widgets
        self.fatNumLBL = Label(root, text="Free Area No.", font=('Poppins', 15), bg="#FFB448", relief="ridge", width=12)
        self.fatNumLBL.place(x=70, y=180)
        self.basicWidgetList.append(self.fatNumLBL)

        self.fatNum1LBL = Label(root, text="1", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.fatNum1LBL.place(x=70, y=220)
        self.basicWidgetList.append(self.fatNum1LBL)

        self.fatNum2LBL = Label(root, text="2", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.fatNum2LBL.place(x=70, y=260)
        self.basicWidgetList.append(self.fatNum2LBL)

        self.fatNum3LBL = Label(root, text="3", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.fatNum3LBL.place(x=70, y=300)
        self.basicWidgetList.append(self.fatNum3LBL)

        self.fatNum4LBL = Label(root, text="4", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.fatNum4LBL.place(x=70, y=340)
        self.basicWidgetList.append(self.fatNum4LBL)

        self.fatNum5LBL = Label(root, text="5", font=('Poppins', 15), bg="#fff6dd", relief="groove", width=12)
        self.fatNum5LBL.place(x=70, y=380)
        self.basicWidgetList.append(self.fatNum5LBL)

        # fat Size Widgets
        self.fatSizeLBL = Label(root, text="Size", font=('Poppins', 15), bg="#FFB448", relief="raised", borderwidth=2,
                                width=14, justify="center")
        self.fatSizeLBL.place(x=257, y=180)
        self.basicWidgetList.append(self.fatSizeLBL)

        self.fatSize1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatSize1ENTRY.place(x=257, y=220)
        self.fatSize1ENTRY.insert(0, self.fatData[0][0])
        self.fatSize1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatSize1ENTRY)

        self.fatSize2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatSize2ENTRY.place(x=257, y=260)
        self.fatSize2ENTRY.insert(0, self.fatData[1][0])
        self.fatSize2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatSize2ENTRY)

        self.fatSize3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatSize3ENTRY.place(x=257, y=300)
        self.fatSize3ENTRY.insert(0, self.fatData[2][0])
        self.fatSize3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatSize3ENTRY)

        self.fatSize4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatSize4ENTRY.place(x=257, y=340)
        self.fatSize4ENTRY.insert(0, self.fatData[3][0])
        self.fatSize4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatSize4ENTRY)

        self.fatSize5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatSize5ENTRY.place(x=257, y=380)
        self.fatSize5ENTRY.insert(0, self.fatData[4][0])
        self.fatSize5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatSize5ENTRY)

        # fat Location Widgets
        self.fatLocationLBL = Label(root, text="Location", font=('Poppins', 15), bg="#FFB448", relief="raised",
                                    borderwidth=2, width=14, justify="center")
        self.fatLocationLBL.place(x=490, y=180)
        self.basicWidgetList.append(self.fatLocationLBL)

        self.fatLocation1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatLocation1ENTRY.place(x=490, y=220)
        self.fatLocation1ENTRY.insert(0, self.fatData[0][1])
        self.fatLocation1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatLocation1ENTRY)

        self.fatLocation2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatLocation2ENTRY.place(x=490, y=260)
        self.fatLocation2ENTRY.insert(0, self.fatData[1][1])
        self.fatLocation2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatLocation2ENTRY)

        self.fatLocation3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatLocation3ENTRY.place(x=490, y=300)
        self.fatLocation3ENTRY.insert(0, self.fatData[2][1])
        self.fatLocation3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatLocation3ENTRY)

        self.fatLocation4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatLocation4ENTRY.place(x=490, y=340)
        self.fatLocation4ENTRY.insert(0, self.fatData[3][1])
        self.fatLocation4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatLocation4ENTRY)

        self.fatLocation5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatLocation5ENTRY.place(x=490, y=380)
        self.fatLocation5ENTRY.insert(0, self.fatData[4][1])
        self.fatLocation5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatLocation5ENTRY)

        # fat Status Widgets
        self.fatStatusLBL = Label(root, text="Status", font=('Poppins', 15), bg="#FFB448", relief="raised",
                                  borderwidth=2, width=14, justify="center")
        self.fatStatusLBL.place(x=700, y=180)
        self.basicWidgetList.append(self.fatStatusLBL)

        self.fatStatus1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatStatus1ENTRY.place(x=700, y=220)
        self.fatStatus1ENTRY.insert(0, self.fatData[0][2])
        self.fatStatus1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatStatus1ENTRY)

        self.fatStatus2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatStatus2ENTRY.place(x=700, y=260)
        self.fatStatus2ENTRY.insert(0, self.fatData[1][2])
        self.fatStatus2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatStatus2ENTRY)

        self.fatStatus3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatStatus3ENTRY.place(x=700, y=300)
        self.fatStatus3ENTRY.insert(0, self.fatData[2][2])
        self.fatStatus3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatStatus3ENTRY)

        self.fatStatus4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatStatus4ENTRY.place(x=700, y=340)
        self.fatStatus4ENTRY.insert(0, self.fatData[3][2])
        self.fatStatus4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatStatus4ENTRY)

        self.fatStatus5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center", width=14)
        self.fatStatus5ENTRY.place(x=700, y=380)
        self.fatStatus5ENTRY.insert(0, self.fatData[4][2])
        self.fatStatus5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.fatStatus5ENTRY)

        # Listbox Widgets

        self.fatListbox1 = Listbox( root, height = 6, width = 30, border = 0, justify = "center", bg="#FDFDD2", font=('Poppins', 12)  )
        self.fatListbox1.place(x=150, y=470)
        self.basicWidgetList.append( self.fatListbox1 )
        self.fatListbox2 = Listbox( root, height = 6, width = 30, border = 0, justify = "center" , bg= "#FFF5BD", font=('Poppins', 12))
        self.fatListbox2.place( x = 500, y = 470 )
        self.basicWidgetList.append( self.fatListbox2 )

        self.tempCount1 = 0
        self.tempCount2 = 0
        for allocation in self.memoryResult_time[1]:
            if allocation[0] == "A":
                self.tempCount1 += 1
                self.fatListbox1.insert( self.tempCount1, allocation )
            else:
                self.tempCount2 += 1
                self.fatListbox2.insert( self.tempCount2, allocation )

        # Buttons
        self.backBTN  =  Button ( root , text = 'Back',command = self.pat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#f3e9dc" )
        self.backBTN.place (x=70, y=650)
        self.basicWidgetList.append( self.backBTN )

        self.nextBTN  =  Button ( root , text = 'Next',command = self.fat_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#f77f00" )
        if self.nextPointer == None:
            self.nextBTN.configure( text = "Try New Input", width = 13 )
        self.nextBTN.place (x=680, y=650)
        self.basicWidgetList.append( self.nextBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = self.homepage, font = ('Poppins', 16, 'bold'), width  =  12, bg = "#eae2b7" )
        self.exitBTN.place (x=250, y=650)
        self.basicWidgetList.append( self.exitBTN )

    def fat_nextBTN_Pressed( self ):
        if self.nextPointer == None:
            frontEnd.input1_window()
        else:
            self.nextPointer.memMap_window()

                    
# The Graphical User Interface's activation.
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x750" )
root.config ( background = "LIGHTBLUE" )

frontEnd = dynamic_firstFit_frontEnd()
frontEnd.input1_window()

root.mainloop()

