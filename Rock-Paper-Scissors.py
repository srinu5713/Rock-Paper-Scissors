# importing required modules

from tkinter import *
from PIL import Image, ImageTk
from random import randint

# intiating  main window

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("860x450")
root.resizable(False, False)

# storing the pictures

rock_img = ImageTk.PhotoImage(Image.open("Images\paper.png"))
paper_img = ImageTk.PhotoImage(Image.open("Images\paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Images\scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("Images\rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("Images\paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Images\scissors.png"))

# labeling the initial picture

user_label = Label(root, image=scissor_img)
comp_label = Label(root, image=scissor_img_comp)
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# intiating scores

playerScore = Label(root, text=0, font=100, fg="black")
computerScore = Label(root, text=0, font=100, fg="black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# player indicators

user_indicator = Label(root, font=50, text="USER", fg="black")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       fg="black")
user_indicator.grid(row=0, column=3)

comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, fg="black", text="")
msg.grid(row=3, column=2)

# update message


def updateMessage(x):
    msg['text'] = x

# update user score


def updateUserScore():
    score = playerScore["text"]
    score += 1
    playerScore["text"] = score

# update computer score


def updateCompScore():
    score = computerScore["text"]
    score += 1
    computerScore["text"] = score

# check winner


def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!! 😊")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose 😔")
            updateCompScore()
        else:
            updateMessage("You Win 😊")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose 😔")
            updateCompScore()
        else:
            updateMessage("You Win 😊")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose 😔")
            updateCompScore()
        else:
            updateMessage("You Win 😊")
            updateUserScore()

    else:
        pass

# update choices


choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)

# reset game


def reset_scores():
    playerScore.configure(text=0)
    computerScore.configure(text=0)
    msg.configure(text="")
    user_label.configure(image=scissor_img)
    comp_label.configure(image=scissor_img_comp)


# buttons

rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="black", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="black", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="black", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

reset = Button(root, text="Reset Game", command=reset_scores,
               font=10, fg="red").grid(row=4, column=0)

root.mainloop()
