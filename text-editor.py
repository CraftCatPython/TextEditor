from tkinter import *
from tkinter.filedialog import *
from datetime import datetime
import pyperclip
from tkinter.font import Font
from tkinter.messagebox import *
root = Tk()
root.title('Untitled - CometCode')
root.geometry('700x700')
root.config(bg="#373737")
text = Text(root)
scroll = Scrollbar(root)
text.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set, undo=True, bg="#373737", fg="#FFFFFF", font=(text["font"], 16), insertbackground="white")
scroll.config(command=text.yview)
fontsss = ['System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Chomsky', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype', 'Sans Serif Collection', 'Segoe Fluent Icons', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'Segoe UI Variable Small Light', 'Segoe UI Variable Small Semilig', 'Segoe UI Variable Small', 'Segoe UI Variable Small Semibol', 'Segoe UI Variable Text Light', 'Segoe UI Variable Text Semiligh', 'Segoe UI Variable Text', 'Segoe UI Variable Text Semibold', 'Segoe UI Variable Display Light', 'Segoe UI Variable Display Semil', 'Segoe UI Variable Display', 'Segoe UI Variable Display Semib', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Small Semibold', 'Sitka Text', 'Sitka Text Semibold', 'Sitka Subheading', 'Sitka Subheading Semibold', 'Sitka Heading', 'Sitka Heading Semibold', 'Sitka Display', 'Sitka Display Semibold', 'Sitka Banner', 'Sitka Banner Semibold', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight', 'HoloLens MDL2 Assets', 'Agency FB', 'Algerian', 'Book Antiqua', 'Arial Rounded MT Bold', 'Baskerville Old Face', 'Bauhaus 93', 'Bell MT', 'Bernard MT Condensed', 'Bodoni MT', 'Bodoni MT Black', 'Bodoni MT Condensed', 'Bodoni MT Poster Compressed', 'Bradley Hand ITC', 'Britannic Bold', 'Berlin Sans FB', 'Berlin Sans FB Demi', 'Broadway', 'Brush Script MT', 'Californian FB', 'Calisto MT', 'Castellar', 'Century Schoolbook', 'Centaur', 'Chiller', 'Colonna MT', 'Cooper Black', 'Copperplate Gothic Bold', 'Copperplate Gothic Light', 'Curlz MT', 'Dubai', 'Dubai Light', 'Dubai Medium', 'Elephant', 'Engravers MT', 'Eras Bold ITC', 'Eras Demi ITC', 'Eras Light ITC', 'Eras Medium ITC', 'Felix Titling', 'Forte', 'Franklin Gothic Book', 'Franklin Gothic Demi', 'Franklin Gothic Demi Cond', 'Franklin Gothic Heavy', 'Franklin Gothic Medium Cond', 'Freestyle Script', 'French Script MT', 'Footlight MT Light', 'Gigi', 'Gill Sans MT', 'Gill Sans MT Condensed', 'Gill Sans Ultra Bold Condensed', 'Gill Sans Ultra Bold', 'Gloucester MT Extra Condensed', 'Gill Sans MT Ext Condensed Bold', 'Century Gothic', 'Goudy Old Style', 'Goudy Stout', 'Harlow Solid Italic', 'Harrington', 'Haettenschweiler', 'High Tower Text', 'Imprint MT Shadow', 'Informal Roman', 'Blackadder ITC', 'Edwardian Script ITC', 'Kristen ITC', 'Jokerman', 'Juice ITC', 'Kunstler Script', 'Wide Latin', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Lucida Handwriting', 'Lucida Sans', 'Lucida Sans Typewriter', 'Magneto', 'Maiandra GD', 'Matura MT Script Capitals', 'Mistral', 'Modern No. 20', 'Monotype Corsiva', 'Niagara Engraved', 'Niagara Solid', 'OCR A Extended', 'Old English Text MT', 'Onyx', 'MS Outlook', 'Palace Script MT', 'Papyrus', 'Parchment', 'Perpetua', 'Perpetua Titling MT', 'Playbill', 'Poor Richard', 'Pristina', 'Rage Italic', 'Ravie', 'Rockwell Condensed', 'Rockwell', 'Rockwell Extra Bold', 'Script MT Bold', 'Showcard Gothic', 'Snap ITC', 'Stencil', 'Tw Cen MT', 'Tw Cen MT Condensed', 'Tw Cen MT Condensed Extra Bold', 'Tempus Sans ITC', 'Viner Hand ITC', 'Vivaldi', 'Vladimir Script', 'Arial Unicode MS', '@Arial Unicode MS', 'Open Sans', 'Open Sans Semibold', 'Cascadia Code ExtraLight', 'Cascadia Code Light', 'Cascadia Code SemiLight', 'Cascadia Code', 'Cascadia Code SemiBold', 'Cascadia Mono ExtraLight', 'Cascadia Mono Light', 'Cascadia Mono SemiLight', 'Cascadia Mono', 'Cascadia Mono SemiBold', 'Bookshelf Symbol 7', 'MS Reference Sans Serif', 'MS Reference Specialty', 'Arial Narrow', 'Garamond', 'Century', 'Wingdings 2', 'Wingdings 3', 'Bookman Old Style', 'MS Mincho', '@MS Mincho', 'Quest Knight', 'Zen Tokyo Zoo']
fontsizes = []
for i in range(100):
	fontsizes.append(i)
colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light gray', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'Slategray1', 'Slategray2', 'Slategray3','Slategray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlategray1', 'DarkSlategray2', 'DarkSlategray3', 'DarkSlategray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4','grey1', 'grey2', 'grey3', 'grey4', 'grey5', 'grey6', 'grey7', 'grey8', 'grey9', 'grey10','grey11', 'grey12', 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19','grey20', 'grey21', 'grey22', 'grey23', 'grey24', 'grey25', 'grey26', 'grey27', 'grey28','grey29', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34', 'grey35', 'grey36', 'grey37','grey38', 'grey39', 'grey40', 'grey42', 'grey43', 'grey44', 'grey45', 'grey46', 'grey47','grey48', 'grey49', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55', 'grey56','grey57', 'grey58', 'grey59', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64', 'grey65','grey66', 'grey67', 'grey68', 'grey69', 'grey70', 'grey71', 'grey72', 'grey73', 'grey74','grey75', 'grey76', 'grey77', 'grey78', 'grey79', 'grey80', 'grey81', 'grey82', 'grey83','grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89', 'grey90', 'grey91', 'grey92','grey93', 'grey94', 'grey95', 'grey97', 'grey98', 'grey99']
def search():
	selected_text = text.selection_get()
	char = text.search(selected_text, 1.0)
	length = (len(selected_text)) / 100
	char = float(char)
	tot = char + length
	return char, tot
def setbackgroundcolor(color, top):
	text.config(bg=color)
	top.destroy()
def backgroundcolor():
	top = Toplevel()
	top.title('Background Color')
	top.geometry('225x100')
	color = StringVar()
	colorss = Label(top, text="Background Color: ")
	colorsss = OptionMenu(top, color, *colors)
	colorbtn = Button(top, relief="solid", text="Set Background Color", command=lambda: setbackgroundcolor(color.get(), top))
	colorss.grid(row=0, column=0)
	colorsss.grid(row=0, column=1)
	colorbtn.grid(row=2, column=0, pady=10)	
def settextcolor(color, top):
	text.config(fg=color)
	top.destroy()
def textcolor():
	top = Toplevel()
	top.title('Text Color')
	top.geometry('225x100')
	color = StringVar()
	colorss = Label(top, text="Text Color: ")
	colorsss = OptionMenu(top, color, *colors)
	colorbtn = Button(top, relief="solid", text="Set Text Color", command=lambda: settextcolor(color.get(), top))
	colorss.grid(row=0, column=0)
	colorsss.grid(row=0, column=1)
	colorbtn.grid(row=2, column=0, pady=10)
def lightmode():
	text.config(bg="#FFFFFF", fg="#000000", insertbackground="black")
def darkmode():
	text.config(bg="#373737", fg="#FFFFFF", insertbackground="white") 
def setfontsize(size):
	font = (text["font"], size);text.config(font=Font(text, font))
def fontsize():
	top = Toplevel()
	top.title('Font Size')
	top.geometry('225x100')

	size = StringVar()

	sizes = Label(top, text="Font Size: ")
	sizess = OptionMenu(top, size, *fontsizes)
	sizebtn = Button(top, relief="solid", text="Set Font Size", command=lambda: setfontsize(size.get()))

	sizes.grid(row=0, column=0)
	sizess.grid(row=0, column=1)
	sizebtn.grid(row=2, column=0, pady=10)
def setfont(font):
	font = (font, 12);text.config(font=Font(text, font))
def fontset():
	top = Toplevel()
	top.title('Font')
	top.geometry('225x100')

	font = StringVar()
	font.set(text["font"])

	size = StringVar()
	size.set(12)

	fonts = Label(top, text="Font: ")
	fontss = OptionMenu(top, font, *fontsss)
	fontbtn = Button(top, relief="solid", text="Set Font", command=lambda: setfont(font.get()))

	fonts.grid(row=0, column=0)
	fontss.grid(row=0, column=1)
	fontbtn.grid(row=2, column=0, pady=10)

def findd(t):
    text.tag_remove('found', '1.0', END)

    if t:
        idx = '1.0'
        while 1:
            idx = text.search(t, idx, nocase=1,
                              stopindex=END)
            if not idx: break
             
            lastidx = '%s+%dc' % (idx, len(t))

            text.tag_add('found', idx, lastidx)
            idx = lastidx
         
        text.tag_config('found', foreground='red', background='blue')

def find():
	top = Toplevel()
	top.title('Find')
	top.geometry('225x70')

	find = Label(top, text="Find: ", font=("Helvetica", 12))
	entry = Entry(top, relief="flat", width=20, font=("Helvetica", 12))
	findbtn = Button(top, relief="solid", text="Find", command=lambda: findd(entry.get()))

	find.grid(row=0, column=0)
	entry.grid(row=0, column=1)
	findbtn.grid(row=1, column=0, pady=10)

def bold():
	try:
		char, tot = search()
	except:
		char, tot = 1.0, END
	font = Font(text, text.cget("font"))
	font.configure(weight="bold")
	text.tag_configure("bold", font=font)
	currtag = text.tag_names('sel.first')
	if "bold" in currtag:
		text.tag_remove("bold", char, tot)
	else:
		text.tag_add("bold", char, tot)

def ital():
	try:
		char, tot = search()
	except:
		char, tot = 1.0, END
	font = Font(text, text.cget("font"))
	font.configure(slant="italic")
	text.tag_configure("italic", font=font)
	currtag = text.tag_names('sel.first')
	if "italic" in currtag:
		text.tag_remove("italic", char, tot)
	else:
		text.tag_add("italic", char, tot)

def under():
	try:
		char, tot = search()
	except:
		char, tot = 1.0, END
	font = Font(text, text.cget("font"))
	font.configure(underline=True)
	text.tag_configure("under", font=font)
	currtag = text.tag_names('sel.first')
	if "under" in currtag:
		text.tag_remove("under", char, tot)
	else:
		text.tag_add("under", char, tot)


def paste():
	text.insert("insert", pyperclip.paste())
def cut():
	char, tot = search()
	pyperclip.copy(text.get(char, tot))
	text.delete(char, tot)
def copy():
	char, tot = search()
	pyperclip.copy(text.get(char, tot))
def delete():
	char, tot = search()
	text.delete(char, tot)
def allt():
	text.tag_add(SEL, "1.0", END)
	text.mark_set(INSERT, "1.0")
	text.see(INSERT)
def time():
	now = datetime.now()
	text.insert("insert", now.strftime('%Y/%m/%d %I:%M:%S'))
def new():
	text.delete(1.0, END)
	root.title('Untitled - CometCode')
def openfile():
	filename = askopenfilename(filetypes=(('Text Files', '*.txt'), ('All Files', '*.*'), ('Python Files', '*.py'), ('Javascript Files', '*.js')))
	file = open(filename, 'r+')
	text.delete(1.0, END)
	text.insert(1.0, file.read())
	root.title(filename + ' - CometCode')

def saveas():
	filename = asksaveasfilename(filetypes=(('Text Files', '*.txt'), ('All Files', '*.*'), ('Python Files', '*.py'), ('Javascript Files', '*.js')))
	if filename:
		file = open(filename, 'w+')
		file.write(text.get(1.0, END))
		root.title(filename + ' - CometCode')

def save():
	title = root.title()
	if not title.find('Untitled'):
		saveas()
	else:
		title = title.replace(' - CometCode', '')
		file = open(title, 'w+')
		file.write(text.get(1.0, END))
		root.title(title + ' - CometCode')

def update(event):
	if event.char == '':
		save()
	elif event.char == '':
		openfile()
	elif event.char == '':
		new()
	elif event.char == '':
		time()
	elif event.char == '':
		allt()

def run():
	menu = Menu(root, tearoff=False)
	root.config(menu=menu)
	file_menu = Menu(menu, tearoff=False)
	menu.add_cascade(label='File', menu=file_menu)
	file_menu.add_command(label='New', command=new, accelerator='Ctrl+N')
	file_menu.add_command(label='Save', command=save, accelerator='Ctrl+S')
	file_menu.add_command(label='Save As', command=saveas, accelerator='Ctrl+Shift+S')
	file_menu.add_command(label='Open', command=openfile, accelerator='Ctrl+O')
	file_menu.add_separator()
	file_menu.add_command(label='Exit', command=root.destroy)
	edit_menu = Menu(menu, tearoff=False)
	menu.add_cascade(label='Edit', menu=edit_menu)
	edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', command=text.edit_undo)
	edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', command=text.edit_redo)
	edit_menu.add_separator()
	edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=cut)
	edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=copy)
	edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=paste)
	edit_menu.add_command(label='Delete', accelerator='Del', command=delete)
	edit_menu.add_separator()
	edit_menu.add_command(label='Select All', accelerator='Ctrl+A', command=allt)
	edit_menu.add_command(label='Time/Date', accelerator='Ctrl+T', command=time)
	edit_menu.add_command(label='Find', accelerator='Ctrl+T', command=find)
	textview = Menu(menu, tearoff=False)
	textview.add_command(label='Bold', command=bold)
	textview.add_command(label='Underline', command=under)
	textview.add_command(label='Italic', command=ital)
	textview.add_command(label='Font', command=fontset)
	textview.add_command(label='Font Size', command=fontsize)
	textview.add_separator()
	textview.add_command(label='Dark Mode', command=darkmode)
	textview.add_command(label='Light Mode', command=lightmode)
	textview.add_command(label='Custom Background Color', command=backgroundcolor)
	textview.add_command(label='Custom Text Color', command=textcolor)
	menu.add_cascade(label='Text/View', menu=textview)
	root.bind('<Key>',update)
	root.mainloop()
run()