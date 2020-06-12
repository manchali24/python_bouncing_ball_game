from tkinter import *
import time


class Ball:
    def __init__(self, canvas, paddle, color, score):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.hit_bottom = False
        self.hit = 0
        self.id = canvas.create_oval(5, 5, 25, 25, fill=color) # create a ball # radius , width color
        self.canvas.move(self.id, 240, 100) # initial position of ball
        starts = [-3, -2, -1, 1, 2, 3]  # x, y, z velocity of the ball(speed)
        self.x =starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <=paddle_pos[3]:
                return  True
        return False

    def calculate_score(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                canvas.bell()
                self.hit += 1
                self.score.configure(text="Score: " + str(self.hit))
                self.canvas.delete(paddle.id)
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) #position of the ball
        starts = [-3, -2, -1, 1, 2, 3]
        if self.calculate_score(pos):
            self.y = starts[0]
        if pos[1] <=0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom= True
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <=0:
            self.x=2
        if pos[2] >= self.canvas_width:
            self.x= -2

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 20, fill=color) # paddle is created
        self.canvas.move(self.id, 200, 400) # initial position of paddle is set
        self.x = 0
        self.pausec = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left) # this used to move the paddle left (left arrow key)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right) # this used to move the paddle right (right arrow key)
        self.canvas.bind_all('<KeyPress-space>',self.pauser) # this used to pause the game (space key)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0:
            self.x=0
        elif pos[2] >= self.canvas_width:
            self.x=0

	# move left
    def turn_left(self, event):
        self.x= -2
	# move right
    def turn_right(self, event):
        self.x = 2

	# Pause
    def pauser(self, event):
        self.pausec += 1
        if self.pausec == 2:
            self.pausec = 0

root = Tk()
root.title("Bouncing Ball")
root.resizable(0, 0)
#root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)
root.geometry("480x550")
score = Label(height=40, width=80, text="Score: 00  (Target = 10)", font="Consolas 14 bold")
score.pack(side="left")
root.update()
paddle = Paddle(canvas, 'yellow')
ball = Ball(canvas, paddle,'red',score)

playing = False

def startGame(event):
    global playing
    if playing is False:
        playing = True
        score.configure(text="Score: 00")
        canvas.delete("all")
        paddle = Paddle(canvas, "yellow")
        ball = Ball(canvas, paddle,'red', score)
        root.update_idletasks()
        root.update()

        time.sleep(1)

        while 1:
            if paddle.pausec != 1:
                try:
                    canvas.delete(m)
                    del m
                except:
                    pass
                if not ball.hit_bottom:
                    ball.draw()
                    paddle.draw()
                    root.update_idletasks()
                    root.update()
                    time.sleep(0.01)
                    if ball.hit== 10 :
                        canvas.create_text(250, 250, text="YOU WIN THE GAME!!", fill="yellow", font="Consolas 24")
                        canvas.create_text(250, 280, text="Stage 2 Starts", fill="red", font="Consolas 24")
                        root.update_idletasks()
                        root.update()
                        time.sleep(3)
                        root.destroy()
                        playing = False
                        break

                else:
                    canvas.create_text(250, 250, text="YOU LOSS!!", fill="yellow", font="Consolas 24 ")
                    canvas.create_text(250, 285, text="GAME OVER", fill="red", font="Consolas 24 ")
                    root.update_idletasks()
                    root.update()
                    playing = False
                    canvas.create_text(250, 320, text="Press Enter to start the Game", fill="red", font="Consolas 18")
                    break

            else:
                try:
                    if m == None: pass
                except:
                    m = canvas.create_text(250, 250, text="PAUSE", fill="green", font="Consolas 24 ")
                root.update_idletasks()
                root.update()


root.bind_all("<Return>", startGame)
canvas.create_text(250, 250, text="Stage 1", fill="red", font="Consolas 18")
canvas.create_text(250, 280, text="Press Enter to start the Game", fill="red", font="Consolas 18")
j = canvas.find_all()
root.mainloop()

