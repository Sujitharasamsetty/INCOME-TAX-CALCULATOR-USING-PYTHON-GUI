from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime

class Income_Tax:

    def __init__(self, root):
        self.root = root
        self.root.title("Income Tax and Wages Calculator")
        self.root.geometry("1360x800+0+0")
        self.root.configure(background= 'cadet blue')

        #==================================Frame=Widget=====================================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=10, width=1350, padx=35, bg='cadetblue', relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,width=43,font=('arial',35,'bold'),text="Income Tax and Wages Calculator"
                               ,padx=11, fg="white",bg='cadetblue')
        self.lblTitle.grid()


        BottomFrame =LabelFrame(MainFrame, bd=10, pady=5, width=1330, height=70,padx=35,  relief = RIDGE,
                                 font=('arial',20,'bold'),text ="Tax and Wages Summary",fg="white" ,bg='cadetblue')

        BottomFrame.pack(side=BOTTOM)

        
  
        MiddleFrame =Frame(MainFrame, bd=10, width=1350,height=100, padx=32, relief=RIDGE ,bg='cadetblue')
        MiddleFrame.pack(side=BOTTOM)

        DataFrame =LabelFrame(MainFrame, bd=10, width=1350, height=400, padx=34, relief=RIDGE ,bg='cadetblue')
        DataFrame.pack(side=BOTTOM)

        UpperFrameLEFT =Frame(DataFrame, bd=10, width=700, height=220, padx=20, relief=RIDGE)
        UpperFrameLEFT.pack(side=LEFT)

        UpperFrameRIGHT =Frame(DataFrame, bd=10, width=570, height=220, padx=20, pady=4, relief=RIDGE ,bg='cadetblue')
        UpperFrameRIGHT.pack(side=RIGHT)


        LowerFrameLEFT =LabelFrame(MiddleFrame, bd=10, width=720, height=220,padx=20,pady=4,  relief = RIDGE,
                                 font=('arial',20,'bold'),bg='cadet blue',fg='white')

        LowerFrameLEFT.pack(side=LEFT)


        
        LowerFrameRIGHT =LabelFrame(MiddleFrame, bd=10, width=550, height=220,padx=20, relief = RIDGE,
                                 font=('arial',20,'bold'))

        LowerFrameRIGHT.pack(side=RIGHT)

        #======================================Variable============================================
        
        TaxPeriod = StringVar()
        TaxCode = StringVar()
        Payment = StringVar()
        PayDate = StringVar()
        EmpRef  = StringVar()
        NonTaxableWages = StringVar()
        TaxableWages = StringVar()
        TaxPaid = StringVar()
        PayBeforeTax = StringVar()
        NetPay= StringVar()
        GrossPay= StringVar()
        Deduction= StringVar()
        NINumber= StringVar()
        NICode= StringVar()
        Employer= StringVar()
        Employee= StringVar()
        JobTitle= StringVar()
        PayBeforeTax.set(1200)
        #=====================================Functions============================================

        def iExit():
              iExit = tkinter.messagebox.askyesno("Income Tax and Wages Calculator","Confirm if you want to exit")
              if iExit > 0:
                 root.destroy()
                 return

        def Reset():
              TaxPeriod.set("Select Tax Period")
              TaxCode.set("Select Tax Code")
              Payment.set("Select Paymemt")
              PayDate.set("")
              EmpRef.set("")
              NonTaxableWages.set("")
              TaxableWages.set("")
              TaxPaid.set("")
              PayBeforeTax.set("")
              NetPay.set("")
              GrossPay.set("")
              Deduction.set("")
              NINumber.set("")
              NICode.set("")
              Employer.set("")
              Employee.set("")
              JobTitle.set("")
              
        def PayDay():
              d1 = datetime.date.today()
              PayDate.set(d1)
              NonTaxableWages.set(PayBeforeTax.get())

              q = float(Payment.get())
              p = float(NonTaxableWages.get())
              TaxableWages.set(q - p)

              x = random.randint(10020, 709929)
              randomRef =str(x)
              EmpRef.set(randomRef)

        def EmpTaxCode(evt):
              values =str(self.cboTaxCode.get())
              TCode  = values
              if (TCode == "TC12100"):
                  Payment.set(PayBeforeTax.get())
                  PayDay()
                  TPaid = float(TaxableWages.get())
                  if (TPaid <=1200) :
                      TaxPaid.set(TPaid)

            
              elif (TCode == "TC12200"):
                  Payment.set("1720")
                  PayDay()
                  TPaid = float(TaxableWages.get())
                  if (TPaid <=1720) :
                      TaxPaid.set((TPaid * 20)/100)

              elif (TCode == "TC12300"):
                  Payment.set("2230")
                  PayDay()
                  TPaid = float(TaxableWages.get())
                  if (TPaid <=2230) :
                      TaxPaid.set((TPaid * 25)/100)

              elif (TCode == "TC12400"):
                  Payment.set("2740")
                  PayDay()
                  TPaid = float(TaxableWages.get())
                  if (TPaid <=2740) :
                      TaxPaid.set((TPaid * 30)/100)

              elif (TCode == "TC12500"):
                  Payment.set("3200")
                  PayDay()
                  TPaid = float(TaxableWages.get())
                  if (TPaid <=3200) :
                      TaxPaid.set((TPaid * 35.7)/100)

        def WagesAfterTax():
            n = float(Payment.get())
            s = float(TaxPaid.get())
            AfterTax = (n - s)
            G = "£",str('%.2f'%(n))
            GrossPay.set(G)
            D = "£",str('%.2f'%(s))
            Deduction.set(D)
            Pay = AfterTax
            iTax = "£",str('%.2f'%((Pay)))
            NetPay.set(iTax)
            PayDay()
                  
   
                             

                             
                             
                             
                     
                     
                     
            
            

             

              
           
            











                
             
         
          







        
        #=====================================Widget============================================


        self.lblTaxPeriod =Label(UpperFrameRIGHT, font=('arial',18,'bold'), text="Tax Period: ",padx=1,pady=2,
                                  bg='cadetblue',fg='white')
        self.lblTaxPeriod.grid(row=0, column=0,sticky=W)


        self.cboTaxPeriod=ttk.Combobox(UpperFrameRIGHT,textvariable=TaxPeriod,state='readonly',
                                       font=('arial',22,'bold'),width=24)
        self.cboTaxPeriod['value']= ('select Tax Period','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
        self.cboTaxPeriod.current(0)
        self.cboTaxPeriod.grid(row=0, column=1, pady=2)

        self.lblTaxCode =Label(UpperFrameRIGHT, font=('arial',18,'bold'), text="Tax Code: ",padx=1,pady=2,
                                  bg='cadetblue',fg='white')
        self.lblTaxCode.grid(row=1, column=0,sticky=W)

        self.cboTaxCode=ttk.Combobox(UpperFrameRIGHT,textvariable=TaxCode,state='readonly',
                                       font=('arial',22,'bold'),width=24)

        self.cboTaxCode.bind("<<Comboboxselected>>",EmpTaxCode)
        
        self.cboTaxCode['value']= ('select Tax Code','TC12100','TC12200','TC12300','TC12400','TC12500')
        self.cboTaxCode.current(0)
        self.cboTaxCode.grid(row=1, column=1, pady=2)

        self.lblNINumber =Label(UpperFrameRIGHT, font=('arial',18,'bold'), text="NI Number: ",padx=1,pady=2,
                                  bg='cadetblue',fg='white')
        self.lblNINumber.grid(row=2, column=0,sticky=W)

        self.txtNINumber = Entry(UpperFrameRIGHT, width=21,font=('arial',26,'bold'),textvariable=NINumber)
        self.txtNINumber.grid(row=2,column=1,pady=2)

        self.lblPayDueDay =Label(UpperFrameRIGHT, font=('arial',18,'bold'), text="NI Code: ",padx=1,pady=2,
                                  bg='cadetblue',fg='white')
        self.lblPayDueDay.grid(row=3, column=0,sticky=W)

        self.txtNICode = Entry(UpperFrameRIGHT, width=21,font=('arial',26,'bold'),textvariable=NICode)
        self.txtNICode.grid(row=3,column=1,pady=2)
        #======================================Upper_LEFTFrame============================================
        
        self.lblReference = Label(UpperFrameLEFT,font=('arial',18,'bold'),text="ReferenceNo: ",padx=1,pady=2)
        self.lblReference.grid(row=0,column=0,sticky=W)

        self.txtReference = Entry(UpperFrameLEFT, width=23,textvariable=EmpRef,font=('arial',26,'bold'))
        self.txtReference.grid(row=0,column=1,pady=2)

        self.lblEmployer = Label(UpperFrameLEFT,font=('arial',18,'bold'),text="Employer: ",padx=1,pady=2)
        self.lblEmployer.grid(row=1,column=0,sticky=W)

        self.txtEmployer = Entry(UpperFrameLEFT, width=23,font=('arial',26,'bold'),textvariable=Employer)
        self.txtEmployer.grid(row=1,column=1,pady=2)

        self.lblEmployee = Label(UpperFrameLEFT,font=('arial',18,'bold'),text="Employee: ",padx=1,pady=2)
        self.lblEmployee.grid(row=2,column=0,sticky=W)

        self.txtEmployee = Entry(UpperFrameLEFT, width=23,font=('arial',26,'bold'),textvariable=Employee)
        self.txtEmployee.grid(row=2,column=1,pady=2)

        self.lblJobTitle = Label(UpperFrameLEFT,font=('arial',18,'bold'),text="Job Title: ",padx=1,pady=2)
        self.lblJobTitle.grid(row=3,column=0,sticky=W)

        self.txtJobTitle = Entry(UpperFrameLEFT, width=23,font=('arial',26,'bold'),textvariable= JobTitle)
        self.txtJobTitle.grid(row=3,column=1,pady=2)

        #======================================RightFrame_Button============================================

        self.lblDate = Label(LowerFrameRIGHT,font=('arial',18,'bold'),text="Date: ",padx=1,pady=2)
        self.lblDate.grid(row=0,column=0,sticky=W)

        self.txtDate = Entry(LowerFrameRIGHT, width=25,textvariable=PayDate,font=('arial',26,'bold'))
        self.txtDate.grid(row=0,column=1,pady=2)

        self.lblGrossPay = Label(LowerFrameRIGHT,font=('arial',16,'bold'),text="GrossPay: ",padx=1,pady=2)
        self.lblGrossPay.grid(row=1,column=0,sticky=W)

        self.txtGrossPay = Entry(LowerFrameRIGHT, width=25,font=('arial',26,'bold'),textvariable=GrossPay)
        self.txtGrossPay.grid(row=1,column=1,pady=2)

        self.lblDeduction = Label(LowerFrameRIGHT,font=('arial',18,'bold'),text="Deduction: ",padx=1,pady=2)
        self.lblDeduction.grid(row=2,column=0,sticky=W)

        self.txtDeduction = Entry(LowerFrameRIGHT, width=25,font=('arial',26,'bold'),textvariable=Deduction)
        self.txtDeduction.grid(row=2,column=1,pady=2)

        self.lblNetPay = Label(LowerFrameRIGHT,font=('arial',18,'bold'),text="Net Pay: ",padx=1,pady=2)
        self.lblNetPay.grid(row=3,column=0,sticky=W)

        self.txtNetPay = Entry(LowerFrameRIGHT, width=25,font=('arial',26,'bold'),textvariable=NetPay)
        self.txtNetPay.grid(row=3,column=1,pady=2)

        #======================================LeftFrame3============================================

        self.lblPayment =Label(LowerFrameLEFT, font=('arial',18,'bold'), text="Payment: ",padx=1,pady=2,
                                  bg='cadetblue',fg='white')
        self.lblPayment.grid(row=0, column=0,sticky=W)


        self.cboPayment=ttk.Combobox(LowerFrameLEFT,textvariable=Payment,state='readonly',
                                       font=('arial',22,'bold'),width=19)
        self.cboPayment['value']= ('select Payment','1200','1720','2230','2740','3200')
        self.cboPayment.current(0)
        self.cboPayment.grid(row=0, column=1, pady=2)

        self.lblIncome =Label(LowerFrameLEFT, font=('arial',18,'bold'), text="Income Not Taxed: ",padx=1,pady=2,
                                  bg='cadetblue',fg='white')
        self.lblIncome.grid(row=1, column=0,sticky=W)

        self.txtIncome = Entry(LowerFrameLEFT, width=17,font=('arial',26,'bold'),textvariable=NonTaxableWages)
        self.txtIncome.grid(row=1,column=1,pady=2)

        self.lblTaxableWages =Label(LowerFrameLEFT, font=('arial',18,'bold'), text="Taxable Wages: ",padx=1,pady=2,
                                  bg='cadetblue',fg='white')
        self.lblTaxableWages.grid(row=2, column=0,sticky=W)

        self.txtTaxableWages = Entry(LowerFrameLEFT, width=17,font=('arial',26,'bold'),textvariable=TaxableWages)
        self.txtTaxableWages.grid(row=2,column=1,pady=2)

        self.lblTaxPaid =Label(LowerFrameLEFT, font=('arial',18,'bold'), text="Tax Paid: ",padx=1,pady=2,
                                  bg='cadetblue',fg='white')
        self.lblTaxPaid.grid(row=3, column=0,sticky=W)

        self.txtTaxPaid = Entry(LowerFrameLEFT, width=17,font=('arial',26,'bold'),textvariable=TaxPaid)
        self.txtTaxPaid.grid(row=3,column=1,pady=2)


        #======================================Buttons====================================================
        self.btnTotal = Button(BottomFrame, padx=37,pady=6,bd=4,fg="White",font=('arial',21,'bold'),width=20,
                                bg="cadet blue" ,text="Calculate Wages",command=WagesAfterTax).grid(row=0,column=0)


        self.btnReset = Button(BottomFrame, padx=37,pady=6,bd=4,fg="White",font=('arial',21,'bold'),width=20,
                                bg="cadet blue" ,text="Reset",command=Reset).grid(row=0,column=1)

        self.btnExit = Button(BottomFrame, padx=37,pady=6,bd=4,fg="White",font=('arial',21,'bold'),width=20,
                                bg="cadet blue" ,text="Exit",command=iExit).grid(row=0,column=2)
        
        

if __name__=='__main__':
    root = Tk()
    application = Income_Tax(root)
    root.mainloop()


        



        
        

        





        

        



        


        

        

        


      


        

        

        
  
