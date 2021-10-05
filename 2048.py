import tkinter as tk
import colors as c
import random
#2 steps create,fix
class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)  #frame made
        self.grid()              #grid made ,created
        self.master.title("2048") #master title (heading)

        self.main_grid=tk.Frame(
            self,bg=c.GRID_COLOR,bd=3,width=600,height=600  
        )    #outline gui, border,bg color

        self.main_grid.grid(pady=(100,0)) #fixing pos of outline grid
        self.make_GUI()
        self.start_game()
 
        self.master.bind("<Left>",self.left)    # linking arrow keys to functions.
        self.master.bind("<Right>",self.right)
        self.master.bind("<Up>",self.up)
        self.master.bind("<Down>",self.down)

        self.mainloop()  #keeps the window running

    def make_GUI(self):
        self.cells=[]
        for i in range(4): #4*4 grid
            row=[]  #initialising empty row
            for j in range(4): #column in each row
                cell_frame=tk.Frame(
                self.main_grid,    #creating cell frame inside main grid
                bg=c.EMPTY_CELL_COLOR,
                height=150,
                width=150
                )
                cell_frame.grid(row=i,column=j,padx=5,pady=5) #fix pos of cell frame
                cell_number=tk.Label(self.main_grid,bg=c.EMPTY_CELL_COLOR) #text label for num on cell
                cell_number.grid(row=i,column=j)  #fix pos of cell num
                cell_data={"frame":cell_frame,"number":cell_number} 
                row.append(cell_data) #append rows in row.
            self.cells.append(row)  
             #   appending row in cell
        #score header  
        score_frame=tk.Frame(self) 
        score_frame.place(relx=0.5,y=45,anchor="center") #placing score_frame
        tk.Label(   
           score_frame,text="Score",
           font= c.SCORE_LABEL_FONT
           ).grid(row=0)
        self.score_label=tk.Label(score_frame,text="0",font= c.SCORE_FONT)
        self.score_label.grid(row=1)  #default score =0
    

    def start_game(self): 
         self.matrix=[[0] *4 for _ in range(4)] #created matrix of zeros
        
         row=random.randint(0,3)   #placing starting random 2's
         col=random.randint(0,3)
         self.matrix[row][col]=2
         self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2]) #cells is a dict 
          #we first configure the frame attribute acc to size of 2
         self.cells[row][col]["number"].configure(
             bg=c.CELL_COLORS[2],
             fg=c.CELL_NUMBER_COLORS[2],
             font=c.CELL_NUMBER_FONTS[2],
             text="2"
             )
         while(self.matrix[row][col]!=0):  #finding em[ty place in matrix for next 2]
            row=random.randint(0,3)   #placing starting random 2's
            col=random.randint(0,3)
         self.matrix[row][col]=2
         self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2]) #cells is a dict 
                #we first configure the frame attribute acc to size of 2
         self.cells[row][col]["number"].configure(
                bg=c.CELL_COLORS[2],
                fg=c.CELL_NUMBER_COLORS[2],
                font=c.CELL_NUMBER_FONTS[2],
                text="2"
             )

         self.score=0

    #matrix manipulation

    def stack(self):
        new_matrix=[[0]*4 for _ in range(4)]
        for i in range(4):   # moving all non zero elements to left side of game elemenating gaps
            fill_position=0   # contains number of cells holding non zero value
            for j in range(4):
                if self.matrix[i][j]!=0:
                    new_matrix[i][fill_position]=self.matrix[i][j]
                    fill_position+=1
        self.matrix=new_matrix   # create a new matrix evrytime you change pos
   
    def combine(self):  # merging all same value horizontally and merges them to left side
        for i in range(4):
            for j in range(3): #combining 2+2
                if self.matrix[i][j]!=0 and self.matrix[i][j]==self.matrix[i][j+1]:
                    self.matrix[i][j]*=2
                    self.matrix[i][j+1]=0 #comibing in one ans setting other to zero
                    self.score+=self.matrix[i][j]  #increasing score

    def reverse(self):
         new_matrix= [] 
         for i in range(4):   # this func basically is reverse of left, for the right arrow key
             new_matrix.append([])
             for j in range(4):
                 new_matrix[i].append(self.matrix[i][3-j]) # reversing the order of the values

         self.matrix=new_matrix
    

    def transpose(self):
        new_matrix=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j]=self.matrix[j][i] # flips over diagnol

        self.matrix=new_matrix

    def add_new_tile(self):  # new tile after every move
        row=random.randint(0,3)
        col=random.randint(0,3)
        while(self.matrix[row][col]!=0):
            row=random.randint(0,3)
            col=random.randint(0,3)
        self.matrix[row][col]=random.choice([2,4])  # a new tile is added after every move and thats either 2 or 4.


    def update_GUI(self):   # update gui to match the new matrix
        for i in range(4):
            for j in range(4):
                cell_value=self.matrix[i][j]  # if cell value is 0 i . e empty 
                if cell_value==0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(
                        bg=c.EMPTY_CELL_COLOR,
                        text=""
                        )
                else:
                    self.cells[i][j]["frame"].configure(bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                       bg=c.CELL_COLORS[cell_value],
                       fg=c.CELL_NUMBER_COLORS[cell_value],
                       font=c.CELL_NUMBER_FONTS[cell_value],
                       text=str(cell_value)  # else set up the cell frame accordingly
                    )
        self.score_label.configure(text=self.score)
        self.update_idletasks()




    #arrow press functions

    def left(self,event):
        self.stack()     # left is the most firect func, accumulate all non zero values to left side, combine them again accumulate and last 3 func are called in evry move.
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def right (self,event):
         self.reverse()   # to reverse the effect of left
         self.stack()     #accumulate
         self.combine()   # combine ,merge same values
         self.stack()     # again accumulate
         self.reverse()   # rev again to get the original matrix
         self.add_new_tile()
         self.update_GUI()
         self.game_over()

    def up (self,event):
        self.transpose()  # to have the up affect using left, flip across the diaognal
        self.stack()      #accumulate
        self.combine()    #merge
        self.stack()      #again accumulate
        self.transpose()   # again to get the original back
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def down(self,event):
        self.transpose()  # down with rev and then same as left func above
        self.reverse()    # basically for up and down we need to have transpose 
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    # checking if any moves are possible either horizontal or vertical
    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j]==self.matrix[i][j+1]:
                    return True
        return False


    def vertical_move_exists(self):
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j]==self.matrix[i+1][j]:
                    return True
        return False

   
    def game_over(self):   # if 2048 is made, game won
        if any (2048 in row for row in self.matrix):
            game_over_frame=tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
            tk.Label(
                game_over_frame,
                text="YOU WIN",
                bg=c.WINNER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font=c.GAME_OVER_FONT
            ).pack()
        elif not any (0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame=tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
            tk.Label(
                game_over_frame,
                text="GAME OVER",
                bg=c.LOSER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font=c.GAME_OVER_FONT
            ).pack()

def main():
  Game()

if __name__ == "__main__":
    main()