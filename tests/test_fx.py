import pytest
from moviepy.editor import *

from moviepy.video.fx.crop import crop
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.headblur import headblur

import os
import sys
sys.path.append("tests")
import download_media
from test_helper import TRAVIS, TMP_DIR, PYTHON_VERSION


def test_download_media(capsys):
    with capsys.disabled():
       download_media.download()

def test_blackwhite():
    clip = VideoFileClip("media/big_buck_bunny_432_433.webm")
    clip1 = blackwhite(clip)
    clip1.write_videofile(os.path.join(TMP_DIR,"blackwhite1.webm"))

def test_blink():
    #this currently fails with a with_mask error!
    return
    clip = VideoFileClip("media/big_buck_bunny_0_30.webm").subclip(0,10)
    clip1 = blink(clip, 1, 1)
    clip1.write_videofile(os.path.join(TMP_DIR,"blink1.webm"))

def test_colorx():
    clip = VideoFileClip("media/big_buck_bunny_432_433.webm")
    clip1 = colorx(clip, 2)
    clip1.write_videofile(os.path.join(TMP_DIR,"colorx1.webm"))


def test_crop():
    clip = VideoFileClip("media/big_buck_bunny_432_433.webm")

    clip1=crop(clip)   #ie, no cropping (just tests all default values)
    clip1.write_videofile(os.path.join(TMP_DIR, "crop1.webm"))

    clip2=crop(clip, x1=50, y1=60, x2=460, y2=275)
    clip2.write_videofile(os.path.join(TMP_DIR, "crop2.webm"))

    clip3=crop(clip, y1=30)  #remove part above y=30
    clip3.write_videofile(os.path.join(TMP_DIR, "crop3.webm"))

    clip4=crop(clip, x1=10, width=200) # crop a rect that has width=200
    clip4.write_videofile(os.path.join(TMP_DIR, "crop4.webm"))

    clip5=crop(clip, x_center=300, y_center=400, width=50, height=150)
    clip5.write_videofile(os.path.join(TMP_DIR, "crop5.webm"))

    clip6=crop(clip, x_center=300, width=400, y1=100, y2=600)
    clip6.write_videofile(os.path.join(TMP_DIR, "crop6.webm"))

def test_fadein():
    clip = VideoFileClip("media/big_buck_bunny_0_30.webm").subclip(0,5)
    clip1 = fadein(clip, 1)
    clip1.write_videofile(os.path.join(TMP_DIR,"fadein1.webm"))

def test_fadeout():
    clip = VideoFileClip("media/big_buck_bunny_0_30.webm").subclip(0,5)
    clip1 = fadeout(clip, 1)
    clip1.write_videofile(os.path.join(TMP_DIR,"fadeout1.webm"))

def test_freeze():
    clip = VideoFileClip("media/big_buck_bunny_0_30.webm").subclip(0,5)
    clip1 = freeze(clip, t=2, freeze_duration=5)
    clip1.write_videofile(os.path.join(TMP_DIR,"freeze1.webm"))

    clip2 = freeze(clip, t=2, total_duration=10)
    clip2.write_videofile(os.path.join(TMP_DIR,"freeze2.webm"))

    #freeze1 and freeze2 should be the same (freeze duration = 5)

def test_freeze_region():

    #I'm not sure the output video is correct..
    clip = VideoFileClip("media/big_buck_bunny_0_30.webm").subclip(0,5)
    clip1 = freeze_region(clip, t=2, region=(100,100,300,300))
    clip1.write_videofile(os.path.join(TMP_DIR,"freeze_region1.webm"))

def test_gamma_corr():
    #please provide an example of how to use gamma_corr

    return

def test_headblur():

    #opencv is not supported in python 3.3
    if PYTHON_VERSION == '3.3':
       return

    clip = VideoFileClip("media/big_buck_bunny_0_30.webm").subclip(15,20)

    fx= lambda t: 100
    fy= lambda t: 100
    clip1=headblur(clip, fx, fy, 25, 100)
    clip1.write_videofile(os.path.join(TMP_DIR,"headblur1.webm"))

if __name__ == '__main__':
   test_headblur()
   #pytest.main()
