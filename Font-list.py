import tkinter as tk
from tkinter import font

fontes = [
    "MS Gothic", "MS PGothic", "MS UI Gothic", "Malgun Gothic", "Malgun Gothic Semilight",
    "Microsoft JhengHei", "Microsoft JhengHei Light", "Microsoft JhengHei UI", "Microsoft JhengHei UI Light",
    "Microsoft YaHei", "Microsoft YaHei Light", "Microsoft YaHei UI", "Microsoft YaHei UI Light",
    "MingLiU-ExtB", "MingLiU_HKSCS-ExtB", "MingLiU_MSCS-ExtB", "NSimSun", "PMingLiU-ExtB",
    "SimSun", "SimSun-ExtB", "SimSun-ExtG", "Yu Gothic", "Yu Gothic Light", "Yu Gothic Medium",
    "Yu Gothic UI", "Yu Gothic UI Light", "Yu Gothic UI Semibold", "Yu Gothic UI Semilight",
    "Agency FB", "Algerian", "Arabic Transparent", "Arial", "Arial Baltic", "Arial Black", "Arial CE",
    "Arial CYR", "Arial Greek", "Arial Narrow", "Arial Rounded MT Bold", "Arial TUR", "Bahnschrift",
    "Bahnschrift Condensed", "Bahnschrift Light", "Bahnschrift Light Condensed", "Bahnschrift Light SemiCondensed",
    "Bahnschrift SemiBold", "Bahnschrift SemiBold Condensed", "Bahnschrift SemiBold SemiConden",
    "Bahnschrift SemiCondensed", "Bahnschrift SemiLight", "Bahnschrift SemiLight Condensed",
    "Bahnschrift SemiLight SemiConde", "Baskerville Old Face", "Bauhaus 93", "Bell MT", "Berlin Sans FB",
    "Berlin Sans FB Demi", "Bernard MT Condensed", "Blackadder ITC", "Bodoni MT", "Bodoni MT Black",
    "Book Antiqua", "Bookman Old Style", "Bradley Hand ITC", "Britannic Bold", "Broadway", "Brush Script MT",
    "Calibri", "Calibri Light", "Cambria", "Cambria Math", "Candara", "Candara Light", "Cascadia Code",
    "Cascadia Mono", "Castellar", "Century", "Century Gothic", "Chiller", "Comic Sans MS", "Consolas",
    "Constantia", "Cooper Black", "Corbel", "Courier", "Courier New", "Curlz MT", "Dubai", "Ebrima",
    "Edwardian Script ITC", "Elephant", "Engravers MT", "Eras Bold ITC", "Felix Titling", "Fixedsys",
    "Footlight MT Light", "Forte", "Franklin Gothic Book", "Freestyle Script", "Gabriola", "Garamond",
    "Georgia", "Gigi", "Gill Sans MT", "Gloucester MT Extra Condensed", "Goudy Old Style", "Haettenschweiler",
    "Harlow Solid Italic", "Harrington", "High Tower Text", "Impact", "Imprint MT Shadow", "Ink Free",
    "Jokerman", "Juice ITC", "Kristen ITC", "Kunstler Script", "Leelawadee", "Lucida Bright",
    "Lucida Calligraphy", "Lucida Console", "Lucida Handwriting", "Lucida Sans Unicode", "MS Sans Serif",
    "MS Serif", "MV Boli", "Magneto", "Maiandra GD", "Marlett", "Matura MT Script Capitals",
    "Microsoft Himalaya", "Microsoft New Tai Lue", "Microsoft PhagsPa", "Microsoft Sans Serif",
    "Microsoft Tai Le", "Microsoft Uighur", "Microsoft Yi Baiti", "Mistral", "Modern", "Monotype Corsiva",
    "Myanmar Text", "Niagara Engraved", "Niagara Solid", "Nirmala Text", "OCR A Extended",
    "Old English Text MT", "Onyx", "Palace Script MT", "Palatino Linotype", "Papyrus", "Perpetua",
    "Playbill", "Poor Richard", "Pristina", "Rage Italic", "Ravie", "Rockwell", "Roman",
    "Script MT Bold", "Segoe Print", "Segoe Script", "Segoe UI", "Segoe UI Black", "Segoe UI Emoji",
    "Segoe UI Historic", "Segoe UI Light", "Segoe UI Semibold", "Segoe UI Semilight",
    "Showcard Gothic", "Sitka Banner", "Sitka Display", "Sitka Heading", "Sitka Small", "Sitka Subheading",
    "Sitka Text", "Snap ITC", "Stencil", "Sylfaen", "Tahoma", "Tempus Sans ITC", "Terminal",
    "Times New Roman", "Trebuchet MS", "Tw Cen MT", "Verdana", "Viner Hand ITC", "Vivaldi",
    "Vladimir Script", "Webdings", "Wide Latin", "Wingdings", "Wingdings 2", "Wingdings 3"
]

root = tk.Tk()
root.title("Visualizador de Fontes")
root.geometry("700x800")

canvas = tk.Canvas(root, borderwidth=0, background="white")
frame = tk.Frame(canvas, background="white")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=frame, anchor="nw")

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

for fonte in fontes:
    try:
        label = tk.Label(frame, text=f"{fonte}", font=(fonte, 16), bg="white", anchor="w")
        label.pack(fill="x", padx=10, pady=3)
    except tk.TclError:
        continue

root.mainloop()
