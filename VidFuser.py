from moviepy.editor import *
from tkinter import filedialog
from tkinter import *
import os, sys, time

extensions = [".mp4", ".avi", ".mov", ".mts"]
clips = []

def specify_src():
    global src_folder
    src_folder = filedialog.askdirectory()
    return src_folder

def specify_dest():
    global dest_folder
    dest_folder = filedialog.askdirectory()
    return dest_folder

def fuse_vids():
    global src_folder, dest_folder

    try:
        src_folder = src_folder
    except NameError:
        src_folder = os.getcwd()

    for filename in os.listdir(src_folder):
        try:
            vid_file = VideoFileClip(os.path.join(src_folder,filename))
            clips.append(vid_file)
        except Exception as e:
            print(f'Skipping {filename} as it is not a valid file.')

    try:
        dest_folder = dest_folder
    except NameError:
        dest_folder = os.getcwd()
    
    if len(clips) > 1:            
        print(f'Stitching {len(clips)} videos...')
        #stitched = concatenate_videoclips(clips)
        #stitched.write_videofile(os.path.join(dest_folder,'stitched_vids.mp4'))
        print(f'Done. You may now quit the app.')
        input()
    elif len(clips) == 1:
        print(f'Only 1 video found.')
        time.sleep(1)
        print(f'Exiting app...')
        time.sleep(1)
    else:
        print(f'No videos found.')
        time.sleep(1)
        print(f'Exiting app...')
        time.sleep(1)
        raise Exception
        sys.exit()

root = Tk()
root.title('VidFuser')
#root.iconbitmap('')
root.geometry('500x300')

lf = LabelFrame(root, text = 'VidFuser')
lf.pack(padx=20)

my_frame = Frame(root)
#my_frame.pack(pady=10)

spec_src_button = Button(my_frame, text="Choose Source Folder", command = specify_src).place(x=0,y=0)
#spec_src_button.grid(row=0, column=0, padx=10)
src_label = Label(my_frame, text="ehehe", anchor="w")
src_label.grid(row=0, column=1, padx=10)


spec_loc_button = Button(my_frame, text="Choose Destination", anchor="w", command = specify_dest)
spec_loc_button.grid(row=1, column=0, padx=10)

fuse_button = Button(my_frame, text="Start Fusing", command = fuse_vids)
fuse_button.grid(row=2, column=0, padx=10)

root.mainloop()
