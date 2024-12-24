import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from colors import *
from golomb_compression_decompression import golomb_decode, golomb_encode
import re
import ast
from huffman import compress_huffman, decompress_huffman
from arithmaticComperssion import getCumulativeProbs, arithmetic_encode


#------- show/hidden sidebar ----------#
# def showSideBar():
#     if not(sidebar.winfo_viewable()):
#         sidebar.place(x= 0)
#         showsidebar_button.config(bg= sidebar.cget("bg"))
#         print(sidebar.cget("bg"))
#     else:
#         sidebar.place_forget()
#         showsidebar_button.config(bg= mainWindow.cget("bg"))
#         print(mainWindow.cget("bg"))
 
def openAlgorithmFrame():
    if not(algorithmFrame.winfo_viewable()):
        algorithmFrame.place(x= 240)
        aboutFrame.place_forget()
        homeFrame.place_forget()
        print(mainWindow.cget("width"))

def openAboutFrame():
    if not(aboutFrame.winfo_viewable()):
        aboutFrame.place(x= 240)
        algorithmFrame.place_forget()
        homeFrame.pack_forget()
        print(mainWindow.cget("width"))

def openHomeFrame():
    if not(homeFrame.winfo_viewable()):
        homeFrame.place(x= 240)
        algorithmFrame.place_forget()
        aboutFrame.place_forget()
        print(mainWindow.cget("width"))

def size():
    print(huffmanButton.cget("width"))
    print(huffmanButton.cget("height"))

def selectFile():
    filePath = filedialog.askopenfilename(
        title="Select file",
        filetypes=[("Compress files", "*.na"), ("Text files", "*.txt"), ("All files", "*.*")])
    
    if filePath:
        print(f"File opened {filePath}")
        huffmanPathEntry.delete(0, len(huffmanPathEntry.get()))
        huffmanPathEntry.insert(0, f"{filePath}")
    else:
        print("Did not choose file")

def selectFileGolomb():
    filePath = filedialog.askopenfilename(
        title="Select file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if filePath:
        print(f"File opened {filePath}")
        pathEntryGolomb.delete(0, len(pathEntryGolomb.get()))
        pathEntryGolomb.insert(0, f"{filePath}")
    else:
        print("Did not choose file")

def selectFileArith():
    filePath = filedialog.askopenfilename(
        title="Select file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if filePath:
        print(f"File opened {filePath}")
        pathEntryArith.delete(0, len(pathEntryArith.get()))
        pathEntryArith.insert(0, f"{filePath}")
    else:
        print("Did not choose file")

def activateFirstAlgorithm(event):
    huffmanButton.config(image= activeFirstAlgorithmPhoto)

def inactivateFirstAlgorithm(event):
    huffmanButton.config(image= firstAlgorithmPhoto)

def activateGolomb(event):
    golombButton.config(image= activeFirstAlgorithmPhoto)

def inactivateGolomb(event):
    golombButton.config(image= firstAlgorithmPhoto)

def activateArith(event):
    arithButton.config(image= activeFirstAlgorithmPhoto)

def inactivateArith(event):
    arithButton.config(image= firstAlgorithmPhoto)

def createNote(image, notes):
    button = tk.Button(
        frame,
        image= image,
        text= notes,
        borderwidth=0,
        bg= aboutFrameColor,
        highlightthickness= 0,
        activebackground= aboutFrameColor,
        compound= "center",
        font= ("Arial",),
        foreground= "white",
        activeforeground= sidebarButtonsActivateColorFG )

    return button

def createNote(image):
    button = tk.Button(
        frame,
        image= image,
        borderwidth=0,
        bg= aboutFrameColor,
        highlightthickness= 0,
        activebackground= aboutFrameColor,

        compound= "center",
        font= ("Arial", ),
        foreground= "white",
        activeforeground= sidebarButtonsActivateColorFG )
    
    return button

def createButton(image, frame, text):
    button = tk.Button(frame,
                       image= image,
                       borderwidth= 0,
                       highlightthickness= 0,
                       activebackground= frame.cget("bg"),
                       activeforeground= sidebarButtonsActivateColorFG,
                       background= frame.cget("bg"),
                       compound= "center",
                       text= text,
                       font= ("Arial",)
                       )
    
    return button

#--------huffman----------#
def openHuffmanTab():
    noteBook.add(huffmanTab, text= "Huffman")
    noteBook.pack(expand= True, fill= "both")


def encodeHuffman():
    path = huffmanPathEntry.get()
    f = open(path, "r")
    try:
        lines = f.readlines()
    except UnicodeDecodeError as e:
        huffmanPathEntry.delete(0, tk.END)
        pop = tk.Tk()
        pop.title("Arithmatic Code")
        pop.geometry("360x144")
        outPut = tk.Entry(master= pop,)
        outPut.delete(0, len(outPut.get()))
        outPut.insert(0, "Enter a valid file you ****")
        outPut.config(state= "readonly")
        outPut.pack(expand= True)
        pop.mainloop()
        return
    
    lines = "".join(lines[0:])
    code = compress_huffman(lines)

    file = filedialog.asksaveasfile(
        mode="w", 
        defaultextension=".txt", 
        filetypes=[("Compressed files", "*.na"), ("All files", "*.*")]
    )
    if file:  
        file.write(f"{code['encoded_string']}\n{code['huffman_codes']}")
        file.close()

    huffmanPathEntry.delete(0, len(huffmanPathEntry.get()))
def decodeHuffman():
    path = huffmanPathEntry.get()
    f = open(path, "r")
    try:
        lines = f.readlines()
    except UnicodeDecodeError as e:
        huffmanPathEntry.delete(0, tk.END)
        pop = tk.Tk()
        pop.title("Arithmatic Code")
        pop.geometry("360x144")
        outPut = tk.Entry(master= pop,)
        outPut.delete(0, len(outPut.get()))
        outPut.insert(0, "Enter a valid file you ****")
        outPut.config(state= "readonly")
        outPut.pack(expand= True)
        pop.mainloop()
        return
    
    lines = "".join(lines[0:])

    pattern = r'\{[^}]+\}'
    huffman_codes = re.search(pattern, lines).group()
    encoded_string = re.sub(pattern, '', lines)
    huffman_codes = ast.literal_eval(huffman_codes)
    dicty = {'encoded_string': encoded_string, 'huffman_codes': huffman_codes}

    decoded_string = decompress_huffman(dict= dicty)
    
    file = filedialog.asksaveasfile(
        mode="w", 
        defaultextension=".txt", 
        filetypes=[("Compressed files", "*.na"), ("All files", "*.*")]
    )
    if file:  
        file.write(decoded_string)
        file.close()

    huffmanPathEntry.delete(0, len(huffmanPathEntry.get()))
    
#------- Golomb-------#

def openGolombTab():
    noteBook.add(golombTab, text= "Golomb")
    noteBook.pack(expand= True, fill= "both")

def encodeGolomb():
    path = pathEntryGolomb.get()
    f = open(path, "r")
    m = nEntry.get()
    lines = []

    try:
        lines = f.readlines()
    except UnicodeDecodeError as e:
        huffmanPathEntry.delete(0, tk.END)
        pop = tk.Tk()
        pop.title("Arithmatic Code")
        pop.geometry("360x144")
        outPut = tk.Entry(master= pop,)
        outPut.delete(0, len(outPut.get()))
        outPut.insert(0, "Enter a valid file you ****")
        outPut.config(state= "readonly")
        outPut.pack(expand= True)
        pop.mainloop()
        return
    
    lines = "".join(lines[:])

    numbers = re.findall(r'\d+', lines)
    numbers = [int(num) for num in numbers]
    encoded_data = [golomb_encode(number, int(m)) for number in numbers]

    file = filedialog.asksaveasfile(
        mode="w", 
        defaultextension=".txt", 
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file:
            for number in encoded_data: 
                file.write(f"{str(number)}, ")
            file.close()

    pathEntryGolomb.delete(0, len(pathEntryGolomb.get()))

def decodeGolomb():
    path = pathEntryGolomb.get()
    f = open(path, "r")
    m = nEntry.get()
    try:
        lines = f.readlines()
    except UnicodeDecodeError as e:
        huffmanPathEntry.delete(0, tk.END)
        pop = tk.Tk()
        pop.title("Arithmatic Code")
        pop.geometry("360x144")
        outPut = tk.Entry(master= pop,)
        outPut.delete(0, len(outPut.get()))
        outPut.insert(0, "Enter a valid file you ****")
        outPut.config(state= "readonly")
        outPut.pack(expand= True)
        pop.mainloop()
        return
    
    lines = "".join(lines[:])
    codes = re.findall(r'\d+', lines)
    print(codes)
    decoded_data = [golomb_decode(code, int(m)) for code in codes]
    print(decoded_data)

    file = filedialog.asksaveasfile(
        mode="w", 
        defaultextension=".txt", 
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file:
            for number in decoded_data: 
                file.write(f"{str(number)}, ")
            file.close()



#---------- arithmatic----------#
def openArithTab():
    noteBook.add(arithTab, text= "Arithmatic")
    noteBook.pack(expand= True, fill= "both")

def encodeArith():
    path = pathEntryArith.get()
    f = open(path, "r")
    try:
        lines = f.readlines()
    except UnicodeDecodeError as e:
        huffmanPathEntry.delete(0, tk.END)
        pop = tk.Tk()
        pop.title("Arithmatic Code")
        pop.geometry("360x144")
        outPut = tk.Entry(master= pop,)
        outPut.delete(0, len(outPut.get()))
        outPut.insert(0, "Enter a valid file you ****")
        outPut.config(state= "readonly")
        outPut.pack(expand= True)
        pop.mainloop()
        return
    
    lines = "".join(lines[0:1])
    pattern = r'\{[^}]+\}'
    dict_str = re.search(pattern, lines).group()
    seq = re.sub(pattern, '', lines)
    probs = ast.literal_eval(dict_str)
    cumuProbs = getCumulativeProbs(probs= probs)
    code = arithmetic_encode(sequence= seq, probabilities= probs, cumulative_probs= cumuProbs)
    
    pop = tk.Tk()
    pop.title("Arithmatic Code")
    pop.geometry("360x144")
    outPut = tk.Entry(master= pop,)
    outPut.delete(0, len(outPut.get()))
    outPut.insert(0, f"{code}")
    outPut.config(state= "readonly")
    outPut.pack(expand= True)
    pop.mainloop()

mainWindow = tk.Tk()

#----------- variables ----------#
framesWidth = 1020
framesHeight = 720

#--------- assets ---------------#
sideBarMenu = tk.PhotoImage(file='menu.png')
firstAlgorithmPhoto = tk.PhotoImage(file='Rectangle1.png')
activeFirstAlgorithmPhoto = tk.PhotoImage(file= 'Rectangle2.png')
orange_button = tk.PhotoImage(file= "button_orange.png")
homeBackGround = Image.open("cato.png")
homeBackGround = ImageTk.PhotoImage(homeBackGround)
chooseButtonPhoto = tk.PhotoImage(file= "chooseButto.png")
compressPhoto = tk.PhotoImage(file= "compress.png")

#---------- main window configuration ----------#
mainWindow.title("Compressor")
mainWindow.config(bg=mainWindowColor)
mainWindow.geometry("1260x720")


#---------- sidebar -----------------#
sidebar = tk.Frame(
    mainWindow,
    bg=sideBarColor,
    height=1260,
    width=240,
    container=False,)
sidebar.place(x= 0)
sidebar.pack_propagate(False)

homebutton = createButton(image= orange_button, frame= sidebar, text= "Home")
homebutton.place(x= 5,y=146)
homebutton.config(command= openHomeFrame)
algobutton = createButton(image= orange_button, frame= sidebar, text= "Algorithms")
algobutton.place(x= 5,y=216)
algobutton.config(command= openAlgorithmFrame)

aboutbutton = createButton(image= orange_button, frame= sidebar, text= "About")
aboutbutton.place(x= 5,y=286)
aboutbutton.config(command= openAboutFrame)

# showsidebar_button = tk.Button(mainWindow,
#                         text="show sidebar",
#                         command=showSideBar,
#                         image=sideBarMenu,
#                         highlightthickness=0,
#                         borderwidth=0,
#                         bg=mainWindow.cget("bg"),
#                         activebackground="blue")

# showsidebar_button.place(x=0)

#------------- home frame --------------------#
homeFrame = tk.Frame(
    mainWindow,
    width= framesWidth,
    height= framesHeight,
)
homeFrame.place(x= 240)
homeFrame.pack_propagate(False)
backGround = createButton(
    image= homeBackGround,
    frame= homeFrame, text= " ")

backGround.config(relief= "flat")
backGround.pack(expand= True, fill="both", )

#------------- algorithm frame ---------------#
algoritmsButtonWidth = 30
algoritmsButtonHeight = 8
algorithmFrame = tk.Frame(
    mainWindow,
    width= framesWidth,
    height= framesHeight,
    bg= aboutFrameColor)
algorithmFrame.pack_propagate(False)

noteBook = ttk.Notebook(algorithmFrame,)

mainTab = tk.Frame(noteBook, background= aboutFrameColor)
huffmanTab = tk.Frame(noteBook, background= aboutFrameColor)
golombTab = tk.Frame(noteBook, background= aboutFrameColor)
arithTab = tk.Frame(noteBook, background= aboutFrameColor)

noteBook.add(mainTab, text= "Main",)
noteBook.pack(expand= True, fill= "both")

huffmanButton = createButton(
    image= firstAlgorithmPhoto,
    frame= mainTab, text= "Huffman Encoding")
huffmanButton.config(
    command= openHuffmanTab, 
    compound= "center", font= ("Arial", 20))
huffmanButton.place(x= 10, y= 50)
huffmanButton.bind("<Leave>", inactivateFirstAlgorithm)
huffmanButton.bind("<Enter>", activateFirstAlgorithm)

golombButton = createButton(
    image= firstAlgorithmPhoto,
    frame= mainTab, text= "Golomb Encoding"
)

golombButton.config(
    command= openGolombTab, 
    compound= "center", font= ("Arial", 20))

golombButton.place(x= 500, y= 50)
golombButton.bind("<Leave>", inactivateGolomb)
golombButton.bind("<Enter>", activateGolomb)

arithButton = createButton(
    image= firstAlgorithmPhoto,
    frame= mainTab, text= "Arithmatic Encoding"
)

arithButton.config(
    command= openArithTab,
    compound= "center", font= ("Arial", 20)
)
arithButton.place(x= 10, y= 350)
arithButton.bind("<Leave>", inactivateArith)
arithButton.bind("<Enter>", activateArith)

#---- huffman tab -------#

huffmanPathEntry = tk.Entry(master= huffmanTab, width= 30)
huffmanPathEntry.pack_propagate(False)
huffmanPathEntry.config(font= ("Arial", 20))
huffmanPathEntry.place(x= 260, y= 360)
huffmanChooseButton = createButton(
    image= chooseButtonPhoto,
    frame= huffmanTab,
    text= "Select",)
huffmanChooseButton.config(compound= "center", height= 30 , command= selectFile)
huffmanChooseButton.place(x= 720, y= 359)

huffmanCompressButton = createButton(
    image= compressPhoto,
    frame= huffmanTab,
    text= "Compress",)
huffmanCompressButton.config(compound= "center", height= 30 , command= encodeHuffman)
huffmanCompressButton.place(x= 720, y= 419)

huffmanDecompressButton = createButton(
    image= compressPhoto,
    frame= huffmanTab,
    text= "Decompress",)
huffmanDecompressButton.config(compound= "center", height= 30 , command= decodeHuffman)
huffmanDecompressButton.place(x= 720, y= 479)

#---- golomb tab -------#

pathEntryGolomb = tk.Entry(master= golombTab, width= 30)
pathEntryGolomb.pack_propagate(False)
pathEntryGolomb.config(font= ("Arial", 20))
pathEntryGolomb.place(x= 260, y= 360)
nLabel = tk.Label(master= golombTab, text= "The N number:", bg= aboutFrameColor, fg= "white", font= ("Arial", 15) )
nLabel.place(x= 260, y= 435)
nEntry = tk.Entry(master= golombTab, width=5)
nEntry.pack_propagate(False)
nEntry.config(font= ("Arial", 20))
nEntry.place(x= 400, y= 430)

chooseButton = createButton(
    image= chooseButtonPhoto,
    frame= golombTab,
    text= "Select",)
chooseButton.config(compound= "center", height= 30 , command= selectFileGolomb)
chooseButton.place(x= 720, y= 359)

compressButton = createButton(
    image= compressPhoto,
    frame= golombTab,
    text= "Compress",)
compressButton.config(compound= "center", height= 30 , command= encodeGolomb)
compressButton.place(x= 720, y= 419)

decompressButton = createButton(
    image= compressPhoto,
    frame= golombTab,
    text= "Deompress",)
decompressButton.config(compound= "center", height= 30 , command= decodeGolomb)
decompressButton.place(x= 720, y= 470)


#--------- arithematic tab ------------#

pathEntryArith = tk.Entry(master= arithTab, width= 30)
pathEntryArith.pack_propagate(False)
pathEntryArith.config(font= ("Arial", 20))
pathEntryArith.place(x= 260, y= 360)

arithChooseButton = createButton(
    image= chooseButtonPhoto,
    frame= arithTab,
    text= "Select",)
arithChooseButton.config(compound= "center", height= 30 , command= selectFileArith)
arithChooseButton.place(x= 720, y= 359)

arithCompressButton = createButton(
    image= compressPhoto,
    frame= arithTab,
    text= "Compress",)
arithCompressButton.config(compound= "center", height= 30 , command= encodeArith)
arithCompressButton.place(x= 720, y= 419)

#--------------- about frame ---------------#
noteImage = tk.PhotoImage(file= "notes.png")
huffman = tk.PhotoImage(file= "huffman.png")
aboutFrame = tk.Frame(
    mainWindow, width= framesWidth,
    height= framesHeight, background= "blue")

aboutCanva= tk.Canvas(
    aboutFrame,
    background= aboutFrameColor,
    height= framesHeight,
    width= framesWidth,
    highlightthickness= 0,
    borderwidth= 0)

aboutCanva.place(x= 0)

scroll = tk.Scrollbar(aboutFrame, orient= "vertical", command= aboutCanva.yview,width= 500)
scroll.place(x= 1000)

aboutCanva.configure(yscrollcommand= scroll.set)

frame = tk.Frame(aboutCanva, bg="white", width=framesWidth, height=framesHeight) 

aboutCanva.create_window(0, 0, window=frame, anchor="nw")

note = createNote(image= huffman)
note.pack()
note.config(state= "active")

mainWindow.mainloop()
