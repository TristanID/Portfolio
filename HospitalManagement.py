class Doctor:

    def __init__(self):
        self.id = "None"
        self.name = "None"
        self.spec = "None"
        self.hours = "None"
        self.qual = "None"
        self.room = "None"

    def formatDrInfo(self, list_to_convert):
        self.converted_string = '_'.join(list_to_convert)
        return self.converted_string + '\n'

    def enterDrInfo(self):
        self.id = input("Enter the doctor's ID:\n\n")
        self.name = input("Enter the doctor's name:\n\n")
        self.spec = input("Enter the doctor's specility:\n\n")
        self.hours = input("Enter the doctor's timing (e.g., 7am-10pm):\n\n")
        self.qual = input("Enter the doctor's qualification:\n\n")
        self.room = input("Enter the doctor's room number:\n\n")
        return [self.id, self.name, self.spec, self.hours, self.qual, self.room]

    def readDoctorsFile(self):
        self.open_file = open("doctors.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list

    def searchDoctorById(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []

        for i in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[i] = self.doctor_list[i].split("_")

        self.query = input("\n Enter the doctor ID:\n\n")

        self.flag = False
        for i in range(len(self.new_list)):
            if self.new_list[i][0] == self.query:
                self.displayDoctorInfo(self.new_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system")

    def searchDoctorByName(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []
        for i in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[i] = self.doctor_list[i].split("_")

        self.query = input("\n Enter the doctor name:\n\n")

        self.flag = False
        for i in range(len(self.new_list)):
            if self.new_list[i][1] == self.query:
                self.displayDoctorInfo(self.new_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same name on the system")

    def displayDoctorInfo(self, doctor_list):
        self.doctor_list = doctor_list
        self.doctor_list[4] = self.doctor_list[4].upper()  # capitalizes qualifications due to file inconsistancy
        print(
            f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}" + '\n')
        print(
            f"{self.doctor_list[0]: <5}{self.doctor_list[1]: <20}{self.doctor_list[2]: <15}{self.doctor_list[3]: <15}{self.doctor_list[4]: <15}{self.doctor_list[5]: <0}")

    def editDoctorInfo(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []
        for i in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[i] = self.doctor_list[i].split("_")

        self.query = input("Please enter the id of the doctor that you want to edit their information:\n\n")

        self.flag = False
        for i in range(len(self.new_list)):
            if self.new_list[i][0] == self.query:
                self.new_list[i][1] = input("\nEnter new Name:\n\n")
                self.new_list[i][2] = input("\nEnter new Specilist in:\n\n")
                self.new_list[i][3] = input("\nEnter new Timing: \n\n")
                self.new_list[i][4] = input("\nEnter new Qualification: \n\n")
                self.new_list[i][5] = input("\nEnter new Room number:\n\n")
                self.doctor_list[i] = self.formatDrInfo(self.new_list[i])
                self.writeListOfDoctorsToFile(self.doctor_list)
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system\n")

    def displayDoctorsList(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []

        for i in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[i] = self.doctor_list[i].split("_")

        del self.new_list[0]  # removes file header

        print(
            f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}" + '\n')
        for i in range(len(self.new_list)):
            print(
                f"{self.new_list[i][0]: <5}{self.new_list[i][1]: <20}{self.new_list[i][2]: <15}{(self.new_list[i][3].lower()): <15}{(self.new_list[i][4].upper()): <15}{self.new_list[i][5]: <0}")

    def writeListOfDoctorsToFile(self, doctor_list):
        self.open_file = open("doctors.txt", "w")
        self.index = 0
        for entries in doctor_list:
            self.open_file.write(doctor_list[self.index])
            self.index += 1
        self.open_file.close()

    def addDrToFile(self):
        self.doctor_to_add = self.enterDrInfo()
        self.doctor_to_add = self.formatDrInfo(self.doctor_to_add)
        self.doctor_list = self.readDoctorsFile()

        self.index = 0
        for entries in self.doctor_list:
            if self.doctor_list[self.index].endswith('\n') == False:
                self.doctor_list[self.index] = self.doctor_list[self.index] + '\n'
            self.index += 1

        self.doctor_list.append(self.doctor_to_add)
        self.writeListOfDoctorsToFile(self.doctor_list)


class Facility:

    def __init__(self):
        self.facility_name = "None"

    def addFacility(self):
        '''Adds and writes the facility name to the file'''
        self.open_file = open("facilities.txt", "r")
        self.facility_list = self.open_file.readlines()
        self.open_file.close()

        self.facility_name = input("Enter Facility name: \n\n")

        self.facility_list.append(self.facility_name)

        self.writeListOffacilitiesToFile(self.facility_list)

    def displayFacilities(self):
        '''Displays the list of facilities'''
        self.open_file = open("facilities.txt", "r")
        self.facility_list = self.open_file.readlines()
        self.open_file.close()

        self.facility_list[0] = "The " + self.facility_list[0]

        for i in range(len(self.facility_list)):
            if self.facility_list[i].endswith('\n') == False:
                print(self.facility_list[i] + '\n')
            else:
                print(self.facility_list[i])

    def writeListOffacilitiesToFile(self, new_entry):
        '''Writes the facilities list to facilities.txt'''
        self.open_file = open("facilities.txt", "w")

        self.index = 0
        for entries in new_entry:
            if new_entry[self.index].endswith('\n') == False:
                new_entry[self.index] = new_entry[self.index] + '\n'
            self.open_file.write(new_entry[self.index])
            self.index += 1

        self.open_file.close()


class Laboratory:
    def __init__(self):
        self.laboratory_name = "None"
        self.Cost = "None"

    def formatLaboratoryInfo(self, list_to_convert):
        # Formats the Laboratory object similar to the laboratories.txt file
        self.converted_string = '_'.join(list_to_convert)
        return self.converted_string + '\n'

    def enterLaboratoryInfo(self):
        self.Facility = input("Enter Laboratory facility: \n\n")
        self.Cost = input("Enter Laboratory cost: \n\n")
        return [self.Facility, self.Cost]

    def readLaboratoriesFile(self):
        self.open_file = open("laboratories.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list

    def displayLaboratoryInfo(self, laboratory_list):
        self.laboratory_list = laboratory_list
        self.laboratory_list[4] = self.laboratory_list[4].upper()  # capitalizes qualifications due to file inconsistancy
        print(
            f"{'Facility': <20}{'Cost': <15}" + '\n')
        print(
            f"{self.laboratory_list[0]: <20}{self.laboratory_list[1]: <15}")

    def displayLabsList(self):
        # Display the list of laboratories
        self.laboratory_list = self.readLaboratoriesFile()
        self.new_list = []

        for i in range(len(self.laboratory_list)):
            self.new_list.append([])
            self.new_list[i] = self.laboratory_list[i].split("_")

        del self.new_list[0]  # removes file header

        print(
               f"{'Facility': <20}{'Cost': <15}" + '\n')
        for i in range(len(self.new_list)):
            print(
                f"{self.new_list[i][0]: <20}{self.new_list[i][1]: <15}")

    def writeListOfLabsToFile(self, test_list):
        # Write the list of labs into the file laboratories.txt
        self.open_file = open("laboratories.txt", "w")
        self.index = 0
        for entries in test_list:
            self.open_file.write(test_list[self.index])
            self.index += 1
        self.open_file.close()

    def addLabToFile(self):
        # Adds and writes the lab name to the file format of the data that is in the file
        self.laboratory_to_add = self.enterLaboratoryInfo()
        self.laboratory_to_add = self.formatLaboratoryInfo(self.laboratory_to_add)
        self.laboratory_list = self.readLaboratoriesFile()

        self.index = 0
        for entries in self.laboratory_list:
            if self.laboratory_list[self.index].endswith('\n') == False:
                self.laboratory_list[self.index] = self.laboratory_list[self.index] + '\n'
            self.index += 1
        self.laboratory_list.append(self.laboratory_to_add)
        self.writeListOfLabsToFile(self.laboratory_list)

class Patient:

    def __init__(self):
        self.id = "None"
        self.Name = "None"
        self.Disease = "None"
        self.Gender = "None"
        self.Age = "None"

    def formatPatientInfo(self, list_to_convert):
        self.converted_string = '_'.join(list_to_convert)
        return self.converted_string + '\n'

    def enterPatientInfo(self):
        self.id = input("Enter the Patient ID:\n\n")
        self.Name = input("Enter the Patient name:\n\n")
        self.Disease = input("Enter the Patient disease:\n\n")
        self.Gender = input("Enter the Patient gender:\n\n")
        self.Age = input("Enter the Patient age :\n\n")
        return [self.id, self.Name, self.Disease, self.Gender, self.Age]

    def readPatientsFile(self):
        self.open_file = open("patients.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list

    def searchPatientById(self):
        self.patients_list = self.readPatientsFile()
        self.new_list = []

        for i in range(len(self.patients_list)):
            self.new_list.append([])
            self.new_list[i] = self.patients_list[i].split("_")

        self.query = input("\n Enter the doctor ID:\n\n")

        self.flag = False
        for i in range(len(self.new_list)):
            if self.new_list[i][0] == self.query:
                self.displayPatientInfo(self.new_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the patient with the same ID on the system")

    def displayPatientInfo(self, patients_list):
        self.patients_list = patients_list
        self.patients_list[4] = self.patients_list[4].upper()  # capitalizes qualifications due to file inconsistancy
        print(
            f"{'Id': <5}{'Name': <20}{'Disease': <15}{'Gender': <15}{'Age': <15}" + '\n')
        print(
            f"{self.patients_list[0]: <5}{self.patients_list[1]: <20}{self.patients_list[2]: <15}{self.patients_list[3]: <15}{self.patients_list[4]: <15}")

    def editPatientInfo(self):
        self.patients_list = self.readPatientsFile()
        self.new_list = []
        for i in range(len(self.patients_list)):
            self.new_list.append([])
            self.new_list[i] = self.patients_list[i].split("_")

        self.query = input("Please enter the id of the Patient that you want to edit their information:\n\n")

        self.flag = False
        for i in range(len(self.new_list)):
            if self.new_list[i][0] == self.query:
                self.new_list[i][1] = input("\nEnter new Name:\n\n")
                self.new_list[i][2] = input("\nEnter new disease in:\n\n")
                self.new_list[i][3] = input("\nEnter new gender: \n\n")
                self.new_list[i][4] = input("\nEnter new age: \n\n")
                self.patients_list[i] = self.formatPatientInfo(self.new_list[i])
                self.writeListOfPatientsToFile(self.patients_list)
                self.flag = True
        if self.flag == False:
            print("Can't find the Patient with the same ID on the system\n")

    def displayPatientsList(self):
        self.patients_list = self.readPatientsFile()
        self.new_list = []

        for i in range(len(self.patients_list)):
            self.new_list.append([])
            self.new_list[i] = self.patients_list[i].split("_")

        del self.new_list[0]  # removes file header

        print(
            f"{'Id': <5}{'Name': <20}{'Disease': <15}{'Gender': <15}{'Gender': <15}" + '\n')
        for i in range(len(self.new_list)):
            print(
                f"{self.new_list[i][0]: <5}{self.new_list[i][1]: <20}{self.new_list[i][2]: <15}{self.new_list[i][3]: <15}{self.new_list[i][4]: <15}")

    def writeListOfPatientsToFile(self, patients_list):
        self.open_file = open("patients.txt", "w")
        self.index = 0
        for entries in patients_list:
            self.open_file.write(patients_list[self.index])
            self.index += 1
        self.open_file.close()

    def addPatientToFile(self):
        self.patient_to_add = self.enterPatientInfo()
        self.patient_to_add = self.formatPatientInfo(self.patient_to_add)
        self.patients_list = self.readPatientsFile()

        self.index = 0
        for entries in self.patients_list:
            if self.patients_list[self.index].endswith('\n') == False:
                self.patients_list[self.index] = self.patients_list[self.index] + '\n'
            self.index += 1

        self.patients_list.append(self.patient_to_add)
        self.writeListOfPatientsToFile(self.patients_list)



class Management:

    def DisplayMenu(self):
        self.repeat = True
        while self.repeat:
            self.option = input(
                'Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n\n')

            if int(self.option) == 1:
                self.cycle = True
                self.obj_handle = Doctor()
                while self.cycle:
                    self.option = input(
                        '\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayDoctorsList()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 2:
                        self.obj_handle.searchDoctorById()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 3:
                        self.obj_handle.searchDoctorByName()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 4:
                        self.obj_handle.addDrToFile()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 5:
                        self.obj_handle.editDoctorInfo()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 6:
                        self.cycle = False
                        print("")

            elif int(self.option) == 2:
                self.cycle = True
                self.obj_handle = Facility()
                while self.cycle:
                    self.option = input(
                        'Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayFacilities()
                        print("Back to the previous Menu")
                    elif int(self.option) == 2:
                        self.obj_handle.addFacility()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 3:
                        self.cycle = False
                        print("")


            elif int(self.option) == 3:
                self.cycle = True
                self.obj_handle = Laboratory()
                while self.cycle:
                    self.option = input('Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayLabsList()
                    elif int(self.option) == 2:
                        self.obj_handle. addLabToFile()
                    elif int(self.option) == 3:
                        self.cycle = False
                    print("Back to the previous Menu\n")

            elif int(self.option) == 4:
                self.cycle = True
                self.obj_handle = Patient()
                while self.cycle:
                    self.option = input('Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayPatientsList()
                    elif int(self.option) == 2:
                        self.obj_handle.searchPatientById()
                    elif int(self.option) == 3:
                        self.obj_handle.addPatientToFile()
                    elif int(self.option) == 4:
                        self.obj_handle.editPatientInfo()
                    elif int(self.option) == 5:
                        self.cycle = False
                    print("Back to the previous Menu\n")

            else:
                self.repeat = False

run_obj = Management()
run_obj.DisplayMenu()