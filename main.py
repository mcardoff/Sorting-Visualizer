import random
from tkinter import *
from tkinter import ttk
from color import *
from enum import Enum
from algos.bubbleSort import bubble_sort
from algos.quickSort import quick_sort

class Alg(Enum):

    BUBBLE = 1
    QUICK = 2

    def __str__(self):
        if self.value == 1:
            return "Bubble Sort"
        elif self.value == 2:
            return "Quick Sort"
        else:
            return "Invalid?"

def drawArr(data, colorArr):
    global canvas, window
    canvas.delete('all')
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    norm_data = [i / max(data) for i in data]

    for i, height in enumerate(norm_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArr[i])

    window.update_idletasks()

def reshuffle():
    global data, canvas, window

    data = [random.randint(1,150) for _ in range(0,100)]

    drawArr(data, [RED for _ in range(len(data))])
        
def set_speed():
    global speed_menu
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.01
    
def sort():
    global data, algo_menu
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawArr, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, drawArr, timeTick)
        

def main():
    global canvas, window, speed_menu, algo_menu

    alg_name = ""
    speed = ""

    algs = [Alg.BUBBLE, Alg.QUICK]
    speeds = ['Slow', 'Medium', 'Fast']
    
    window = Tk()
    window.title("Sorting Algorithms Visualization")
    window.maxsize(1000, 700)
    window.config(bg = WHITE)
    
    ### UI Here ###

    # initialize UI object
    UI_frame = Frame(window, width=900, height=300, bg=WHITE)
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    counter = 0

    # Dropdown for choosing sorting algo
    sorting_dropdown = Label(UI_frame, text="Algo: ", bg=WHITE)
    sorting_dropdown.grid(row=counter, column=0, padx=10, pady=5, sticky=W)
    algo_menu = ttk.Combobox(UI_frame, textvariable=alg_name, values=algs)
    algo_menu.grid(row=counter, column=1, padx=5, pady=5)
    algo_menu.current(0)

    counter += 1

    # Dropdown for choosing speed
    speed_dropdown = Label(UI_frame, text="Speed: ", bg=WHITE)
    speed_dropdown.grid(row=counter, column=0, padx=10, pady=5, sticky=W)
    speed_menu = ttk.Combobox(UI_frame, textvariable=speed, values=speeds)
    speed_menu.grid(row=counter, column=1, padx=5, pady=5)
    speed_menu.current(0)

    counter += 1

    # Button for performing sort
    sort_button = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
    sort_button.grid(row=counter, column=0, padx=5, pady=5)

    # Button for Reshuffling
    shuffle_button = Button(UI_frame, text="Reshuffle",
                            command=reshuffle, bg=LIGHT_GRAY)
    shuffle_button.grid(row=counter, column=1, padx=5, pady=5)

    counter += 1
    
    # Canvas on which to Draw Array
    canvas = Canvas(window, width=800, height=400, bg=WHITE)
    canvas.grid(row=counter, column=0, padx=10, pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()
