import tkinter as tk
import json

# load genres and stories
with open("storydata.json") as file:
    obj = json.load(file)
list_genre_lbls = (obj["list_genre_lbls"])
colors = (obj["colors"])
genres = (obj["genres"])
stories = (obj["stories"])

# game
root = tk.Tk()
root.geometry("800x650")
root.resizable(width=False, height=False)
root.title("Create a Story")
root.configure(background="ghost white")


def create_heading(heading, headingfont):
    lbl_heading = tk.Label(root, text=heading, font=headingfont,
                           background="ghost white")

    lbl_heading.pack(anchor="center", pady=15, padx=10)
    return lbl_heading


def create_frame():
    fr1 = tk.Frame(root, relief="ridge", background="ghost white")

    fr1.pack(anchor="center", fill="x", pady=15)
    return fr1


def pack_lbls(list, bg_color):
    """Displays different prompts based on the chosen genre"""
    global vars_genre
    vars_genre = []
    for index, x in enumerate(list):
        lbl_words = tk.Label(frame_words, text=f"{x}:",
                             background=bg_color,
                             font=("Calibre", 15))
        lbl_words.pack(padx=5, pady=5, anchor="w")
        txt_words = tk.Entry(frame_words_txt, font=("Calibre", 15))
        vars_genre.append(txt_words)
        txt_words.pack(padx=5, pady=5, anchor="e")


def enter_words(genre):
    bg_color = colors[genres.index(genre)]
    for child in frame_words.winfo_children():
        child.pack_forget()

    frame_buttons.pack_forget()
    lbl_genre.configure(text="Enter your words here:", background=bg_color)
    lbl_create.configure(background=bg_color)

    root.configure(background=bg_color)
    frame_words.pack(side="left")
    frame_words.configure(background=bg_color, padx=100, pady=1)
    frame_words_txt.pack(side="right")
    frame_words_txt.configure(background=bg_color, padx=100, pady=1)

    pack_lbls(list_genre_lbls[genres.index(genre)], bg_color)

    btn_get_story = tk.Button(frame_words_txt, text="Read Story",
                              command=lambda: display_story(genre), font=("Calibri", 12, "bold"),
                              background="ghost white",
                              activebackground="ghost white")
    btn_get_story.pack(padx=5, pady=5, fill="x")
    btn_back = tk.Button(frame_words, text="Back", font=("Calibri", 12, "bold"),
                         background="ghost white",
                         activebackground="ghost white",
                         command=back_button)
    btn_back.pack(padx=5, pady=5, fill="x")


def back_button():
    root.configure(background="ghost white")
    for child in frame_buttons.winfo_children():
        child.pack_forget()
    frame_buttons.pack_forget()

    for i in range(len(vars_genre)):
        vars_genre[i] = tk.StringVar(root, value="")

    for child in frame_words.winfo_children():
        child.pack_forget()
    for child in frame_words_txt.winfo_children():
        child.pack_forget()
    for child in frame_story.winfo_children():
        child.pack_forget()
    frame_words_txt.pack_forget()
    frame_words.pack_forget()
    frame_story.pack_forget()
    frame_buttons.pack(fill="x")
    for i in range(len(genres)):
        create_buttons(genres[i], colors[i])
    lbl_create.configure(text="Create your own story", background="ghost white")
    lbl_genre.configure(text="Choose a genre:", background="ghost white")


def save_story(title, description, text):
    f = open("newstory.txt", "a")
    f.write(f"{title}\n{description}\n\n{text}\n")
    f.close()


def display_story(genre):
    """Displays the finished story with the words the user has entered."""
    bg_color = colors[genres.index(genre)]

    entries = []
    for i in range(len(vars_genre)):
        entries.append(vars_genre[i].get())

    (var0, var1, var2, var3, var4, var5, var6, var7, var8, var9) = entries

    frame_words_txt.pack_forget()
    frame_words.pack_forget()

    lbl_create.configure(text=var0.title())

    lbl_genre.configure(text=f"A {genre} Story")
    frame_story.pack()
    frame_story.configure(background=bg_color)

    lbl_story = tk.Label(frame_story, text=eval(f'f"""{stories[genres.index(genre)]}"""'), background=bg_color,
                         font=("Calibri", 15))

    lbl_story.pack(pady=40, padx=20)

    lbl_saved = tk.Label(frame_story)
    lbl_saved.configure(text="", background=bg_color,
                        font=("Calibri", 15, "italic"), height=2)
    lbl_saved.pack()

    btn_save = tk.Button(frame_story, text="Save Story",
                         command=lambda: [save_story(lbl_create["text"], lbl_genre["text"], lbl_story["text"]),
                                          lbl_saved.configure(text="Your story has been saved.")],
                         background="ghost white", activebackground="ghost white",
                         pady=5, padx=5, font=("Calibri", 15, "bold"), width=13)

    btn_save.pack()

    btn_restart = tk.Button(frame_story, text="Start Over", command=back_button,
                            background="ghost white", activebackground="ghost white",
                            pady=5, padx=5, font=("Calibri", 15, "bold"), width=13)
    btn_restart.pack()


def create_buttons(genre, bgcolor):
    btn1 = tk.Button(frame_buttons, text=genre,
                     font=("Calibri", 20, "bold"),
                     padx=10, pady=10,
                     activebackground=bgcolor,
                     background=bgcolor,
                     command=lambda: enter_words(genre))

    btn1.pack(fill="x", padx=30)


lbl_create = create_heading("Create your own story", ("Calibri", 40, "bold"))
lbl_genre = create_heading("Choose a genre:", ("Calibri", 30, "bold", "italic"))

frame_buttons = create_frame()
for i in range(len(genres)):
    create_buttons(genres[i], colors[i])

frame_words = create_frame()
frame_words_txt = create_frame()
frame_story = create_frame()

root.mainloop()
