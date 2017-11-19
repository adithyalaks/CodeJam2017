#this module will define functions that will be used to generate our UI
# it will need to display graphics to the user (button, map, etc)
# it will need to grab user input (ie. when they click a submit button)
import sys
from PyQt5 import QtCore,QtWidgets,QtWebKitWidgets,QtWidgets, QtGui
import mapping
import processing
import pandas as pd
import webbrowser, os
##Create a class to deal with a UI object, composing of a main window.
class Window(QtWidgets.QMainWindow):
    ##Object instantiation variables.
    def __init__(self):
        super(Window,self).__init__()
        
        self.mainLayout = self.mainLayout()
        self.setWindowTitle("Index Visualisation-CodeJam2017")
        self.setCentralWidget(self.mainLayout)
        self.show()
        ##Final layout of window w

    ## Function used to parse user input of indicators and weights, and pass these to
    ## to the processing.py and mapping.py modules containing plotting and processing functions.
    ## This function is triggered when a signal from the submit button is emitted.
    def process_data(self):
        in1=self.option1_cb.currentText()
        in2=self.option2_cb.currentText()
        in3=self.option3_cb.currentText()
        in4=self.option4_cb.currentText()
        in5=self.option5_cb.currentText()
        indicator = [in1,in2,in3,in4,in5]
        
        wt1=float(self.option1_le.text())
        wt2=float(self.option2_le.text())
        wt3=float(self.option3_le.text())
        wt4=float(self.option4_le.text())
        wt5=float(self.option5_le.text())
        weight= [wt1,wt2,wt3,wt4,wt5]
        
        year = self.year_cb.currentText()
        ##This handles the case where a user inputs a sum of weights greater than 1.
        weight_sum = sum(weight)
        indiweight = {}
        for i in range(5):
            weight[i]= (weight[i]/(weight_sum+0.000001))
            indiweight[indicator[i]] = weight[i]
        

        processing.computeIndex(year,indiweight)
        indexdf= pd.read_csv("index.csv")
        mapping.plot(indexdf, "Index")
        webbrowser.open('file:///C:/Users/Imad/Documents/GitHub/CodeJam2017/CodeJam2017/d3-world-map.html')
        
        

    ## This function deals with building the layout of the UI. 
    def mainLayout(self):
        w = QtWidgets.QWidget()
        w.setGeometry(50,50,1000,1000)
        vbox = QtWidgets.QVBoxLayout()

        list_options = ['GNI per capita, Atlas method (current US$)', 'Mortality rate, under-5 (per 1,000)', 'Mortality rate, neonatal (per 1,000 live births)', 'Improved water source, rural (% of rural population with access)', 'Improved water source, urban (% of urban population with access)', 'Improved water source (% of population with access)', 'Immunization, HepB3 (% of one-year-old children)', 'Immunization, Hib3 (% of children ages 12-23 months)', 'Immunization, BCG (% of one-year-old children)', 'Immunization, DPT (% of children ages 12-23 months)', 'Immunization, measles (% of children ages 12-23 months)', 'Immunization, Pol3 (% of one-year-old children)', 'Lifetime risk of maternal death (%)', 'Improved sanitation facilities (% of population with access)', 'Improved sanitation facilities, rural (% of rural population with access)', 'Improved sanitation facilities, urban (% of urban population with access)', 'Maternal mortality ratio (modeled estimate, per 100,000 live births)', 'People practicing open defecation, rural (% of rural population)', 'People practicing open defecation (% of population)', 'Tuberculosis treatment success rate (% of new cases)', 'Tuberculosis case detection rate (all forms)', 'Incidence of tuberculosis (per 100,000 people)', 'Tuberculosis death rate (per 100,000 people)', 'Prevalence of tuberculosis (per 100,000 population)', 'Health expenditure per capita, PPP', 'Health expenditure, public (% of government expenditure)', 'Health expenditure, total (% of GDP)', 'Labor force, female (% of total labor force)', 'Unemployment, female (% of female labor force)', 'Unemployment, male (% of male labor force)', 'Unemployment, total (% of total labor force)', 'Prevalence of undernourishment (% of population)', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'Mortality rate, adult, female (per 1,000 female adults)', 'Mortality rate, adult, male (per 1,000 male adults)', 'Birth rate, crude (per 1,000 people)', 'Death rate, crude (per 1,000 people)', 'Mortality rate, infant (per 1,000 live births)', 'Life expectancy at birth, female (years)', 'Life expectancy at birth, total (years)', 'Life expectancy at birth, male (years)', 'Fertility rate, total (births per woman)', 'Survival to age 65, female (% of cohort)', 'Survival to age 65, male (% of cohort)', 'Rural population (% of total population)', 'Urban population growth (annual %)', 'Urban population (% of total)']
        choice_form = QtWidgets.QFormLayout()
     
        ##browser = QtWebKitWidgets.QWebView()
        ##browser.load(QtCore.QUrl.fromLocalFile("file///C:/Users/Imad/Documents/GitHub/CodeJam2017/CodeJam2017/test.html"))

        option1_label = QtWidgets.QLabel("Option 1:")
        self.option1_cb = QtWidgets.QComboBox()
        self.option1_cb.addItems(list_options)
        self.option1_le = QtWidgets.QLineEdit()
        self.option1_le.setValidator(QtGui.QDoubleValidator(0.00,1.00,2))
        self.option1_le.setText('0.00')

        option2_label = QtWidgets.QLabel("Option 2:")
        self.option2_cb = QtWidgets.QComboBox()
        self.option2_cb.addItems(list_options)
        self.option2_le = QtWidgets.QLineEdit()
        self.option2_le.setValidator(QtGui.QDoubleValidator(0.00,1.00,2))
        self.option2_le.setText('0.00')

        option3_label = QtWidgets.QLabel("Option 3:")
        self.option3_cb = QtWidgets.QComboBox()
        self.option3_cb.addItems(list_options)
        self.option3_le = QtWidgets.QLineEdit()
        self.option3_le.setValidator(QtGui.QDoubleValidator(0.00,1.00,2))
        self.option3_le.setText('0.00')

        option4_label = QtWidgets.QLabel("Option 4:")
        self.option4_cb = QtWidgets.QComboBox()
        self.option4_cb.addItems(list_options)
        self.option4_le = QtWidgets.QLineEdit()
        self.option4_le.setValidator(QtGui.QDoubleValidator(0.00,1.00,2))
        self.option4_le.setText('0.00')

        option5_label = QtWidgets.QLabel("Option 5:")
        self.option5_cb = QtWidgets.QComboBox()
        self.option5_cb.addItems(list_options)
        self.option5_le = QtWidgets.QLineEdit()
        self.option5_le.setValidator(QtGui.QDoubleValidator(0.00,1.00,2))
        self.option5_le.setText('0.00')

        year_label = QtWidgets.QLabel("Year of interest")
        self.year_cb = QtWidgets.QComboBox()
        self.year_cb.addItems(['2010','2011','2012','2013','2014','2015'])

        submit_button = QtWidgets.QPushButton("Submit")
        
        choice_form.addRow(option1_label)
        choice_form.addRow(self.option1_cb,self.option1_le)
        choice_form.addRow(option2_label)
        choice_form.addRow(self.option2_cb,self.option2_le)
        choice_form.addRow(option3_label)
        choice_form.addRow(self.option3_cb,self.option3_le)
        choice_form.addRow(option4_label)
        choice_form.addRow(self.option4_cb,self.option4_le)
        choice_form.addRow(option5_label)
        choice_form.addRow(self.option5_cb,self.option5_le)
        choice_form.addRow(year_label,self.year_cb)
        choice_form.addRow(submit_button)

        submit_button.clicked.connect(self.process_data)
        
        ##vbox.addWidget(browser)
        vbox.addLayout(choice_form)
        w.setLayout(vbox)
        return w        
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
