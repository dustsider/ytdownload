from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

#download video function to obtain from a url a stream filter with mp4 file extension and obtaining highest quality image
def download_video(url,save_dir):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_dir)
        print("Video downloaded successfully!")
        # look up alternative downloading methods if needed
    except Exception as e:
        print(e)

#function to open file explorer to find appropriate folder/directory to place download
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
#sample url: "https://www.youtube.com/watch?v=iLBBRuVDOo4" (you can remove the 'watch?v=' and will still download it)                
    video_url = input("Type/copy-paste YouTube URL here: ")
    save_dir = open_file_dialog()
# somehow still downloads the video, try to download to the same directory as this program, may put in an exception or if-else if possible,
#but for now goes straight...may just be a fail-safe 

    if save_dir:
        print(" Now downloading...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location")