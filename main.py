import tkinter as tk
import time

FONT=("Courier", 18, "normal")
TIMER = None
WORDS = ""
CONTADOR = 0
FGCOLOR = 'black'

def timer(count):
    global TIMER, WORDS, CONTADOR, FGCOLOR

    count = count - initialTime
    count_min = count // 60
    count_seg = (count % 60)
    count_cent = (count_seg % 1) * 10000
    lbl_timer.configure(text=str(f"Tempo:  {int(count_min):0>2}:{int(count_seg//1):0>2}:{int(count_cent):0>4}"), font=FONT)

    response = response_text.get("1.0", "end-1c")
    words_response = response.split(' ')

    for i in range(0, len(WORDS)):
        try:
            if WORDS[i] == words_response[i]:
                CONTADOR = i + 1
        except:
            break

    wordsps = 0.0
    if (count_min * 60) + count_seg > 0 and CONTADOR > 0:
        wordsps = (CONTADOR) / int(((count_min * 60) + count_seg)//1)

    lbl_qtd.configure(text=f"Qtd. Palavras: {CONTADOR}", font=FONT)
    lbl_wps.configure(text=f"Words Per Second: {round(wordsps, 2)}", font=FONT)
    lbl_wpm.configure(text=f"Words Per Minute: {round(wordsps * 60, 2)}", font=FONT)

    if CONTADOR == 0:
        resposta = ""
        FGCOLOR = "black"
    elif wordsps * 60 < 40:
        resposta = "abaixo da média"
        FGCOLOR = "red"
    elif wordsps * 60 > 40:
        resposta = "acima da média"
        FGCOLOR = "green"
    else:
        resposta = "na média"
        FGCOLOR = "black"

    lbl_result.configure(text=f"Você está: {resposta}", font=FONT, fg=FGCOLOR)

    TIMER = root.after(100, timer, time.perf_counter())


root = tk.Tk()
root.title('Typing Speed Test')
root.geometry("2050x1100")
root.resizable(0, 0)

lblTitle = tk.Label(text="Typing Speed Test", font=("Courier", 35, "bold"), fg="blue")
lblTitle.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

lbl_timer = tk.Label(text="Tempo: 00:00:0000", font=FONT)
lbl_timer.grid(row=1, column=1, padx=10, pady=10)

lbl_qtd = tk.Label(text="Qtd. Palavras: 0", font=FONT)
lbl_qtd.grid(row=2, column=1, padx=10, pady=10)

lbl_wps = tk.Label(text="Words Per Second: 0.00", font=FONT)
lbl_wps.grid(row=3, column=1, padx=10, pady=10)

lbl_wpm = tk.Label(text="Words Per Minute: 0.00", font=FONT)
lbl_wpm.grid(row=4, column=1, padx=10, pady=10)

lbl_result = tk.Label(text="", font=FONT)
lbl_result.grid(row=5, column=1, padx=10, pady=10)

text = ""
with open("text.txt") as file:
    text = file.read()

lbl_text = tk.Text(root, height=30, width=200)
lbl_text.grid(row=1, column=0, rowspan=5, padx=10, pady=10)
lbl_text.insert(tk.END, text)
lbl_text.configure(state=tk.DISABLED)
lbl_text.event_delete('<<Copy>>', '<Control-c>')

WORDS = text.split(' ')

response_text = tk.Text(root, height=30, width=200)
response_text.event_delete('<<Paste>>', '<Control-v>')
response_text.grid(row=6, column=0, padx=10, pady=10)


initialTime = time.perf_counter()

time.sleep(3)

finalTime = time.perf_counter()

timer(initialTime)

root.mainloop()
