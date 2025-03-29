from tkinter import *
import os
import ctypes as ct

#paths
dir_path = os.getcwd()
assets_path = os.path.join(dir_path, "Assets")

#colors
background_color = "#262626"

#mathematical operation and num list for comparisons
mathematical_operators = ["%", "x", "-", "+", "÷"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
entry_nums = []

# taskbar icon
myappid = 'WeatherApp' 
ct.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

############################# FUNCTIONS #############################

# dark title bar function
def dark_title_bar():
    if os.name == 'nt':
        app.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(app.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                             ct.sizeof(value))


############################# CLASSES #############################
class calculator():
    def __init__(self, app, frame):
        #self adjustments
        self.frame = frame
        self.app = app
        #vars of app size
        self.current_width = IntVar()
        self.current_height = IntVar()
        #for adding dot
        self.mathematical_operator_before_bool = True
        #sizes_reset
        self.size_10 = 0
        self.size_15 = 0
        self.size_24 = 0
        self.size_30 = 0
        #create widgets func
        self.create_widgets()
        #resize func
        self.app.bind("<Configure>", self.resize)

    def create_widgets(self):
        self.entry_frame = Frame(self.frame)
        self.entry = Entry(self.frame, justify="right", border=5, font=("Arial", 24, "bold"), state="normal")
        self.entry_frame.grid_columnconfigure(0, weight=1)
        self.entry.insert(0, "0")
        self.entry.grid(row=0, column=0)
        self.entry_frame.grid(row=0, column=0)
        #button frame
        self.button_frame = Frame(self.frame, background=background_color)
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)
        self.button_frame.grid(row=1, column=0)
        #buttons first row
        self.percent_button = Button(self.button_frame, text=" % ", font=("Arial", 30, "bold"))
        self.percent_button.grid(row=0, column=0, padx = 15, pady= 10)
        self.c_button = Button(self.button_frame, text=" C ", font=("Arial", 30, "bold"))
        self.c_button.grid(row=0, column=1, padx = 15, pady= 10)
        self.delete_last_button = Button(self.button_frame, text="⌫", font=("Arial", 30, "bold"))
        self.delete_last_button.grid(row=0, column=2, padx = 15, pady= 10)
        self.div_button = Button(self.button_frame, text=" ÷ ", font=("Arial", 30, "bold"))
        self.div_button.grid(row=0, column=3, padx = 15, pady= 10)
        #buttons second row
        self.num_7_button = Button(self.button_frame, text=" 7 ", font=("Arial", 30, "bold"))
        self.num_7_button.grid(row=1, column=0, padx = 15, pady= 10)
        self.num_8_button = Button(self.button_frame, text=" 8 ", font=("Arial", 30, "bold"))
        self.num_8_button.grid(row=1, column=1, padx = 15, pady= 10)
        self.num_9_button = Button(self.button_frame, text=" 9  ", font=("Arial", 30, "bold"))
        self.num_9_button.grid(row=1, column=2, padx = 15, pady= 10)
        self.mult_button = Button(self.button_frame, text=" x ", font=("Arial", 30, "bold"))
        self.mult_button.grid(row=1, column=3, padx = 15, pady= 10)
        #buttons third row
        self.num_4_button = Button(self.button_frame, text=" 4 ", font=("Arial", 30, "bold"))
        self.num_4_button.grid(row=2, column=0, padx = 15, pady= 10)
        self.num_5_button = Button(self.button_frame, text=" 5 ", font=("Arial", 30, "bold"))
        self.num_5_button.grid(row=2, column=1, padx = 15, pady= 10)
        self.num_6_button = Button(self.button_frame, text=" 6  ", font=("Arial", 30, "bold"))
        self.num_6_button.grid(row=2, column=2, padx = 15, pady= 10)
        self.sub_button = Button(self.button_frame, text=" - ", font=("Arial", 30, "bold"))
        self.sub_button.grid(row=2, column=3, padx = 15, pady= 10)
        #buttons fourth row
        self.num_1_button = Button(self.button_frame, text=" 1 ", font=("Arial", 30, "bold"))
        self.num_1_button.grid(row=3, column=0, padx = 15, pady= 10)
        self.num_2_button = Button(self.button_frame, text=" 2 ", font=("Arial", 30, "bold"))
        self.num_2_button.grid(row=3, column=1, padx = 15, pady= 10)
        self.num_3_button = Button(self.button_frame, text=" 3  ", font=("Arial", 30, "bold"))
        self.num_3_button.grid(row=3, column=2, padx = 15, pady= 10)
        self.add_button = Button(self.button_frame, text=" + ", font=("Arial", 30, "bold"))
        self.add_button.grid(row=3, column=3, padx = 15, pady= 10)
        #buttons fifth row
        self.num_0_button = Button(self.button_frame, text="     0     ", font=("Arial", 30, "bold"))
        self.num_0_button.grid(row=4, column=0, columnspan=2, padx = 15, pady= 10)
        self.dot_button = Button(self.button_frame, text=" . ", font=("Arial", 30, "bold"))
        self.dot_button.grid(row=4, column=2, padx = 15, pady= 10)
        self.equal_button  = Button(self.button_frame, text="=", font=("Arial", 30, "bold"))
        self.equal_button.grid(row=4, column=3)
        #button commands
        self.num_0_button.config(command=self.add_0)
        self.num_1_button.config(command=self.add_1)
        self.num_2_button.config(command=self.add_2)
        self.num_3_button.config(command=self.add_3)
        self.num_4_button.config(command=self.add_4)
        self.num_5_button.config(command=self.add_5)
        self.num_6_button.config(command=self.add_6)
        self.num_7_button.config(command=self.add_7)
        self.num_8_button.config(command=self.add_8)
        self.num_9_button.config(command=self.add_9)
        self.c_button.config(command=self.erase)
        self.delete_last_button.config(command=self.delete_last)
        self.percent_button.config(command=self.add_percent)
        self.dot_button.config(command=self.add_dot)
        self.add_button.config(command=self.add_plus)
        self.sub_button.config(command=self.add_sub)
        self.mult_button.config(command=self.add_mult)
        self.div_button.config(command=self.add_div)
        self.equal_button.config(command=self.format_data)
    
    ########## COMMAND FUNCTIONS ##########
    def add_0(self):
        if(self.entry.get() == "0"):
            pass
        else:
            if(self.entry.get() in mathematical_operators):
                self.entry.delete(0,END)
                self.entry.insert(END, "0")
            else:    
                self.entry.insert(END, "0")
    
    def add_1(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "1")

    def add_2(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "2")

    def add_3(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "3")

    def add_4(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "4")

    def add_5(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "5")

    def add_6(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "6")

    def add_7(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "7")

    def add_8(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "8")

    def add_9(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            self.entry.delete(0, END)
        self.entry.insert(END, "9")

    def erase(self):
        if(self.entry.get() == "0"):
            pass
        else:
            self.entry.delete(0, END)
            self.entry.insert(END, "0")
            entry_nums.clear()
            self.mathematical_operator_before_bool = True

    def delete_last(self):
        if(self.entry.get() == "0" or self.entry.get() in mathematical_operators):
            pass
        else:
            self.entry.delete(len(self.entry.get()) - 1, END)
            if(self.entry.get() == ""):
                self.entry.insert(END, "0")

    def add_percent(self):
        if(self.entry.get() == "0"):
            pass
        elif("%" in entry_nums):
            pass
        else:
            entry_nums.append(self.entry.get())
            self.entry.delete(0, END)
            entry_nums.append("%")
            self.entry.insert(END, "%")
            self.mathematical_operator_before_bool = True

    def add_dot(self):
        if(self.mathematical_operator_before_bool == True):    
            data = self.entry.get()
            if(data[len(data) - 1] in nums):
                self.entry.insert(END, ".")
                self.mathematical_operator_before_bool = False
            else:
                pass

    def add_plus(self):
        data = self.entry.get()
        if(data[len(data) - 1] in nums):
            entry_nums.append(self.entry.get())
            self.entry.delete(0, END)
            entry_nums.append("+")
            self.entry.insert(END, "+")
            self.mathematical_operator_before_bool
        else:
            pass

    def add_sub(self):
        data = self.entry.get()
        if(data[len(data) - 1] in nums):
            entry_nums.append(self.entry.get())
            self.entry.delete(0, END)
            entry_nums.append("-")
            self.entry.insert(END, "-")
            self.mathematical_operator_before_bool
        else:
            pass

    def add_mult(self):
        data = self.entry.get()
        if(data[len(data) - 1] in nums):
            entry_nums.append(self.entry.get())
            self.entry.delete(0, END)
            entry_nums.append("x")
            self.entry.insert(END, "x")
            self.mathematical_operator_before_bool
        else:
            pass

    def add_div(self):
        data = self.entry.get()
        if(data[len(data) - 1] in nums):
            entry_nums.append(self.entry.get())
            self.entry.delete(0, END)
            entry_nums.append("÷")
            self.entry.insert(END, "÷")
            self.mathematical_operator_before_bool
        else:
            pass

    #getting and formating data into a list
    def format_data(self):
        #get if the last is an operator and if yes put 0 to not get error
        if(self.entry.get() not in mathematical_operators):
            entry_nums.append(self.entry.get())
        else:
            pass
        print(entry_nums)
        self.new_nums = []
        for count,data in enumerate(entry_nums):
            if(entry_nums[count] not in mathematical_operators):    
                if("." in entry_nums[count]):
                    try:
                        self.new_nums.append(float(data))
                    except Exception as e:
                        print(e)
                else:
                    try:
                        self.new_nums.append(int(data))
                    except Exception as e:
                        print(e)        
            else:
                self.new_nums.append(entry_nums[count])
        print(self.new_nums)
        #go to process data if content is at least 3
        if(len(self.new_nums) >= 3):
            self.process_data()
        else:
            self.entry.delete(0,END)
            self.entry.insert(0, self.new_nums[0])
            entry_nums.clear()
            self.new_nums.clear()

    #processing the data
    def process_data(self):
        #1st div 2nd mult 3rd add 4th sub 5th perc
        data_list = self.new_nums
        div_count = 0
        mult_count = 0
        add_count = 0
        sub_count = 0
        
        #get times of div operators
        if("÷" in data_list):
            for count, data in enumerate(data_list):
                if(data == "÷"):
                    div_count += 1
                else:
                    pass
            #do the math
            for times in range(0, div_count):
                for count, data in enumerate(data_list):
                    if(data == "÷"):
                        a_num = data_list[count - 1]
                        b_num = data_list[count + 1]
                        for val in range(0, 3):
                            if(count - 1 > 0):
                                data_list.pop(count - 1)
                            else:
                                data_list.pop(count - 1)
                        data_list.insert(count - 1, (a_num / b_num))
        
        #get times of mult operators
        if("x" in data_list):
            for count, data in enumerate(data_list):
                if(data == "x"):
                    mult_count += 1
                else:
                    pass
            #do the math
            for times in range(0, mult_count):
                for count, data in enumerate(data_list):
                    if(data == "x"):
                        a_num = data_list[count - 1]
                        b_num = data_list[count + 1]
                        for val in range(0, 3):
                            if(count - 1 > 0):
                                data_list.pop(count - 1)
                            else:
                                data_list.pop(count - 1)
                        data_list.insert(count - 1, (a_num * b_num))           

        #get times of add operators
        if("+" in data_list):
            for count, data in enumerate(data_list):
                if(data == "+"):
                    add_count += 1
                else:
                    pass
            #do the math
            for times in range(0, add_count):
                for count, data in enumerate(data_list):
                    if(data == "+"):
                        a_num = data_list[count - 1]
                        b_num = data_list[count + 1]
                        for val in range(0, 3):
                            if(count - 1 > 0):
                                data_list.pop(count - 1)
                            else:
                                data_list.pop(count - 1)
                        data_list.insert(count - 1, (a_num + b_num))    

        #get times of sub operators
        if("-" in data_list):
            for count, data in enumerate(data_list):
                if(data == "-"):
                    sub_count += 1
                else:
                    pass
            #do the math
            for times in range(0, sub_count):
                for count, data in enumerate(data_list):
                    if(data == "-"):
                        a_num = data_list[count - 1]
                        b_num = data_list[count + 1]
                        for val in range(0, 3):
                            if(count - 1 > 0):
                                data_list.pop(count - 1)
                            else:
                                data_list.pop(count - 1)
                        data_list.insert(count - 1, (a_num - b_num))       

        #do the percentage happens only one time at the end so not complex
        if("%" in data_list):
            a_num = data_list[0]
            b_num = data_list[2]
            data_list.clear()
            data_list.append((a_num / b_num) * 100)

        print(data_list)
        self.entry.delete(0,END)
        self.entry.insert(0, data_list[0])
        entry_nums.clear()
        self.new_nums.clear()
        data_list.clear()

    def configure_widgets(self):
        #getting window size percentage
        window_percentage = (((self.current_width.get() / start_width) + (self.current_height.get() / start_height))/2)
        size_10 = int(10 * window_percentage)
        size_15 = int(15 * window_percentage)
        size_24 = int(24 * window_percentage)
        size_30 = int(30 * window_percentage)
        #resize widgets
        if (size_10 != self.size_10):
            self.percent_button.grid_configure(pady=size_10)
            self.c_button.grid_configure(pady=size_10)
            self.delete_last_button.grid_configure(pady=size_10)
            self.div_button.grid_configure(pady=size_10)
            self.num_7_button.grid_configure(pady=size_10)
            self.num_8_button.grid_configure(pady=size_10)
            self.num_9_button.grid_configure(pady=size_10)
            self.mult_button.grid_configure(pady=size_10)
            self.num_4_button.grid_configure(pady=size_10)
            self.num_5_button.grid_configure(pady=size_10)
            self.num_6_button.grid_configure(pady=size_10)
            self.sub_button.grid_configure(pady=size_10)
            self.num_1_button.grid_configure(pady=size_10)
            self.num_2_button.grid_configure(pady=size_10)
            self.num_3_button.grid_configure(pady=size_10)
            self.add_button.grid_configure(pady=size_10)
            self.num_0_button.grid_configure(pady=size_10)
            self.dot_button.grid_configure(pady=size_10)
            self.equal_button.grid_configure(pady=size_10)
            self.size_10 = size_10

        if (size_15 != self.size_15):
            self.percent_button.grid_configure(padx=size_15)
            self.c_button.grid_configure(padx=size_15)
            self.delete_last_button.grid_configure(padx=size_15)
            self.div_button.grid_configure(padx=size_15)
            self.num_7_button.grid_configure(padx=size_15)
            self.num_8_button.grid_configure(padx=size_15)
            self.num_9_button.grid_configure(padx=size_15)
            self.mult_button.grid_configure(padx=size_15)
            self.num_4_button.grid_configure(padx=size_15)
            self.num_5_button.grid_configure(padx=size_15)
            self.num_6_button.grid_configure(padx=size_15)
            self.sub_button.grid_configure(padx=size_15)
            self.num_1_button.grid_configure(padx=size_15)
            self.num_2_button.grid_configure(padx=size_15)
            self.num_3_button.grid_configure(padx=size_15)
            self.add_button.grid_configure(padx=size_15)
            self.num_0_button.grid_configure(padx=size_15)
            self.dot_button.grid_configure(padx=size_15)
            self.equal_button.grid_configure(padx=size_15)
            self.size_15 = size_15

        if (size_24 != self.size_24):
            self.entry.config(font = ("Arial", size_24, "bold"))
            self.size_24 = size_24

        if (size_30 != self.size_30):
            self.percent_button.config(font = ("Arial", size_30, "bold"))
            self.c_button.config(font = ("Arial", size_30, "bold"))
            self.delete_last_button.config(font = ("Arial", size_30, "bold"))
            self.div_button.config(font = ("Arial", size_30, "bold"))
            self.num_7_button.config(font = ("Arial", size_30, "bold"))
            self.num_8_button.config(font = ("Arial", size_30, "bold"))
            self.num_9_button.config(font = ("Arial", size_30, "bold"))
            self.mult_button.config(font = ("Arial", size_30, "bold"))
            self.num_4_button.config(font = ("Arial", size_30, "bold"))
            self.num_5_button.config(font = ("Arial", size_30, "bold"))
            self.num_6_button.config(font = ("Arial", size_30, "bold"))
            self.sub_button.config(font = ("Arial", size_30, "bold"))
            self.num_1_button.config(font = ("Arial", size_30, "bold"))
            self.num_2_button.config(font = ("Arial", size_30, "bold"))
            self.num_3_button.config(font = ("Arial", size_30, "bold"))
            self.add_button.config(font = ("Arial", size_30, "bold"))
            self.num_0_button.config(font = ("Arial", size_30, "bold"))
            self.dot_button.config(font = ("Arial", size_30, "bold"))
            self.equal_button.config(font = ("Arial", size_30, "bold"))
            self.size_30 = size_30
        
    #resize function
    def resize(self, event):
        self.app.config(width=event.width, height=event.height)
        self.current_width.set(str(self.app.winfo_width()))
        self.current_height.set(str(self.app.winfo_height()))
        self.configure_widgets()

############################# APP #############################
app = Tk()
app.title("Calculator")
app.geometry("372x550")
app.maxsize(width = 600, height= 935)
app.minsize(width=372, height=550)
app.iconphoto(False, PhotoImage(file=os.path.join(assets_path, "calculator_icon.png")))
frame = Frame(app, background=background_color)
#make title bar black
dark_title_bar()
start_width = app.winfo_width()
start_height = app.winfo_height()
print(f"Start size: {start_width}x{start_height}\nMax Size is 1.7 more: 600x935")
frame.grid_columnconfigure(0, weight=1)
#call calculator class
calculator(app, frame)

#display
frame.pack(expand=True, fill="both")
app.mainloop()