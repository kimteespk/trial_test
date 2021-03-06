
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1503x800")
window.configure(bg = "#EAF4FF")
        


canvas = Canvas(
    window,
    bg = "#EAF4FF",
    height = 800,
    width = 1503,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1503.0,
    79.19911193847656,
    fill="#1167B1",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    954.2857971191406,
    42.612905502319336,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EAF4FF",
    highlightthickness=0
)
entry_1.place(
    x=894.7142944335938,
    y=29.26474380493164,
    width=119.14300537109375,
    height=24.69632339477539
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1160.0535278320312,
    41.72302436828613,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EAF4FF",
    highlightthickness=0
)
entry_2.place(
    x=1100.4820556640625,
    y=28.374858856201172,
    width=119.1429443359375,
    height=24.696331024169922
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    542.7499542236328,
    42.612905502319336,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EAF4FF",
    highlightthickness=0
)
entry_3.place(
    x=483.1785583496094,
    y=29.26474380493164,
    width=119.14279174804688,
    height=24.69632339477539
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    336.982177734375,
    44.392656326293945,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EAF4FF",
    highlightthickness=0
)
entry_4.place(
    x=277.4107666015625,
    y=31.044490814208984,
    width=119.142822265625,
    height=24.696331024169922
)

canvas.create_text(
    770.6851806640625,
    107.6751937866211,
    anchor="nw",
    text="Feed",
    fill="#1167B1",
    font=("RobotoRoman ExtraBold", 25 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1220.0,
    y=679.0,
    width=249.0,
    height=87.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1220.0,
    y=575.0,
    width=249.0,
    height=96.0
)

canvas.create_rectangle(
    1241.0,
    121.0,
    1461.0,
    416.0,
    fill="#EAF4FF",
    outline="")

canvas.create_text(
    760.0,
    540.0,
    anchor="nw",
    text="Report",
    fill="#1167B1",
    font=("RobotoRoman ExtraBold", 25 * -1)
)

canvas.create_text(
    440.4625244140625,
    11.71875,
    anchor="nw",
    text="Timeframe",
    fill="#EAF4FF",
    font=("RobotoRoman Bold", 17 * -1)
)

canvas.create_text(
    651.2999877929688,
    11.71875,
    anchor="nw",
    text="Size(coin)",
    fill="#EAF4FF",
    font=("RobotoRoman Bold", 17 * -1)
)

canvas.create_text(
    245.52976989746094,
    11.568408012390137,
    anchor="nw",
    text="Symbol",
    fill="#EAF4FF",
    font=("RobotoRoman Bold", 17 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    748.5178833007812,
    42.612905502319336,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#EAF4FF",
    highlightthickness=0
)
entry_5.place(
    x=688.9464721679688,
    y=29.26474380493164,
    width=119.142822265625,
    height=24.69632339477539
)

canvas.create_rectangle(
    422.0,
    137.0,
    1174.0,
    519.0,
    fill="#81B8F5",
    outline="")

canvas.create_text(
    865.8154907226562,
    11.568408012390137,
    anchor="nw",
    text="API",
    fill="#EAF4FF",
    font=("RobotoRoman Bold", 17 * -1)
)

canvas.create_text(
    1063.6309814453125,
    11.568408012390137,
    anchor="nw",
    text="Secret",
    fill="#EAF4FF",
    font=("RobotoRoman Bold", 17 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    797.5,
    687.5,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#81B8F5",
    highlightthickness=0
)
entry_6.place(
    x=464.0,
    y=575.0,
    width=667.0,
    height=223.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    183.6999969482422,
    411.18299865722656,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#81B8F5",
    highlightthickness=0
)
entry_7.place(
    x=0.0,
    y=210.01112365722656,
    width=367.3999938964844,
    height=400.34375
)

canvas.create_text(
    133.20237731933594,
    180.64515686035156,
    anchor="nw",
    text="Indicator",
    fill="#1167B1",
    font=("RobotoRoman Bold", 25 * -1)
)

canvas.create_text(
    80.0,
    238.0,
    anchor="nw",
    text="EMA Cross",
    fill="#EAF4FF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)

canvas.create_text(
    80.0,
    280.0,
    anchor="nw",
    text="SMA Cross",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)

canvas.create_text(
    80.0,
    322.0,
    anchor="nw",
    text="RSI Cross",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)

canvas.create_text(
    82.0,
    364.0,
    anchor="nw",
    text="MACD Cross",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)

canvas.create_text(
    82.0,
    406.0,
    anchor="nw",
    text="RSI",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)

canvas.create_text(
    82.0,
    448.0,
    anchor="nw",
    text="Stochastic",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)

canvas.create_text(
    80.0,
    490.0,
    anchor="nw",
    text="Supertrend",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)

canvas.create_rectangle(
    38.0,
    238.0,
    58.0,
    256.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    38.0,
    280.0,
    58.0,
    298.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    38.0,
    322.0,
    58.0,
    340.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    38.0,
    364.0,
    58.0,
    382.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    38.0,
    406.0,
    58.0,
    424.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    38.0,
    448.0,
    58.0,
    466.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    38.0,
    490.0,
    58.0,
    508.0,
    fill="#FFFFFF",
    outline="")

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    229.0,
    247.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_8.place(
    x=216.0,
    y=240.0,
    width=26.0,
    height=12.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    307.0,
    247.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_9.place(
    x=294.0,
    y=240.0,
    width=26.0,
    height=12.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    227.0,
    289.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_10.place(
    x=214.0,
    y=282.0,
    width=26.0,
    height=12.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    307.0,
    289.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_11.place(
    x=294.0,
    y=282.0,
    width=26.0,
    height=12.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    227.0,
    331.0,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_12.place(
    x=214.0,
    y=324.0,
    width=26.0,
    height=12.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    307.0,
    331.0,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_13.place(
    x=294.0,
    y=324.0,
    width=26.0,
    height=12.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    227.0,
    373.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_14.place(
    x=214.0,
    y=366.0,
    width=26.0,
    height=12.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    307.0,
    373.0,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_15.place(
    x=294.0,
    y=366.0,
    width=26.0,
    height=12.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    273.0,
    413.0,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_16.place(
    x=260.0,
    y=406.0,
    width=26.0,
    height=12.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    198.0,
    453.0,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_17.place(
    x=185.0,
    y=446.0,
    width=26.0,
    height=12.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    254.0,
    453.0,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_18.place(
    x=241.0,
    y=446.0,
    width=26.0,
    height=12.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    332.0,
    453.0,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_19.place(
    x=319.0,
    y=446.0,
    width=26.0,
    height=12.0
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    228.0,
    496.0,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_20.place(
    x=215.0,
    y=489.0,
    width=26.0,
    height=12.0
)

entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(
    327.0,
    496.0,
    image=entry_image_21
)
entry_21 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_21.place(
    x=314.0,
    y=489.0,
    width=26.0,
    height=12.0
)

canvas.create_text(
    189.0,
    240.0,
    anchor="nw",
    text="fast",
    fill="#EAF4FF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    265.0,
    240.0,
    anchor="nw",
    text="slow",
    fill="#EAF4FF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    189.0,
    282.0,
    anchor="nw",
    text="fast",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    265.0,
    282.0,
    anchor="nw",
    text="slow",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    189.0,
    324.0,
    anchor="nw",
    text="fast",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    265.0,
    324.0,
    anchor="nw",
    text="slow",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    189.0,
    366.0,
    anchor="nw",
    text="fast",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    265.0,
    366.0,
    anchor="nw",
    text="slow",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    243.0,
    404.0,
    anchor="nw",
    text=">",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)

canvas.create_text(
    176.0,
    446.0,
    anchor="nw",
    text="K",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    230.0,
    446.0,
    anchor="nw",
    text="D",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    284.0,
    446.0,
    anchor="nw",
    text="smooth",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    176.0,
    489.0,
    anchor="nw",
    text="length",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

canvas.create_text(
    262.0,
    489.0,
    anchor="nw",
    text="multiplier",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 10 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=245.0,
    y=561.0,
    width=83.0,
    height=51.0
)

entry_image_22 = PhotoImage(
    file=relative_to_assets("entry_22.png"))
entry_bg_22 = canvas.create_image(
    198.5,
    586.5,
    image=entry_image_22
)
entry_22 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_22.place(
    x=152.0,
    y=578.0,
    width=93.0,
    height=15.0
)

canvas.create_text(
    27.0,
    577.0,
    anchor="nw",
    text="Request indicator",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 15 * -1)
)
window.resizable(False, False)
from tkinter import messagebox

with open('config.txt', 'r+') as f:
    input_token = f.readline()
    input_api = f.readline()
    print(input_token)
    print(input_api)
    
with open('validity.txt', 'r+') as f:
    check_token = f.readline()
    check_api = f.readline()
    print(check_token)
    print(check_api)
    
if check_token == input_token and check_api == input_api:
    window.mainloop()
else:
    messagebox.showerror('Error', 'Trial version has been expire, Please contact facebook page')
