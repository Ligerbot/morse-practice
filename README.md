# Morse practice

Choose two different modes, one where you type dashes and dots and the program converts them, or one where you hold or tap space bar for variable length dashes and dots (second one not added yet).

`python3 beeper.py` runs the converter from dots and dashes to sound.

playsound is required, otherwise on Linux you might hear weird screeching.

To add more of a gap between words just add extra spaces or look in the top of beeper.py for settings.

Also to enable or disable the auto id at start check in the top of beeper.py for `autoid = True`

# Dependencies

This is for an installation in WSL2 Debian.

### Install playsound

If you have python 3.14;

>pip install playsound

If you have python 3.13;  *this is what we have tested*

>pip install playsound==1.2.2

you may need to add **--break-system-packages**

### Install pyaudio

>pip3 install pyaudio

you may need to add **--break-system-packages**

### Resolving Errors

If you get error

>ModuleNotFoundError: No module named 'gi'

then run

>sudo apt install python3-gi

If you get error

>  File "/usr/lib/python3/dist-packages/gi/__init__.py", line 122, in require_version
> 
>    raise ValueError('Namespace %s not available' % namespace)
> 
>ValueError: Namespace Gst not available

then you should both

>sudo apt upgrade

and

>sudo apt-get install -y \
>
>    python3-gi \
>
>    python3-gi-cairo \
>
>    gir1.2-gstreamer-1.0 \
>
>    gstreamer1.0-plugins-base \
>
>    gstreamer1.0-plugins-good \
>
>    libgstreamer1.0-de

(you may not need every one of these packages)
