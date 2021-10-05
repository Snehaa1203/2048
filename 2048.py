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
        for i in range(4):   # moving rightwards column+1, row same
            fill_position=0
            for j in range(4):
                if self.matrix[i][j]!=0:
                    new_matrix[i][fill_position]=self.matrix[i][j]
                    fill_position+=1
        self.matrix=new_matrix   # create a new matrix evrytime you change pos
   
    def combine(self):
        for i in range(4):
            for j in range(3): #combining 2+2
                if self.matrix[i][j]!=0 and self.matrix[i][j]==self.matrix[i][j+1]:
                    self.matrix[i][j]*=2
                    self.matrix[i][j+1]=0 #comibing in one ans setting other to zero
                    self.score+=self.matrix[i][j]  #increasing score

    def reverse(self):
         new_matrix= [] 
         for i in range(4):
             new_matrix.append([])
             for j in range(4):
                 new_matrix[i].append(self.matrix[i][3-j])

         self.matrix=new_matrix
    

    def transpose(self):
        new_matrix=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j]=self.matrix[j][i]

        self.matrix=new_matrix

    def add_new_tile(self):
        row=random.randint(0,3)
        col=random.randint(0.3)
        while(self.matrix[row][col]!=0):
            row=random.randint(0,3)
            col=random.randint(0,3)
        self.matrix[row][col]=random.choice([2,4])

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value=self.matrix[i][j]
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
                       text=str(cell_value)
                    )
        self.score_label.configure(text=self.score)



    #arrow press functions

    