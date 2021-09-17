from tkinter import*

def btnClick(numbers):  # When clicked a number
    global operator  # The calculated math will be stored here
    marks = ["*", "/", "+", "-"]  # Marks that can cause math errors
    error = False  # Boolean to check if inputs are allowed

    for i in marks: # Goes through all possible duplicate operations for errors
        if numbers == i:  # If the input number is same as one of operators
            if numbers == "-" and operator == "":  # If input is minus and operator is empty, it is allowed.
                continue
            else:
                try:
                    if operator[-1] in marks or operator == "":  # Check for last element in operator and if it is
                        text_Input.set("Error")     # one of operators, it causes an error. Also cant be 1st element
                        operator = ""       # Set operator to be empty again and show "error" in display.
                        error = True        # Set boolean Error to be true, so it won't be processed further.
                except:
                    text_Input.set("Error")
                    operator = ""
                    error = True

        continue
    if error == False:      # If no errors occur, add the input into operator as string.
        operator = operator + str(numbers)
        text_Input.set(operator)        # Show operator in display.

def btnClearDisplay():  # This function is for the C button to clear display
    global operator
    operator = ""       # Sets operator string to empty
    text_Input.set("")      # Resets display

def btnEqualsInput():   # Function for equals- button.
    global operator
    try:                                # if the math is correct, following will be done:
        sumup = str(eval(operator))     # Evaluates the string put in operator and puts it into variable sumup as str.
        text_Input.set(sumup)           # Puts the sum into the display
        operator = sumup                   # Clears the operator
    except:                             # This happens when the math is erroneous.
        text_Input.set("Error")         # Such as when trying to divide by zero.
        operator = ""


cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

# FirstRow ===========================================================
txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable=text_Input, bd=30,
 insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

btn7=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="7",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="8",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="9",command=lambda:btnClick(9)).grid(row=1,column=2)

Addition=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="+",command=lambda:btnClick("+")).grid(row=1,column=3)



# Second Row =====================================================
btn4=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="4",command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="5",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="6",command=lambda:btnClick(6)).grid(row=2,column=2)

Substraction=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="-",command=lambda:btnClick("-")).grid(row=2,column=3)



# Third Row =====================================================
btn1=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="1",command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="2",command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="3",command=lambda:btnClick(3)).grid(row=3,column=2)

Multiply=Button(cal,padx=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="*",command=lambda:btnClick("*")).grid(row=3,column=3)




# Fourth Row =====================================================
btn0=Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="0",command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="C",command= btnClearDisplay).grid(row=4,column=1)

btnEquals=Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="=",command = btnEqualsInput).grid(row=4,column=2)

Division=Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
text="/",command=lambda:btnClick("/")).grid(row=4,column=3)







cal.mainloop()