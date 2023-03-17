from moviepy.editor import *
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import os, sys, time

clips = []

def specify_src():
    src_folder_init = filedialog.askdirectory()
    spec_src_entry.delete(0, END)
    spec_src_entry.insert(END,src_folder_init)

def specify_dest():
    dest_folder_init = filedialog.askdirectory()
    spec_dest_entry.delete(0, END)
    spec_dest_entry.insert(END,dest_folder_init)    

def fuse_vids():
    src_folder = spec_src_entry.get()
    dest_folder = spec_dest_entry.get()
    
    #print(f'src_folder: {src_folder}\ndest_folder: {dest_folder}')
    
    for filename in os.listdir(src_folder):
        try:
            vid_file = VideoFileClip(os.path.join(src_folder,filename))
            clips.append(vid_file)
        except Exception as e:
            print(f'Skipping {filename} as it is not a valid video file.')
    
    if len(clips) > 1:            
        print(f'Stitching {len(clips)} videos...')
        stitched = concatenate_videoclips(clips)
        stitched.write_videofile(os.path.join(dest_folder, output_name_entry.get()))
        print(f'Done. You may now quit the app.')
        input()
    elif len(clips) == 1:
        print(f'Only 1 video found.')
        time.sleep(1)
        print(f'Exiting app...')
        time.sleep(1)
        root.destroy()
        sys.exit()
    else:
        print(f'No videos found.')
        time.sleep(1)
        print(f'Exiting app...')
        time.sleep(1)
        root.destroy()
        sys.exit()

root = Tk()
root.title('VidFuser')
root.iconbitmap('resources/VidFuser.ico')
root.geometry('400x150')

photo = Image.open('resources/folder.ico')
photo = photo.resize((15,15), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)

# -- Source Folder
spec_src_lbl = Label(root, text="Source Folder:")
spec_src_lbl.grid(row=0, column=0)

spec_src_entry = Entry(root, width=40)
spec_src_entry.grid(row=0, column=1)
spec_src_entry.insert(END, os.getcwd())

spec_src_button = Button(root, text="Browse", image=img, command = specify_src)
spec_src_button.grid(row=0, column=2, padx=5)

# -- Destination Folder
spec_dest_lbl = Label(root, text="Target Folder:")
spec_dest_lbl.grid(row=1, column=0)
spec_dest_entry = Entry(root, width=40)
spec_dest_entry.grid(row=1, column=1)
spec_dest_entry.insert(END, os.getcwd())
spec_dest_button = Button(root, text="Browse", image=img, command = specify_dest)
spec_dest_button.grid(row=1, column=2, padx=5)

# -- Output Name
output_name_lbl = Label(root, text="Output Name:")
output_name_lbl.grid(row=2, column=0)
output_name_entry = Entry(root, width=40)
output_name_entry.grid(row=2, column=1)
output_name_entry.insert(END, "output.mp4")

fuse_button = Button(root, text="Start Fusing", command = fuse_vids)
fuse_button.grid(row=3, column=1, pady=30)

root.mainloop()
