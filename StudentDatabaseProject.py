import sqlite3, sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton,QMessageBox, QGridLayout, QMainWindow, QVBoxLayout, QComboBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtGui import QIcon
class Login(QDialog):
    def __init__(self, parent = None):
        super().__init__() #''' Here Parent Class in QDialog initializing it with Super Method passing parent = None'''
        self.usernameLabel = QLabel("Username")
        self.passwordLabel = QLabel("Password")
        self.textUsername  = QLineEdit(self)
        self.textPassword  = QLineEdit(self)
        self.loginButton   =  QPushButton("Login",self)
        self.loginButton.setToolTip("Login to Continue")
        self.loginButton.clicked.connect(self.performLogin)
        self.displayImage = QLabel(self)
        self.displayImage.resize(70, 70)
        self.displayImage.move(115,10)
        self.displayImage.setScaledContents(True)
        self.displayImage.setPixmap(QPixmap("AUTH.png"))
        '''imageLabel = QLabel(self)
        pix = QPixmap('AUTH.png')
        imageLabel.setPixmap(pix)
        imageLabel.setScaledContents(True)
        imageLabel.setFixedWidth(80)
        imageLabel.setFixedHeight(80)
        '''
        layout = QGridLayout(self)                          #Self Not Used Here Because they are Define Inside Function.
        '''layout.addWidget(self.imageLabel)'''
        layout.addWidget(self.usernameLabel, 2, 1, 2, 3)
        layout.addWidget(self.passwordLabel, 3, 1, 2, 3)
        layout.addWidget(self.textUsername,  2, 2, 2, 2)
        layout.addWidget(self.textPassword,  3, 2, 2, 2)
        layout.addWidget(self.loginButton,   4, 2)
        #image = QPixMap('AUTH.png')
        self.setWindowTitle("Login")
        self.setGeometry(10, 10, 300, 300)
        '''self.setWindowTitle("LOGIN AUTHENTICATION")
        self.setGeometry(10, 10, 640, 480)
        self.show()
        self.show()'''
    def performLogin(self):
        if(self.textUsername.text() == 'admin' and self.textPassword.text() == 'password'):
            self.accept() #here self.accept() is a QDialog Method to close the dialog
        else:
            QMessageBox.warning(self, "Authentication Failed", "Username or Password Incorrect")

class DatabaseAP():
    def __init__(self):
        self.conn = sqlite3.connect('JoJo.db')
        self.c = self.conn.cursor()
        #WHY GENDER INT
        self.c.execute("CREATE TABLE IF NOT EXISTS StudentRecord(Name TEXT, Address TEXT, Year INTEGER, Branch INTEGER, Roll INTEGER, Gender INTEGER, Phone INTEGER, AcademicYear INTEGER")

    def addStudentRecord(self, name, address, year, branch, roll, gender, phone , academicYear):
        self.c.execute("INSERT INTO StudentRecord(Name, Address, Year, Branch, Roll, Gender, Phone, AcademicYear) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                       (name, address, year, branch, roll, gender, phone, academicYear))
        self.conn.commit()
        self.c.close()
        self.conn.close()
        QMessageBox.information(QMessageBox, "Successfull","Record Entered Successfully")

    def searchRecord(self, roll):
        self.c.execute("SELECT * from StudentRecord where Roll ="+str(roll))
        self.data = self.c.fetchone()
        if not self.data:
            QMessageBox.warning(QMessageBox(), 'Error', "Record Not Found")
            return None
        self.list = []
        for i in range(0, 8):
            self.list.append(self.data[i])
        self.c.close()
        self.conn.close()
        showStudent(self.list)

        ## ADD SHOW FUNCTION HERE - ADDED
    def updateRecord(self, name, address, year, branch, roll, gender, phone , academicYear):
        self.c.execute("SELECT * FROM StudentRecord WHERE Roll=")    # ADD HERE
        self.data = self.c.fetchone()
        if not self.data:
            QMessageBox.warning(QMessageBox(), 'Error', "Record Not Found")
            return None
        self.c.execute("UPDATE StudentRecord SET Name = %s, Address = %s, Year = %s , Branch =%s, Roll =%s, Gender =%s, Phone = %s, AcademicYear = %s WHERE Roll = ?" % (name, address, year, branch, roll, gender, phone , academicYear), roll)
        self.c.close()
        self.conn.close()
        QMessageBox(QMessageBox, 'Error',"Updated Successfully !")

def showStudent(newList):
    name = ""
    address = ""
    year = ""
    branch = ""
    roll = 0
    gender = ""
    phone = -1
    academicyear = -1

    name = newList[0]
    address = newList[1]

    #YEAR
    if newList[2] == 0:
        year = "1st Year"
    elif newList[2] == 1:
        year = "2nd Year"
    elif newList[2] == 2:
        year = "3rd Year"
    elif newList[2] == 3:
        year = "3rd Year"
    elif newList[2] == 4:
        year = "4rd Year"

   #BRANCH
    if newList[3] == 0:
        branch = "Civil"
    elif newList[3] == 1:
        branch = "Mechanical"
    elif newList[3] == 2:
        branch = "Computer Science"
    elif newList[3] == 3:
        branch = "Electrical"
    elif newList[3] == 4:
        branch = "Electronics And Telecommunication"
    elif newList[3] == 5:
        branch = "IT"

    roll = newList[4]

    #GENDER
    if newList[5] == 0:
        gender = "Male"
    elif newList == 1:
        gender = "Female"

    phone = newList[6]

    academicyear = newList[7]

    #DISPLAY TABLE

class AddPayment(QDialog):
    def __init__(self):
        super().__init__()
        self.rollNumber = -1
        self.fee = -1

        #BUTTONS
        self.cancelButton = QPushButton("Cancel", self)
        self.addButton = QPushButton("Push", self)
        self.resetButton  = QPushButton("Reset", self)

        self.cancelButton.setFixedHeight(30)
        self.addButoon.setFixedHeight(30)
        self.resetButton.setFixedHeight(30)

        #Labels
        self.rollNumberLabel = QLabel("Roll Number")
        self.feeLabel = QLabel("Fee Amount")

        #TextEdits
        self.rollNumberEdit = QLineEdit(self)
        self.feeEdit = QLineEdit(self)

        self.grid = QGridLayout(self)

        #SETIING LABELS IN THE GRID
        self.grid.addWidget(self.rollNumberLabel, 1, 1)
        self.grid.addWidget(self.feeLabel, 2, 1)

        #SETTING LINEDITS IN THE GRID
        self.grid.addWidget(self.rollNumberEdit, 1, 2)
        self.grid.addWidget(self.feeEdit, 2, 2)

        #SETIING BUTTONS IN THE GRID
        self.grid.addWidget(self.resetButton, 3, 1)
        self.grid.addWidget(self.addButton, 3, 2)
        self.grid.addWidget(self.cancelButton, 3, 3)

        #CONNECTING BUTTONS
        self.resetButton.clicked.connect(self.performReset)
        self.cancelButton.clicked.connect(self.done(0))
        self.addButton.clicked.connect(self.performAdd)

        #Setting Dialog Parameters;
        self.setLayout(self.grid)
        self.resize(400, 300)
        self.setWindowTitle("Add Payment Record")
        self.show()
        sys.exit(self.exec())

    #Methods
    def performReset(self):
            self.rollNumberEdit.setText("")
            self.feeEdit.setText("")

    def performAdd(self):
            self.rollNumber = int(self.rollNumberEdit.text())
            self.fee = int(self.feeLabel.text())
class AddStudent(QDialog):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.address = ""
        self.year = -1
        self.branch = -1
        self.phoneNumber = -1
        self.rollNo = -1
        self.gender = -1
        self.academicYear = -1

        self.resetButton  = QPushButton("Reset", self)
        self.addButton    = QPushButton("Add", self)
        self.cancelButton = QPushButton("Cancel", self)

        self.resetButton.setFixedHeight(30)
        self.addButton.setFixedHeight(30)
        self.cancelButton.setFixedHeight(30)

        self.nameLabel    = QLabel("Name")
        self.addressLabel = QLabel("Address")
        self.genderLabel  = QLabel("Gender")
        self.yearLabel    = QLabel("Current Year")
        self.branchLabel  = QLabel("Branch")
        self.phoneNumberLabel = QLabel("Phone Number")
        self.rollNoLabel = QLabel("Roll No.")
        self.academicYearLabel = QLabel("Academic Year")

        self.yearCombo = QComboBox(self)
        self.yearCombo.addItem("1st Year")
        self.yearCombo.addItem("2nd Year")
        self.yearCombo.addItem("3rd Year")
        self.yearCombo.addItem("4th Year")

        self.genderCombo = QComboBox(self)
        self.genderCombo.addItem("Male")
        self.genderCombo.addItem("Female")

        self.branchCombo = QComboBox(self)
        self.branchCombo.addItem("Civil")
        self.branchCombo.addItem("Mechanical")
        self.branchCombo.addItem("Computer Science")
        self.branchCombo.addItem("Electrical")
        self.branchCombo.addItem("Electronics And Telecommunication")
        self.branchCombo.addItem("IT")


        self.nameEdit = QLineEdit(self)
        self.addressEdit = QLineEdit(self)
        self.academicYearEdit = QLineEdit(self)
        self.phoneNumberEdit = QLineEdit(self)
        self.rollNumberEdit = QLineEdit(self)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.nameLabel, 1, 1)
        self.gridLayout.addWidget(self.addressLabel, 2, 1)
        self.gridLayout.addWidget(self.genderLabel, 3, 1)
        self.gridLayout.addWidget(self.yearLabel, 4, 1)
        self.gridLayout.addWidget(self.branchLabel, 5, 1)
        self.gridLayout.addWidget(self.phoneNumberLabel, 6, 1)
        self.gridLayout.addWidget(self.rollNoLabel, 7, 1)
        self.gridLayout.addWidget(self.academicYearLabel, 8, 1)

        self.gridLayout.addWidget(self.nameEdit, 1, 2)
        self.gridLayout.addWidget(self.addressEdit, 2, 2)
        self.gridLayout.addWidget(self.genderCombo, 3, 2)
        self.gridLayout.addWidget(self.yearCombo, 4, 2)
        self.gridLayout.addWidget(self.branchCombo, 5, 2)
        self.gridLayout.addWidget(self.phoneNumberEdit, 6, 2)
        self.gridLayout.addWidget(self.rollNumberEdit, 7, 2)
        self.gridLayout.addWidget(self.academicYearEdit, 8, 2)

        ##ADDING BUTTONS
        self.gridLayout.addWidget(self.resetButton, 9, 1)
        self.gridLayout.addWidget(self.addButton, 9, 2)
        self.gridLayout.addWidget(self.cancelButton,9, 3)

        #CONNECTING BUTTONS TO METHODS
        self.resetButton.clicked.connect(self.performResetOperation)            #FUNCTION DEFINATION LEFT
        self.addButton.clicked.connect(self.performAddOperation)                #FUNCTION DEFINATION LEFt
        self.cancelButton.clicked.connect(self.done(0)) ## NEED TO ADD DIALOG QUIT


        self.setLayout(self.gridLayout)
        self.setWindowTitle("Add Student Details")
        self.resize(500, 300)
        self.show()
        sys.exit(self.exec())

    def performAddOperation(self):
            self.name = self.nameEdit.text()
            self.address = self.addressEdit.text()
            self.year = self.yearCombo.currentIndex()
            self.branch = self.branchCombo.currentIndex()
            self.phoneNumber = int(self.phoneNumberEdit.text())
            self.rollNo = int(self.rollNumberEdit)
            self.gender = self.genderCombo.currentIndex()
            self.academicYear = int(self.academicYearEdit.text())

    def performResetOperation(self):
            self.nameEdit.setText("")
            self.addressEdit.setText("")
            self.yearEdit.setText("")
            self.phoneNumberEdit.setText("")
            self.rollNumberEdit.setText("")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #DIALOG FOR SEARCHING STUDENT RECORD
        self.searchDialogName = QLabel("Enter Student's Roll No")
        self.rollNoToken     = QLineEdit(self)
        self.searchButton    = QPushButton("Search", self)
        self.searchButton.clicked.connect(self.showStudentDetails)
        self.vBox            = QVBoxLayout()
        self.vBox.addWidget(self.searchDialogName)
        self.vBox.addWidget(self.rollNoToken)
        self.vBox.addWidget(self.searchButton)
        self.dialog = QDialog()
        self.setWindowTitle("Search Details")
        self.dialog.setLayout(self.dialog)

        #DIALOG FOR SEARHING STUDENT's PAYMENT RECORD
        self.paymentDialogName   = QLabel("Enter Student's Roll No")
        self.paymentRollNoToken  = QLineEdit(self)
        self.paymentSearchButton = QPushButton("Search", self)
        self.paymentSearchButton.clicked.connect(self.showPaymentDetails)
        self.paymentBoxLayout    = QVBoxLayout()
        self.paymentBoxLayout.addWidget(self.paymentDialogName)
        self.paymentBoxLayout.addWidget(self.paymentRollNoToken)
        self.paymentBoxLayout.addWidget(self.paymentSearchButton)
        self.paymentDialog = QDialog()
        self.paymentDialog.setLayout(self.paymentBoxLayout)
        self.setWindowTitle("Search Payment Details")



        #Four Search Buttons
        self.enterStudentRecord        = QPushButton("Enter Student Details", self)
        self.showStudentRecord         = QPushButton("Show Student Details", self)
        self.enterStudentPaymentRecord = QPushButton("Enter Payment Details", self)
        self.showStudentPaymentRecord  = QPushButton("Show Payment Details", self)

        #Picture
        self.imageLabel = QLabel(self)
        self.imageLabel.resize(150, 150)
        self.imageLabel.move(120, 20)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setPixmap(QPixmap('xyz.jpg'))

        #BUTTON 1
        self.enterStudentRecord.move(15, 170)
        self.enterStudentRecord.resize(180,40)
        self.enterStudentRecordFont = self.enterStudentRecord.font()
        self.enterStudentRecordFont.setFontSize(16)
        self.enterStudentRecord.setFont(self.enterStundentRecord)
        self.enterStudentRecord.clicked.connect(self.enterStudentRecordDialog)  #First Function

        #Button 2
        self.enterStudentPaymentRecord.move(15, 170)
        self.enterStudentPaymentRecord.resize(180, 40)
        self.enterStudentPaymentRecordFont = self.enterStudentPaymentRecord.font()
        self.enterStudentPaymentRecordFont.setFontSize(16)
        self.enterStudentPaymentRecord.setFont(self.enterStudentPaymentRecordFont)
        self.enterStudentPaymentRecord.clicked.connect(self.enterStudentPaymentRecordDialog)  # Second Funtion

        # BUTTON 3
        self.showStudentRecord.move(15, 170)
        self.showStudentRecord.resize(180, 40)
        self.showStudentRecordFont = self.showStudentRecord.font()
        self.showStudentRecordFont.setFontSize(16)
        self.showStudentRecord.setFont(self.showStudentRecordFont)
        self.showStudentRecord.clicked.connect(self.StudentRecordSearchDialog)  # Third Function

        #Button 4
        self.showStudentPaymentRecord.move(15, 170)
        self.showStudentPaymentRecord.resize(180, 40)
        self.showStudentPaymentRecordFont = self.showStudentPaymentRecord.font()
        self.showStudentPaymentRecordFont.setFontSize(16)
        self.showStudentPaymentRecord.setFont(self.showStudentPaymentRecordFont)
        self.showStudentPaymentRecord.clicked.connect(self.StudentPaymentRecordSearchDialog)  # Third Function


        self.resize(400, 280)
        self.setWindowTitle("Student Database Management System")

    def enterStudentRecordDialog(self):
        enterStudent = AddStudent()
    def enterStudentPaymentRecordDialog(self):
        enterPayment = AddPayment()
    def StudentRecordSearchDialog(self):
        self.dialog.exec();
    def StudentPaymentRecordSearchDialog(self):
        self.paymentDialog.exec()
    def showStudentDetails(self):
        if self.rollNoToken.text() is "":
            QMessageBox.warning(QMessageBox(), "Errro", "You Must Provide a Roll Number to search record")
            return None
    def showPaymentDetails(self):
        if self.paymentRollNoToken.text() is "":
            QMessageBox.warning(QMessageBox(), "Error", "You Must Provide a Roll Number to Search Record")
            return None


if __name__ == '__main__':
    app = QApplication([])  #No Runtime Parameters Being passed Here.
    LoginForm = Login()
    if LoginForm.exec_() == QDialog.accepted:
        window = Window()
        window.show()
    sys.exit(app.exec_())





















