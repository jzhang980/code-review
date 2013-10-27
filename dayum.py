# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Oh my Dayum! Code Smells

# <markdowncell>

# with `DataCleaning()` code sample inspired thanks to Group 10!

# <codecell>

from IPython.display import HTML

HTML(DataCleaning("Dayum")) #testing for invalid input

# <markdowncell>

# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>

# <codecell>

from IPython.display import YouTubeVideo

videoid = "DcJFdCmN98s"

YouTubeVideo(videoid)

# <markdowncell>

# Later versions of IPython Notebook allow you to use other YouTube parameters, such as `autoplay` and time offset to `start` playing a video from a specified point in time, whereas earlier versions only support embedding the video by id, but don't provide other parameters.

# <codecell>

from datetime import timedelta
start=int(timedelta(hours=0, minutes=1, seconds=12).total_seconds())
start

# <codecell>

YouTubeVideo(videoid, start=start, autoplay=1, theme="light", color="red")

# <markdowncell>

# This StackOverflow article provides further background: http://stackoverflow.com/questions/13119791/can-the-ipython-notebook-youtubevideo-class-play-from-time-offset
# 
# IPython has a [Rich Display System](http://nbviewer.ipython.org/urls/raw.github.com/ipython/ipython/1.x/examples/notebooks/Part%205%20-%20Rich%20Display%20System.ipynb) and you can [Defining Custom Display Logic for Your Own Objects](http://nbviewer.ipython.org/url/github.com/ipython/ipython/raw/master/examples/notebooks/Custom%20Display%20Logic.ipynb).

# <markdowncell>

# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>

# <codecell>

# This cell is *supposed* to be hidden off-screen during a presentation
# But make sure to run this cell first otherwise the first cell will fail.
def DataCleaning(awesomeness):
    return '''
<span style="color:red">Invalid input bro, gg. Valid inputs are "past hour", "past day", "past 7days", "past 30days"</span>

<pre>
This is how code is *supposed* to be

The data they blend so perfectly

The science up in here is goin' dayum, dayum, DAYUM

I wish you could smell what I'm smellin'

You byte<span style="text-decoration: line-through;opacity: 0.3;">-compile</span> the code, the code bites back!

dayum, dayum, DAYUM
</pre>

<a href="http://youtu.be/DcJFdCmN98s?t=1m12s">Click here for further debugging information</a>
'''

