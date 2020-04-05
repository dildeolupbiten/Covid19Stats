# -*- coding: utf-8 -*-

from .modules import tk, Tv


class Entry(tk.Entry):
    def __init__(self, treeview: Tv = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack()
        self.treeview = treeview
        self.right_click = None
        self.configure(font="Default 10 italic")
        self.insert(index="0", string="Search a country...")
        self.bind(
            sequence="<Button-1>",
            func=lambda event: self.delete_default_text(
                text="Search a country..."
            )
        )
        self.bind(
            sequence="<KeyRelease>",
            func=lambda event: self.search_name()
        )
        self.bind(
            sequence="<Button-3>",
            func=lambda event: self.popup(
                event=event,
                func=self.button_3_on_entry
            )
        )
        self.bind(
            sequence="<Control-KeyRelease-a>",
            func=lambda event: self.select_range(0, tk.END)
        )
        self.treeview.bind(
            sequence="<Button-1>",
            func=lambda event: self.insert_default_text(
                text="Search a country..."
            )
        )      
        
    def popdown(self):
        if self.right_click:
            self.right_click.destroy()
            self.right_click = None

    def popup(
            self,
            event: tk.Event = None,
            func=None
    ):
        self.popdown()
        if not self.treeview.selection():
            return
        self.right_click = tk.Menu(master=None, tearoff=False)
        func()
        self.right_click.post(event.x_root, event.y_root)
                
    def delete_default_text(self, text: str = ""):
        self.popdown()
        if text in self.get():
            self.configure(font="Default 10")
            self.delete("0", "end")

    def insert_default_text(self, text: str = ""):
        self.popdown()
        if not self.get():
            self.configure(font="Default 10 italic")
            self.insert(
                index="0",
                string=text
            )

    def search_name(self):
        for i, j in enumerate(self.treeview.get_children()):
            if self.get().capitalize() == self.treeview.item(j)["values"][0]:
                self.treeview.selection_set(j)
                self.treeview.yview_moveto(
                    i / len(self.treeview.get_children())
                )
                     
    def button_3_on_entry(self):
        self.right_click.add_command(
            label="Copy",
            command=lambda: self.master.focus_get(
            ).event_generate('<<Copy>>')
        )
        self.right_click.add_command(
            label="Cut",
            command=lambda: self.master.focus_get(
            ).event_generate('<<Cut>>')
        )
        self.right_click.add_command(
            label="Delete",
            command=lambda: self.master.focus_get(
            ).event_generate('<<Clear>>')
        )
        self.right_click.add_command(
            label="Paste",
            command=lambda: self.master.focus_get(
            ).event_generate('<<Paste>>')
        )
