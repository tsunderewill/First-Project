import tkinter as tk
import random 


root = tk.Tk()
root.resizable(0,0)
root.wm_title("Rock, Paper, Scissor")


frame1 = tk.Frame(root)
frame1.pack(side=tk.BOTTOM)

frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP, pady = 20)

text = tk.Label(frame2, text="選べ", font = "Times 50")
text.pack(side=tk.BOTTOM, pady = 0)

answer = 10


def disappear():
	button3.pack_forget()
	button2.pack_forget()
	button1.pack_forget()
	
def replay():
	PA.pack_forget()
	result.place_forget()
	results.place_forget()
	text.config(text="選べ", font = "Times 50")
	button2.pack(side=tk.RIGHT, pady = 20, padx=15)
	button1.pack(side=tk.RIGHT, pady = 20,  padx=15)
	button3.pack(side=tk.RIGHT, pady = 100, padx=15)
	
PA = tk.Button(frame2, text="Play Again", width=30, command = replay)
PA.pack_forget()


RP = tk.PhotoImage(file="hap.png")
result = tk.Label(image=RP)
result.pack_forget()
	
	
def show():
	PA.pack()
	

def scissors():
		show()
		scissorsc()
		disappear()

def scissorsc():
		global answer
		answer = random.randint(0,30)
		if answer == 10:
				answer += 1
		if answer < 10:
			results.place(relx=0.6, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "You Win!")
			text.config(text="scissor cuts paper", font = "Times 35")
			RP.config(file="scissors.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")
		if answer > 10 and answer < 21:
			results.place(relx=0.62, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "You Lose!")
			text.config(text="rock breaks scissor", font = "Times 35")
			RP.config(file="rockbreak.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")
		if answer > 20:
			results.place(relx=0.52, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "tie")
			text.config(text="scissor and scissor", font = "Times 35")
			RP.config(file="scissorandscissor.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")


photo2 = tk.PhotoImage(file="scissor.png")
button2 = tk.Button(frame1, compound=tk.TOP, image=photo2,
    text="scissor",  height=150, width = 100, command = scissors)
button2.pack(side=tk.RIGHT,  padx=15)


def paperc():
		show()
		paper()
		disappear()

def paper():
		global answer
		answer = random.randint(0,30)
		if answer == 10:
				answer += 1
		if answer < 10:
			text.config(text="scissor cuts paper", font = "Times 35")
			results.place(relx=0.62, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "You Lose!")
			RP.config(file="scissors.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")
			
		if answer > 10 and answer < 21:
			results.place(relx=0.6, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "You Win!")
			text.config(text="paper covers rock", font = "Times 35")
			RP.config(file="papercover.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")
		if answer > 20:
			results.place(relx=0.52, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "tie")
			text.config(text="paper and paper", font = "Times 35")
			RP.config(file="paperandpaper.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")
		


photo1 = tk.PhotoImage(file="paper.png")
button1 = tk.Button(frame1, compound=tk.TOP, image=photo1,
    text="paper",  height=150, width = 100, command=paperc)
button1.pack(side=tk.RIGHT,  pady = 20, padx=15)

def rock():
		show()
		rockc()
		disappear()
	
def rockc():
		global answer
		answer = random.randint(0,30)
		if answer == 10:
				answer += 1
		if answer < 10:
			results.place(relx=0.6, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "You Win!")
			text.config(text="rock breaks scissors", font = "Times 35")
			RP.config(file="rockbreak.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")
			
		if answer > 10 and answer < 21:
			results.place(relx=0.62, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "You Lose!")
			text.config(text="paper covers rock", font = "Times 35")
			RP.config(file="papercover.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")
		if answer > 20:
			results.place(relx=0.52, rely=0.92, x=-0, y=-0,anchor="se")
			results.config(text = "tie")
			text.config(text="rock and rock", font = "Times 35")
			RP.config(file="rockrock.png")
			result.place(relx=0.93, rely=1.0, x=-0, y=-0,anchor="se")
		
		

photo3 = tk.PhotoImage(file="rock.png")
button3 = tk.Button(frame1, compound=tk.TOP, image=photo3,
    text="rock", height=150, width = 100, command= rock)
button3.pack(side=tk.RIGHT, pady = 100, padx=15 )


results = tk.Label(text="ook ook", font = "Times 20", fg = "red")
	

root.geometry("500x500")
button1.image = photo1
root.mainloop()