"""
Section 11 Challenge - DataListbox
Fix the DataListbox class so that it displays the songs for the correct album,
when the same album name appears more than once in the database.

Hint: It's worth taking the time to work out what you need the query to be,
then check the code to see at what point you actually have the information you'll need.
"""
import sqlite3
import tkinter


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + " = ?" + self.sql_sort
            self.cursor.execute(sql, (link_value,))
        else:
            self.cursor.execute(self.sql_select + self.sql_sort)

        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        value = None

        if self.linked_box:
            if self.curselection():
                index = self.curselection()[0]
                value = self.get(index),

            if self.link_value and value:
                value = value[0], self.link_value
                sql_where = " WHERE " + self.field + " = ? AND " + self.link_field + " = ?"
            else:
                sql_where = " WHERE " + self.field + " = ?"

            if value:
                link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
                self.linked_box.requery(link_id)


if __name__ == '__main__':
    conn = sqlite3.connect('music.sqlite')

    mainWindow = tkinter.Tk()
    mainWindow.title('Music DB Browser')
    mainWindow.geometry('1024x768')

    # Columns
    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)

    # Rows
    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # Labels
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # Artists Listbox
    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistList.config(border=2, relief='sunken')

    artistList.requery()

    # Albums Listbox
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.config(border=2, relief='sunken')

    artistList.link(albumList, "artist")

    # Songs Listbox
    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
    songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songList.config(border=2, relief='sunken')

    albumList.link(songList, "album")

    # Main loop
    mainWindow.mainloop()
    conn.close()
