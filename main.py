from tkinter import *
import time

window = Tk()
window.title("Typing Speed App")
window.config(padx=50, pady=50)

timer = None
start = None


def start_func():
    words_entry.config(state='normal')
    start_button.config(state='disabled')
    end_button.config(state='normal')

    global start
    start = time.time()
    update()


def update():
    elapsed = time.time() - start
    char_per_min.config(
        text=f"Characters per second: {round(len(words_entry.get()) / elapsed, 2)}")
    window.update()

    global timer
    timer = window.after(1000, lambda: update())


def end():
    window.after_cancel(timer)
    top = Toplevel(window)
    top.config(padx=50, pady=50)
    top.title("Characters per minute")
    start_button.config(state='normal')
    end_button.config(state='disabled')
    Label(
        top, text=f'Characters per minute: {round(len(words_entry.get()) / 60, 2)}').grid()
    Label(
        top, text=f'Seconds passed: {round(time.time() - start, 2)}').grid(row=1)
    words_entry.delete(0, END)
    Button(top, text='Close', command=top.destroy).grid(row=2)


char_per_min = Label(window, text=f"Characters per minute: 0")
words_entry = Entry(window, width=35, state='disabled')
start_button = Button(window, text="Start", command=start_func)
end_button = Button(window, text="End", command=end, state='disabled')
exit_button = Button(window, text='Exit', command=window.destroy)

char_per_min.grid(row=0, columnspan=2)
words_entry.grid(row=1, columnspan=2, sticky='EW')
start_button.grid(row=2, column=0)
end_button.grid(row=2, column=1)
exit_button.grid(row=2, columnspan=2)

window.mainloop()
