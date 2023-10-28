from tkinter import *
from pytube import YouTube


def videodownload():
    try:
        at_work.set("Downloading...")
        window.update()
        video_url = get_url.get()
        yt = YouTube(video_url)
        video_we_got = yt.streams.get_highest_resolution()
        video_we_got.download()
        finished_work.set("Video download successfully")
    except Exception as e:
        at_work.set("Mistake")
        finished_work.set("Enter correct url")
        window.update()


window = Tk()
window.geometry("400x400")
window.title("Youtube Video Downloader")

get_url = StringVar()
at_work = StringVar()
finished_work = StringVar()

Label(window, text="Youtube Video Downloader", font="calibri 20 bold").pack()
Label(window, text="Write URL here").pack(pady=5)
Entry(window, textvariable=get_url, width=40).pack(pady=5)
Entry(window, textvariable=at_work, width=40).pack(pady=5)
Entry(window, textvariable=finished_work, width=40).pack(pady=5)
Button(window, text="Click To download", command=videodownload).pack(pady=10)

window.mainloop()
