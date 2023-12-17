from tkinter import *
from PIL import Image, ImageTk
from random import randint

def rpsgame():
    window= Tk()
    window.title("Rock Paper and Scissor Game")
    window.configure(background="black")
    
    image_rock1=ImageTk.PhotoImage(Image.open("rps//rock.png"))
    image_paper1=ImageTk.PhotoImage(Image.open("rps//paper.png"))
    image_scissor1=ImageTk.PhotoImage(Image.open("rps//scissor.png"))
    image_rock2=ImageTk.PhotoImage(Image.open("rps//rock.png"))
    image_paper2=ImageTk.PhotoImage(Image.open("rps//paper.png"))
    image_scissor2=ImageTk.PhotoImage(Image.open("rps//scissor.png"))


    #score for comp and player
    computer_score= Label(window, text=0,font=("arial",60,"bold"),fg="white",bg="black")
    player_score=Label(window,text=0,font=("arial",60,"bold"), fg="white",bg="black")
    player_score.grid(row=1,column=3)
    computer_score.grid(row=1,column=1)



    #indicator at the top
    player_indicator= Label(window,font=("arial",40,"bold"),
                            text="PLAYER",bg="orange",fg="blue")
    computer_indicator=Label(window,font=("arial",40,"bold"),
                            text="COMPUTER",bg="orange",fg="blue")
    computer_indicator.grid(row=0,column=1)
    player_indicator.grid(row=0,column=3)



    #updating message and score
    def updateMessage(a):
        final_message['text']=a

    def Computer_Update():
        final = int(computer_score['text'])
        final=final+1
        computer_score["text"]=str(final)

    def Player_Update():
        final=int(player_score['text'])
        final+=1
        player_score["text"]=str(final)


    #updateMessage is a function available
    def winner_check(p,c):
        if p==c:
            updateMessage("It's a tie!")
        elif p=="rock":
            if c=="paper":
                updateMessage("Computer has Won!")
                Computer_Update()
            else:
                updateMessage("Player has won!")
                Player_Update()
        elif p=="paper":
            if c=="scissor":
                updateMessage("Computer has Won!")
                Computer_Update()
            else:
                updateMessage("Player has won!")
                Player_Update()
        elif p=="scissor":
            if c=="rock":
                updateMessage("Computer has won!")
                Computer_Update()
            else:
                updateMessage("Player has won !")
                Player_Update()
        else:
            pass
            
    #updating choices w help of images
    to_select=["rock", "paper","scissor"]
    def choice_update(a):
    #rock=0, paper=1,scissor=2
        choice_computer=to_select[randint(0,2)]
        if choice_computer=="rock":
            label_computer.configure(image=image_rock1)
        elif choice_computer=="paper":
            label_computer.configure(image=image_paper1)
        elif choice_computer=="scissor":
            label_computer.configure(image=image_scissor1)


        if a=="rock":
            label_player.configure(image=image_rock1)
        elif a=="paper":
            label_player.configure(image=image_paper1)
        else:
            label_player.configure(image=image_scissor1)

        winner_check(a,choice_computer)
        


    





    #label for user and computer
    label_player=Label(window,image=image_scissor1)
    label_computer=Label(window,image=image_scissor2)
    label_computer.grid(row=1,column=0)
    label_player.grid(row=1,column=4)

    #message of you winning and losing
    final_message=Label(window,font=("arial",40,"bold"),
                        bg="red", fg="white")
    final_message.grid(row=3, column=0, columnspan=5)


    #we might need to change dimensions of the buttons
    button_rock=Button(window,width=16, height=3, text="rock",font=("arial",20,"bold"), background="yellow",
                    fg="black",command=lambda:choice_update("rock")).grid(row=2,column=1)
    button_paper=Button(window,width=16, height=3, text="paper",font=("arial",20,"bold"), background="yellow",
                        fg="black",command=lambda:choice_update("paper")).grid(row=2,column=2)
    button_scissor=Button(window,width=16, height=3, text="scissor",font=("arial",20,"bold"), background="yellow",
                    fg="black",command=lambda:choice_update("scissor")).grid(row=2,column=3)



    window.mainloop()


