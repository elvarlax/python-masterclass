"""
Section 11 Challenge - Music Browser
It's pretty basic, but demonstrates some useful techniques for subclassing an existing class.

We want to put a scrollbar next to each listbox, but we'll put them in the same column as their listbox.
So we'll need 3 columns.

The space between the lists will be set using padding, but there's something I want to demonstrate when
we come to subclass the listboxes. So we'll set the padding on the left of each list, but for the far right
of the display, I'm going to use another column, to keep the songs list away from the edge of the window.
You don't have to do that, I'm only doing it to make explaining something else easier.

We also want a title above each box, so there'll be at least 2 rows.
Because there'll be far more artists than albums or songs, we're going to span the artists listbox over 2 rows.

We'll also leave a blank row along the bottom, to keep everything away from the edge of the window.
So that's 4 rows in total.

Once we've decided that, we can set up the windows.
"""
import tkinter

mainWindow = tkinter.Tk()
mainWindow.title('Music DB Browser')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# Labels
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# Artists Listbox
artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# Artists Scrollbar
artistScrollBar = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
artistScrollBar.grid(row=1, column=0, sticky='nse', rowspan=2)
artistList['yscrollcommand'] = artistScrollBar.set

# Albums Listbox
albumListValue = tkinter.Variable(mainWindow)
albumListValue.set(("Choose an artist",))
albumList = tkinter.Listbox(mainWindow, listvariable=albumListValue)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# Albums Scrollbar
albumScrollBar = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
albumScrollBar.grid(row=1, column=1, sticky='nse')
albumList['yscrollcommand'] = albumScrollBar.set

# Songs Listbox
songListValue = tkinter.Variable(mainWindow)
songListValue.set(("Choose an album",))
songList = tkinter.Listbox(mainWindow, listvariable=songListValue)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# Main loop
testList = range(0, 100)
albumListValue.set(tuple(testList))
mainWindow.mainloop()
