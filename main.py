print("vjoiner started")

# Import everything needed to edit video clips
from moviepy.editor import *
from pathlib import Path

 
# loading video dsa gfg intro video
# clip = VideoFileClip("v1.mp4")

# getting subclip as video is large
# clip1 = clip.subclip(0, 5)

# p = Path('d.mov')
# p.rename(p.with_suffix('.webm'))

# p = Path('a.mp4')
# p.rename(p.with_suffix('.webm'))

# print(p)
clipa = VideoFileClip("wmv1.wmv")
clipb = VideoFileClip("avi1.avi")
clipc = VideoFileClip("mpg1.mpg")
clipd = VideoFileClip("mkv1.mkv")
clipe = VideoFileClip("mpeg1.mpeg")
clipx = VideoFileClip("vid-1.mp4")
clipy = VideoFileClip("d.mov")
clipz = VideoFileClip("a.webm")
# getting subclip as video is large
 
# concatenating both the clips
final = concatenate_videoclips([clipa,clipb,clipc,clipd,clipe,clipx,clipy,clipz],method='compose')
#writing the video into a file / saving the combined video
final.write_videofile("merged.mp4")
 
