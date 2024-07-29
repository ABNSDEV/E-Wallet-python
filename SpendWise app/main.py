#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs

import sys
import time
from threading import * 
from PyQt6.QtCore import *
from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import *
from PyQt6 import * 
from win32api import GetSystemMetrics
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QIcon
import sqlite3
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg 
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('assets/logo.png'))
        self.width = 1200
        self.height = 700
        self.x = GetSystemMetrics(0)# get width res
        self.y = GetSystemMetrics(1)# get height res

        self.wall = QPixmap('assets/bg-2.JPG').scaled(self.width,self.height)
        self.pix = QLabel(self)
        self.pix.setGeometry(0,0,self.width,self.height)
        self.pix.setPixmap(self.wall)
      
        
        # Create a label widget and set its pixmap
        

        self.App_name = "SpendWise v1.0.1"
        self.copyrights = QLabel(f"© ABNS•DEVS SPENDWISE APP 2024 ",self)
        self.copyrights.setStyleSheet('color:silver;font-weight:bold;font-size:10px;background:transparent')
        self.copyrights.setGeometry(0,int(self.height-20),self.width,20)
        self.copyrights.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        self.w_center = (self.x - self.width)/2 # get width center point
        self.h_center = (self.y - self.height)/2# get height center point

        self.bg_titlebar = "transparent"
        self.frames_bg = "transparent"
        self.frames_bg2 = "transparent"
        self.bg = "#192a56"
        self.sec_bg = "#273c75"
        self.TitleWidth = self.width
        self.TitleHeight = 40
        self.TitleBtns = self.TitleHeight
        
        self.setGeometry(int(self.w_center),int(self.h_center),self.width,self.height)
        self.setWindowTitle(f"{self.App_name}")
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(f'background:{self.bg};color:white')
        self.titlebar = QFrame(self)
        self.titlebar.setGeometry(0,0,self.TitleWidth,self.TitleHeight)
        self.titlebar.setStyleSheet(f'background:{self.bg_titlebar};border:none')

        self.titlelog = QLabel(f"{self.App_name}",self.titlebar)
        self.titlelog.setStyleSheet('color:#3694c8;font-weight:bold;font-size:14px')
        self.titlelog.setGeometry(0,0,self.width,self.TitleHeight)
        self.titlelog.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        self.closeBtn = QPushButton("•",self.titlebar)
        self.closeBtn.setGeometry(self.width-self.TitleBtns,0,self.TitleBtns,self.TitleBtns)
        self.closeBtn.clicked.connect(self.closeFUNC)
        self.closeBtn.setStyleSheet("QPushButton""{"
            "border:none;"
            "background:transparent;"
            "color:red;"
            "font-weight: bold;"
            "padding-top:-5px;"
            "font-size:35px;"
            "}"

            "QPushButton::hover" "{" 
            "background:rgba(0,0,0,.3);" 
            
            "}"
            )

        self.MinBtn = QPushButton("•",self.titlebar)
        self.MinBtn.setGeometry(self.width-self.TitleBtns*2,0,self.TitleBtns,self.TitleBtns)
        self.MinBtn.clicked.connect(self.minuFUNC)
        self.MinBtn.setStyleSheet("QPushButton""{"
            "border:none;"
            "color:orange;"
            "background:transparent;"
            "padding-top:-5px;"
            "font-weight: bold;"
            "font-size:35px;"
   
            "}"

            "QPushButton::hover" "{" 
            "background:rgba(0,0,0,.3);" 
            "}"
            )
        


        #--------------------------------------------------------------------
       
        # -----------------------------

        #-------------------------------



        self.bdgt_lab = QLabel("Total Budget",self)
        self.bdgt_lab.setGeometry(50,55,250,30)
        self.bdgt_lab.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.bdgt_lab.setStyleSheet('background:rgba(52, 152, 219,.8);border-radius:10px;color:white;font-weight:bold;font-size:20px')
        self.Total_budget = QLabel(f"-- DA",self)
        self.Total_budget.setGeometry(50,90,250,150)
        self.Total_budget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Total_budget.setStyleSheet('background:rgba(52, 152, 219,.8);border-radius:10px;color:white;font-weight:bold;font-size:40px')

        self.Exp_lab = QLabel("Expenses",self)
        self.Exp_lab.setGeometry(475,55,250,30)
        self.Exp_lab.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Exp_lab.setStyleSheet('background:rgba(192, 57, 43,.8);border-radius:10px;color:white;font-weight:bold;font-size:20px')
        self.Expenses = QLabel(f"-- DA",self)
        self.Expenses.setGeometry(475,90,250,150)
        self.Expenses.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Expenses.setStyleSheet('background:rgba(192, 57, 43,.8);border-radius:10px;color:white;font-weight:bold;font-size:40px')
 
        self.balance_lab = QLabel("balance",self)
        self.balance_lab.setGeometry(900,55,250,30)
        self.balance_lab.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.balance_lab.setStyleSheet('background:rgba(22, 160, 133,.8);border-radius:10px;color:white;font-weight:bold;font-size:20px')
        self.Balance = QLabel(f"-- DA",self)
        self.Balance.setGeometry(900,90,250,150)
        self.Balance.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Balance.setStyleSheet('background:rgba(22, 160, 133,.8);border-radius:10px;color:white;font-weight:bold;font-size:40px')

        
        

        self.leftFrame = QFrame(self)
        self.leftFrame.setGeometry(50,260,545,400)
        self.leftFrame.setStyleSheet(f'background:rgba(150,150,170,.1);border-radius:10px')

        self.RightFrame = QFrame(self)
        self.RightFrame.setGeometry(605,260,545,400)
        self.RightFrame.setStyleSheet(f'background:rgba(250,250,250,.1);border-radius:10px')

        
        
        self.conn = sqlite3.connect('dbs/expenses.db')
        self.c = self.conn.cursor()

        self.c.execute("""
                select category , SUM(cost)
                from exps
                GROUP BY category
                """)
            
        self.data = self.c.fetchall()
        self.close()
        self.conn.close()


        layout = QVBoxLayout(self.RightFrame)
        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig) 
        layout.addWidget(self.canvas)
            
            
        self.ax = self.fig.add_subplot(111)
        if self.data:
            self.categories , self.sums = zip(*self.data)
            self.ax.tick_params(axis='x', rotation=12)
            self.ax.bar(self.categories,self.sums,color=["#78e08f","#e55039","#686de0","#f6b93b","#b71540"])
        else:
            pass
        
      
  



        self.category = QComboBox(self.leftFrame)
        self.category.setGeometry(72,50,400,40)
        self.category.setStyleSheet(f'background:rgba(52, 152, 219,.8);border-radius:10px;color:white;font-weight:bold;font-size:25px;border:none')
        self.category.addItem('         -- Choose Category --')
        self.category.addItems(['Food & Drink', 'Transportation', 'Shopping','Health','Education'])
        self.category.setCurrentIndex(0)
        self.category.model().item(0).setEnabled(False)

        self.Exp_name = QLineEdit(self.leftFrame)
        self.Exp_name.setGeometry(72,100,400,40)
        self.Exp_name.setStyleSheet(f'background:rgba(52, 152, 219,.8);border-radius:10px;color:white;font-weight:bold;font-size:25px;border:none')
        self.Exp_name.setPlaceholderText('Enter Expense Name')
        self.Exp_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Exp_Price = QLineEdit(self.leftFrame)
        self.Exp_Price.setGeometry(72,150,400,40)
        self.Exp_Price.setStyleSheet(f'background:rgba(52, 152, 219,.8);border-radius:10px;color:white;font-weight:bold;font-size:25px;border:none')
        self.Exp_Price.setPlaceholderText('Enter Expense Price')
        self.Exp_Price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Add_record = QPushButton("Add Record",self.leftFrame)
        self.Add_record.setGeometry(72,200,400,60)
        self.Add_record.setStyleSheet(f'background:rgba(26, 188, 156,.8);border-radius:10px;color:white;font-weight:bold;font-size:25px')
        self.Add_record.clicked.connect(self.Add_record_fun)

        self.Add_Income = QLineEdit(self.leftFrame)
        self.Add_Income.setGeometry(72,270,190,40)
        self.Add_Income.setStyleSheet(f'background:rgba(255, 255, 255,.8);border-radius:10px;color:{self.bg};font-weight:bold;font-size:20px')
        self.Add_Income.setPlaceholderText('Your New Income')
        self.Add_Income.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Add_Income_btn = QPushButton("Add Income",self.leftFrame)
        self.Add_Income_btn.setGeometry(280,270,190,40)
        self.Add_Income_btn.setStyleSheet(f'background:rgba(241, 196, 15,.8);border-radius:10px;color:white;font-weight:bold;font-size:20px')
        self.Add_Income_btn.clicked.connect(self.Add_income_fun)

        self.Rest_Budget = QPushButton("REST BUDGET",self.leftFrame)
        self.Rest_Budget.setGeometry(72,320,190,60)
        self.Rest_Budget.setStyleSheet(f'background:rgba(255, 99, 71,.8);border-radius:10px;color:white;font-weight:bold;font-size:25px')
        self.Rest_Budget.clicked.connect(self.Rest_bdgt)

        self.ShowRecords = QPushButton("Show Details",self.leftFrame)
        self.ShowRecords.setGeometry(280,320,190,60)
        self.ShowRecords.setStyleSheet(f'background:#8c7ae6;border-radius:10px;color:white;font-weight:bold;font-size:25px')
        self.ShowRecords.clicked.connect(self.Show_Records)



        # Updating the LAbels when the app start
        self.conn = sqlite3.connect('dbs/expenses.db')
        self.c = self.conn.cursor()
        self.c.execute('select SUM(cost) from exps')
        self.costs_Sum =self.c.fetchone()[0]
        self.c.execute('select budget from balance')
        self.budget = self.c.fetchone()
   
        if self.costs_Sum is None:
            self.costs_Sum = 0
        self.Expenses_value = self.costs_Sum
        self.balance_final = float(self.budget[0] - self.costs_Sum)

        self.Expenses.setText(f"{self.Expenses_value} DA")
        self.Balance.setText(f"{self.balance_final} DA")
        self.Total_budget.setText(f'{self.budget[0]} DA')
        
        self.lang = QPushButton("العربية",self)
        self.lang.setGeometry(10,670,100,25)
        self.lang.setStyleSheet('background:#76b8db;color:white;font-size:16px;border-radius:10px')
        self.lang.clicked.connect(self.lang_switch)

        self.lang_sw = False
    def lang_switch(self):
            
        if self.lang_sw == False:
            self.bdgt_lab.setText('الميزانية الإجمالية')
            self.Exp_lab.setText('النفقات')
            self.balance_lab.setText('الميزانية المتبقية')
            self.Exp_name.setPlaceholderText('أدخل إسم النفقة')
            self.Exp_Price.setPlaceholderText('أدخل سعر النفقة')
            self.Add_record.setText('إضافة النفقة')
            self.Add_Income_btn.setText('إضافة المدخول')
            self.Add_Income.setPlaceholderText('أضف مدخولك الجديد')
            self.Rest_Budget.setText('محو الميزانية')
            self.ShowRecords.setText('عرض التفاصيل')
            self.lang.setText('English')
            self.lang_sw = True
        elif self.lang_sw == True:
            self.bdgt_lab.setText('Total Budget')
            self.Exp_lab.setText('Expenses')
            self.balance_lab.setText('balance')
            self.Exp_name.setPlaceholderText('Enter Expense Name')
            self.Exp_Price.setPlaceholderText('Enter Expense Price')
            self.Add_record.setText('Add Record')
            self.Add_Income_btn.setText('Add Income')
            self.Add_Income.setPlaceholderText('Your New Income')
            self.Rest_Budget.setText('REST BUDGET')
            self.ShowRecords.setText('Show Details')
            self.lang.setText('العربية')
            self.lang_sw = False


    def Show_Records(self):
        self.recs = records_window()
        self.recs.show()
        self.close()

        
    def Add_record_fun(self):
        try:
            self.date = time.strftime('%x')
            self.name = self.Exp_name.text()
            self.Selected_category  = self.category.currentText()
            self.cost = self.Exp_Price.text()
            self.conn = sqlite3.connect('dbs/expenses.db')
            self.c = self.conn.cursor()
            if self.name != "" and self.Selected_category != "" and self.cost != "":
                if self.balance_final <= 100:
                    QMessageBox.warning(self,'Oops','Your Budget is under 100 DA !')

                else:
                    self.c.execute('insert into exps (date,category,name,cost) values(?,?,?,?)',(self.date,self.Selected_category,self.name,self.cost))
                    self.conn.commit()
                    self.conn.close()
                    self.Exp_name.clear()
                    self.Exp_Price.clear()
                
                    self.conn = sqlite3.connect('dbs/expenses.db')
                    self.c = self.conn.cursor()

                    self.c.execute('select SUM(cost) from exps')

                    self.costs_Sum =self.c.fetchone()[0]

                    self.c.execute('select budget from balance')
                        
                    self.budget = self.c.fetchone()
                    if self.costs_Sum is None:
                        self.costs_Sum = 0
                    self.Expenses_value = self.costs_Sum
                    self.balance_final = float(self.budget[0] - self.costs_Sum)
                
                    self.Expenses.setText(f"{self.Expenses_value} DA")
                    self.Balance.setText(f"{self.balance_final} DA")
                    self.Total_budget.setText(f'{self.budget[0]} DA')

            else:
                QMessageBox.warning(self,'Oops','ALL filled are Required! ')

        except Exception as e:
            print(f"{e}")

        

    def Add_income_fun(self):
        try:

            self.Add_income = float(self.Add_Income.text())
            self.Add_Income.clear()
            if str(self.Add_income ) != "":

                self.conn = sqlite3.connect('dbs/expenses.db')
                self.c = self.conn.cursor()

                self.c.execute('select Budget from balance')
                self.new_budget = self.c.fetchone()
                self.bdg = self.new_budget[0]
                self.bdg += self.Add_income 
                self.c.execute('select SUM(cost) from exps')
                self.current_costs = self.c.fetchall()[0][0]
                if self.current_costs is None:
                    self.current_costs = 0
            
                self.balance_final = float(self.bdg - self.current_costs)
                self.c.execute("""update balance set Budget=?""",(float(self.bdg),))
                self.conn.commit()
                self.conn.close()
                self.Balance.setText(f"{self.balance_final} DA")
                self.Total_budget.setText(f'{self.bdg} DA')
            

            else:
                
                pass
        except Exception as e:
            QMessageBox.warning(self,'Oops','ALL filled are Required! ')

    def Rest_bdgt(self):
        self.conf = QMessageBox.question(self,"Confirmation","Are you sure u want to Rest your budget ?")

        try:
            if self.conf == 16384:
                self.conn = sqlite3.connect('dbs/expenses.db')
                self.c = self.conn.cursor()
                self.c.execute('DELETE FROM exps') 

                self.c.execute('update balance set Budget=?',(0,))
                self.c.execute('select Budget from balance')
                self.current_budget = self.c.fetchone()
                
                self.c.execute('select SUM(cost) from exps')
                self.current_costs = self.c.fetchall()
                if self.current_costs is None:
                    self.current_costs = 0
                self.balance_final = 0.0
                self.Expenses.setText(f"{0.0} DA")
                self.Balance.setText(f"{self.balance_final} DA")
                self.Total_budget.setText(f"{self.current_budget[0]} DA")
                
                self.conn.commit()
                self.conn.close()   

            else:
                pass

        except Exception as e:
            print(f'{e}')


        
    def closeFUNC(self):
        self.close()       
        self.click_check = 0
    def minuFUNC(self):
        self.showMinimized()
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except:
            pass






#-------------------------------------------------------------------------------------------------------------------------------------------------------
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
#@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs@abnsdevs
class passrest_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 500
        self.height = 500
        self.x = GetSystemMetrics(0)# get width res
        self.y = GetSystemMetrics(1)# get height res

        self.setWindowIcon(QIcon('assets/logo.png'))

        # Create a label widget and set its pixmap
        self.wall = QPixmap('assets/BG-2.JPG').scaled(self.width,self.height)
        self.pix = QLabel(self)
        self.pix.setGeometry(0,0,self.width,self.height)
        self.pix.setPixmap(self.wall)

        self.App_name = "SpendWise v1.0.1"
        self.copyrights = QLabel(f"© ABNS•DEVS SPENDWISE APP 2024 ",self)
        self.copyrights.setStyleSheet('color:silver;font-weight:bold;font-size:10px;background:transparent')
        self.copyrights.setGeometry(0,int(self.height-20),self.width,20)
        self.copyrights.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        self.w_center = (self.x - self.width)/2 # get width center point
        self.h_center = (self.y - self.height)/2# get height center point

        

        self.bg_titlebar = "transparent"
        self.frames_bg = "transparent"
        self.frames_bg2 = "transparent"
        self.bg = "#192a56"
        self.sec_bg = "#273c75"
        self.TitleWidth = self.width
        self.TitleHeight = 40
        self.TitleBtns = self.TitleHeight
        
        self.setGeometry(int(self.w_center),int(self.h_center),self.width,self.height)
        self.setWindowTitle(f"{self.App_name}")
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(f'background:{self.bg};color:white;')
        self.titlebar = QFrame(self)
        self.titlebar.setGeometry(0,0,self.TitleWidth,self.TitleHeight)
        self.titlebar.setStyleSheet(f'background:{self.bg_titlebar};border:none')

        self.titlelog = QLabel(f"{self.App_name}",self.titlebar)
        self.titlelog.setStyleSheet('color:#3694c8;font-weight:bold;font-size:14px')
        self.titlelog.setGeometry(0,0,self.width,self.TitleHeight)
        self.titlelog.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        self.closeBtn = QPushButton("•",self.titlebar)
        self.closeBtn.setGeometry(self.width-self.TitleBtns,0,self.TitleBtns,self.TitleBtns)
        self.closeBtn.clicked.connect(self.closeFUNC)
        self.closeBtn.setStyleSheet("QPushButton""{"
            "border:none;"
            "background:transparent;"
            "color:red;"
            "font-weight: bold;"
            "padding-top:-5px;"
            "font-size:35px;"
            "}"

            "QPushButton::hover" "{" 
            "background:rgba(0,0,0,.3);" 
            
            "}"
            )

        self.MinBtn = QPushButton("•",self.titlebar)
        self.MinBtn.setGeometry(self.width-self.TitleBtns*2,0,self.TitleBtns,self.TitleBtns)
        self.MinBtn.clicked.connect(self.minuFUNC)
        self.MinBtn.setStyleSheet("QPushButton""{"
            "border:none;"
            "color:orange;"
            "background:transparent;"
            "padding-top:-5px;"
            "font-weight: bold;"
            "font-size:35px;"
   
            "}"

            "QPushButton::hover" "{" 
            "background:rgba(0,0,0,.3);" 
            "}"
            )
        


        #--------------------------------------------------------------------
        self.log_lab = QLabel("password Reset",self)
        self.log_lab.setStyleSheet(f'color:#4a69bd;font-weight:bold;font-size:50px;background:transparent') 
        self.log_lab.setGeometry(0,100,self.width,100)
        self.log_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)



        self.currentpassword_ed = QLineEdit(self)
        self.currentpassword_ed.setStyleSheet(f'background:#4a69bd;border-radius:10px;color:white;font-weight:bold;font-size:18px;border:none') 
        self.currentpassword_ed.setGeometry(100,245,300,50)
        self.currentpassword_ed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currentpassword_ed.setPlaceholderText('Current password')
        self.currentpassword_ed.setEchoMode(QLineEdit.EchoMode.Password)

        self.new_password_ed = QLineEdit(self)
        self.new_password_ed.setStyleSheet(f'background:#4a69bd;border-radius:10px;color:white;font-weight:bold;font-size:18px;border:none') 
        self.new_password_ed.setGeometry(100,300,300,50)
        self.new_password_ed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.new_password_ed.setPlaceholderText('New Password')
        self.new_password_ed.setEchoMode(QLineEdit.EchoMode.Password)

        self.save_btn = QPushButton("SAVE",self)
        self.save_btn.setGeometry(100,360,300,50)
        self.save_btn.setStyleSheet(f'background:#10ac84;border-radius:10px;color:white;font-weight:bold;font-size:18px;border:none') 
        self.save_btn.clicked.connect(self.password_rest)

    def password_rest(self):
        
        self.current_pass = self.currentpassword_ed.text()
        self.new_pass = self.new_password_ed.text()
        
        self.conn = sqlite3.connect('dbs/Auth.db')
        self.c = self.conn.cursor()

        self.c.execute('SELECT password FROM Auth')
        self.old_password = self.c.fetchone()[0]

        if self.current_pass == self.old_password:
            self.c.execute('update Auth set password=?',(self.new_pass,))
            self.conn.commit()
            QMessageBox.information(self,'password changed','Password Changed successfully ! ')
            self.currentpassword_ed.clear()
            self.new_password_ed.clear()
            self.close()
        else:
            QMessageBox.warning(self,'Wrong Password','Current password is wrong ! TRy Again')

    def closeFUNC(self):
        self.close()  
        self.click_check = 0
    def minuFUNC(self):
        self.showMinimized()
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except:
            pass

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
        
class login_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 1200
        self.height = 700
        self.x = GetSystemMetrics(0)# get width res
        self.y = GetSystemMetrics(1)# get height res

        self.setWindowIcon(QIcon('assets/logo.png'))

        # Create a label widget and set its pixmap
        self.wall = QPixmap('assets/BG-2.JPG').scaled(self.width,self.height)
        self.pix = QLabel(self)
        self.pix.setGeometry(0,0,self.width,self.height)
        self.pix.setPixmap(self.wall)

        self.App_name = "SpendWise v1.0.1"
        self.copyrights = QLabel(f"© ABNS•DEVS SPENDWISE APP 2024 ",self)
        self.copyrights.setStyleSheet('color:silver;font-weight:bold;font-size:10px;background:transparent')
        self.copyrights.setGeometry(0,int(self.height-20),self.width,20)
        self.copyrights.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        self.w_center = (self.x - self.width)/2 # get width center point
        self.h_center = (self.y - self.height)/2# get height center point

        

        self.bg_titlebar = "transparent"
        self.frames_bg = "transparent"
        self.frames_bg2 = "transparent"
        self.bg = "#192a56"
        self.sec_bg = "#273c75"
        self.TitleWidth = self.width
        self.TitleHeight = 40
        self.TitleBtns = self.TitleHeight
        
        self.setGeometry(int(self.w_center),int(self.h_center),self.width,self.height)
        self.setWindowTitle(f"{self.App_name}")
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(f'background:{self.bg};color:white')
        self.titlebar = QFrame(self)
        self.titlebar.setGeometry(0,0,self.TitleWidth,self.TitleHeight)
        self.titlebar.setStyleSheet(f'background:{self.bg_titlebar};border:none')

        self.titlelog = QLabel(f"{self.App_name}",self.titlebar)
        self.titlelog.setStyleSheet('color:#3694c8;font-weight:bold;font-size:14px')
        self.titlelog.setGeometry(0,0,self.width,self.TitleHeight)
        self.titlelog.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        self.closeBtn = QPushButton("•",self.titlebar)
        self.closeBtn.setGeometry(self.width-self.TitleBtns,0,self.TitleBtns,self.TitleBtns)
        self.closeBtn.clicked.connect(self.closeFUNC)
        self.closeBtn.setStyleSheet("QPushButton""{"
            "border:none;"
            "background:transparent;"
            "color:red;"
            "font-weight: bold;"
            "padding-top:-5px;"
            "font-size:35px;"
            "}"

            "QPushButton::hover" "{" 
            "background:rgba(0,0,0,.1);" 
            
            "}"
            )

        self.MinBtn = QPushButton("•",self.titlebar)
        self.MinBtn.setGeometry(self.width-self.TitleBtns*2,0,self.TitleBtns,self.TitleBtns)
        self.MinBtn.clicked.connect(self.minuFUNC)
        self.MinBtn.setStyleSheet("QPushButton""{"
            "border:none;"
            "color:orange;"
            "background:transparent;"
            "padding-top:-5px;"
            "font-weight: bold;"
            "font-size:35px;"
   
            "}"

            "QPushButton::hover" "{" 
            "background:rgba(0,0,0,.1);" 
            "}"
            )
        


        #--------------------------------------------------------------------
        self.log_lab = QLabel("WELCOME BACK !",self)
        self.log_lab.setStyleSheet(f'color:#3694c8;font-weight:bold;font-size:90px;background:transparent') 
        self.log_lab.setGeometry(0,100,self.width,100)
        self.log_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)




        self.password_ed = QLineEdit(self)
        self.password_ed.setStyleSheet(f'background:#3694c8;border-radius:10px;color:white;font-weight:bold;font-size:30px;border:none') 
        self.password_ed.setGeometry(400,300,400,100)
        self.password_ed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_ed.setPlaceholderText('password')
        self.password_ed.setEchoMode(QLineEdit.EchoMode.Password)

        self.Log_btn = QPushButton("Login",self)
        self.Log_btn.setGeometry(400,415,400,80)
        self.Log_btn.setStyleSheet(f'background:#4ebd85;border-radius:10px;color:white;font-weight:bold;font-size:30px;border:none') 
        self.Log_btn.clicked.connect(self.Auth)
        self.Log_btn.setShortcut('Return')


        self.res_btn = QPushButton("Change password",self)
        self.res_btn.setGeometry(10,int(self.height-50),150,40)
        self.res_btn.setStyleSheet(f'background:#4ebd85;border-radius:5px;color:white;font-size:15px;border:none') 
        self.res_btn.clicked.connect(self.respass)




    def respass(self):
        self.win = passrest_window()
        self.win.show()
    
    def Auth(self):
        self.password = self.password_ed.text()

        
        self.conn = sqlite3.connect('dbs/Auth.db')
        self.c = self.conn.cursor()

        self.c.execute('SELECT password FROM Auth')
        self.passw = self.c.fetchone()[0]
        
    
        if self.password == self.passw:
            self.window = MainWindow()
            self.window.show()
            self.close()
        else:
            QMessageBox.warning(self,'Oops ! ',"Wrong Username Or Password !")

        self.conn.commit()
        self.conn.close()
        
    def closeFUNC(self):
        self.close()  
        self.click_check = 0
    def minuFUNC(self):
        self.showMinimized()
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except:
            pass







class records_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 1200
        self.height = 700
        self.x = GetSystemMetrics(0)# get width res
        self.y = GetSystemMetrics(1)# get height res

        self.setWindowIcon(QIcon('assets/logo.png'))

        # Create a label widget and set its pixmap
        self.wall = QPixmap('assets/BG-2.JPG').scaled(self.width,self.height)
        self.pix = QLabel(self)
        self.pix.setGeometry(0,0,self.width,self.height)
        self.pix.setPixmap(self.wall)

        self.App_name = "SpendWise v1.0.1"
        self.copyrights = QLabel(f"© ABNS•DEVS SPENDWISE APP 2024 ",self)
        self.copyrights.setStyleSheet('color:silver;font-weight:bold;font-size:10px;background:transparent')
        self.copyrights.setGeometry(0,int(self.height-20),self.width,20)
        self.copyrights.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        self.w_center = (self.x - self.width)/2 # get width center point
        self.h_center = (self.y - self.height)/2# get height center point

        

        self.bg_titlebar = "transparent"
        self.frames_bg = "transparent"
        self.frames_bg2 = "transparent"
        self.bg = "#192a56"
        self.sec_bg = "#273c75"
        self.TitleWidth = self.width
        self.TitleHeight = 40
        self.TitleBtns = self.TitleHeight
        
        self.setGeometry(int(self.w_center),int(self.h_center),self.width,self.height)
        self.setWindowTitle(f"{self.App_name}")
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(f'background:{self.bg};color:white')
        self.titlebar = QFrame(self)
        self.titlebar.setGeometry(0,0,self.TitleWidth,self.TitleHeight)
        self.titlebar.setStyleSheet(f'background:{self.bg_titlebar};border:none')

        self.titlelog = QLabel(f"{self.App_name}",self.titlebar)
        self.titlelog.setStyleSheet('color:#3694c8;font-weight:bold;font-size:14px')
        self.titlelog.setGeometry(0,0,self.width,self.TitleHeight)
        self.titlelog.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        self.closeBtn = QPushButton("•",self.titlebar)
        self.closeBtn.setGeometry(self.width-self.TitleBtns,0,self.TitleBtns,self.TitleBtns)
        self.closeBtn.clicked.connect(self.closeFUNC)
        self.closeBtn.setStyleSheet("QPushButton""{"
            "border:none;"
            "background:transparent;"
            "color:red;"
            "font-weight: bold;"
            "padding-top:-5px;"
            "font-size:35px;"
            "}"

            "QPushButton::hover" "{" 
            "background:rgba(0,0,0,.3);" 
            
            "}"
            )

        self.MinBtn = QPushButton("•",self.titlebar)
        self.MinBtn.setGeometry(self.width-self.TitleBtns*2,0,self.TitleBtns,self.TitleBtns)
        self.MinBtn.clicked.connect(self.minuFUNC)
        self.MinBtn.setStyleSheet("QPushButton""{"
            "border:none;"
            "color:orange;"
            "background:transparent;"
            "padding-top:-5px;"
            "font-weight: bold;"
            "font-size:35px;"
   
            "}"

            "QPushButton::hover" "{" 
            "background:rgba(0,0,0,.3);" 
            "}"
            )
        


        #--------------------------------------------------------------------
        from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
        self.log_lab = QLabel("RECORDS TABLE",self)
        self.log_lab.setStyleSheet(f'color:#192a56;font-weight:bold;font-size:20px;background:rgba(255,255,255,.8)') 
        self.log_lab.setGeometry(0,50,self.width,30)
        self.log_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.box = QFrame(self)
        self.box.setGeometry(70,100,int(self.width-140),int(self.height-130))
        self.box.setStyleSheet('background:rgba(255,255,255,.5);border-radius:10px')

        self.home_btn = QPushButton("Home",self.titlebar)
        self.home_btn.setGeometry(10,5,100,20)
        self.home_btn.setStyleSheet('background:#3694c8;color:white;border:none;border-radius:10px;font-weight:bold;font-size:17px')
        self.home_btn.clicked.connect(self.home_route)
        
        # Connect to the SQLite database
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("dbs/expenses.db")

        if not self.db.open():
            print("Error: Could not open database")
            return

        # Create the model and set the table name
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("exps")
        self.model.select()  # Fetch data from the table

        # Create the table view and set the model
        self.tableView = QTableView(self.box)
        self.tableView.setGeometry(0,0,int(self.width-140),int(self.height-130))
        self.tableView.setStyleSheet('background:rgba(255,255,255,.7);color:#273c75;font-weight:bold;font-size:20px')
        self.tableView.setModel(self.model)
        
        self.tableView.setColumnWidth(0, 260)  # Set width of first column
        self.tableView.setColumnWidth(1, 260)  # Set width of second column
        self.tableView.setColumnWidth(2, 260)
        self.tableView.setColumnWidth(3, 260)

    def home_route(self):
        try:
            self.window = MainWindow()
            self.window.show()
            self.close()
        except:
            pass

    def closeFUNC(self):
        self.close()  
        self.click_check = 0
    def minuFUNC(self):
        self.showMinimized()
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except:
            pass







applog = QApplication(sys.argv)
winlog = login_window()
winlog.show()
applog.exec()








