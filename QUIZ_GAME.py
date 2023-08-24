from tkinter import *    
from tkinter import messagebox as mb   
import json  
 
guiWindow = Tk()   
guiWindow.geometry("810x400")  
guiWindow.title("QUIZ GAME")  

class myQuiz:  
    def __init__(self):       
        self.quesNumber = 0    
        self.displayQuestion()  
        self.optSelected = IntVar()   
        self.options = self.radioButtons()   
        self.displayOptions()   
        self.buttons()  
        self.dataSize = len(question)  
        self.rightAnswer = 0  
  
    def displayResult(self):  
        wrongCount = self.dataSize - self.rightAnswer  
        rightAnswer = f"Correct: {self.rightAnswer}"  
        wrongAnswer = f"Wrong: {wrongCount}"  
        the_score = int(self.rightAnswer / self.dataSize * 100)  
        the_result = f"Score: {the_score}%"  
        mb.showinfo("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}")  

    def checkAnswer(self, quesNumber):  
        if self.optSelected.get() == answer[quesNumber]:  
            return True  

    def nextButton(self):  
        if self.checkAnswer(self.quesNumber):  
            self.rightAnswer += 1  
        self.quesNumber += 1  
             
        if self.quesNumber == self.dataSize:    
            self.displayResult()   
            guiWindow.destroy()  
        else:   
            self.displayQuestion()  
            self.displayOptions()  

    def buttons(self):  
        next_button = Button(  
            guiWindow,  
            text = "Next",  
            command = self.nextButton,  
            width = 10,  
            bg = "green",  
            fg = "white",  
            font = ("ariel", 16, "bold")  
            )  
        next_button.place(x = 340, y = 320)  
        quit_button = Button(  
            guiWindow,  
            text = "Quit",  
            command = guiWindow.destroy,  
            width = 5,  
            bg = "red",  
            fg = "white",  
            font = ("ariel", 16, " bold")  
            )   
        quit_button.place(x = 720, y = 12)  
  
    def displayOptions(self):  
        val = 0  
        self.optSelected.set(0)  
        for opt in opts[self.quesNumber]:  
            self.options[val]['text'] = opt  
            val += 1  

    def displayQuestion(self):  
        quesNumber = Label(  
            guiWindow,  
            text = question[self.quesNumber],  
            width = 60,  
            font = ('ariel', 16, 'bold'),  
            anchor = 'w'  
            )  
        quesNumber.place(x = 70, y = 80)  

    def radioButtons(self):  
        qList = []  
        y_pos = 130   
        while len(qList) < 4:   
            radio_button = Radiobutton(  
                guiWindow,  
                text = " ",  
                variable = self.optSelected,  
                value = len(qList) + 1,  
                font = ("ariel", 14)  
                )  
  
            qList.append(radio_button)  
            radio_button.place(x = 120, y = y_pos)  
            y_pos += 40  
        return qList  

with open('Questions.json') as json_file:  
    data = json.load(json_file)  
   
question = (data['ques'])  
opts = (data['choices'])  
answer = (data[ 'ans'])  
  
quiz = myQuiz()  
guiWindow.mainloop()