import math

import customtkinter as ctk


class TreeGraphGUI:
    def __init__(self, master, adjacency_list, values, levels):
        self.master = master

        self.values = values
        self.adjacency_list = adjacency_list
        self.no_of_nodes = len(self.values)
        self.radius = 20
        self.gap = 10
        self.no_of_levels = levels + 1
        self.no_of_leaves = math.pow(7, self.no_of_levels - 1)
        self.width = self.no_of_leaves * (self.gap + 2 * self.radius) + 3 * self.gap
        self.dx = (self.gap + 2 * self.radius) * math.pow(7, self.no_of_levels - 1)
        self.canvas = ctk.CTkCanvas(master=master, width=1200, height=1000, scrollregion=(0, 0, self.width, 2000))

        self.scroll_bar = ctk.CTkScrollbar(master=master, orientation='horizontal', command=self.canvas.xview)
        self.scroll_bar.place(relx=0, rely=1, anchor='sw', relwidth=1)

        self.canvas.configure(xscrollcommand=self.scroll_bar.set)
        self.canvas.bind('<Shift-Button-4>', lambda event: self.canvas.xview_scroll(-1, 'units'))
        self.canvas.bind('<Shift-Button-5>', lambda event: self.canvas.xview_scroll(1, 'units'))

        self.canvas.pack(expand=True, fill='both')

    def draw_tree(self, node, x, y, dx, dy, color):
        if node in self.adjacency_list:
            children = self.adjacency_list[node]
            num_children = len(children)
            dx = dx / 7
            if num_children > 0:
                h = num_children // 2
                for i, child in enumerate(children):
                    if i < h:
                        x_child = x - (h - i) * dx
                    else:
                        x_child = x + (i - h) * dx
                    y_child = y + dy + self.radius
                    child_color = 'red'
                    if color == 'red':
                        child_color = 'yellow'
                    self.canvas.create_line(x, y, x_child, y_child)
                    self.draw_tree(child, x_child, y_child, dx, dy, child_color)

            self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill=color)
            self.canvas.create_text(x, y, text=f'{self.values[node][1]}, {self.values[node][0]}')

    def display_tree(self):
        root_node = list(self.adjacency_list.keys())[0]
        self.draw_tree(root_node, self.width / 2, 150, self.dx, 100, 'red')


def show(adjacency_list, values):

    root = ctk.CTk()
    root.title("Tree Graph GUI")

    tree_gui = TreeGraphGUI(root, adjacency_list, values, 4)
    tree_gui.display_tree()

    root.mainloop()


# if __name__ == "__main__":

