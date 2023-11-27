import customtkinter as ctk


class TreeGraphGUI:
    def __init__(self, master, adjacency_list, values):
        self.master = master
        self.values = values
        self.adjacency_list = adjacency_list
        self.canvas = ctk.CTkCanvas(master=master, width=1200, height=1000, scrollregion=(0, 0, 14_000, 2000))
        self.scroll_bar = ctk.CTkScrollbar(master=master, orientation='horizontal', command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.scroll_bar.set)
        self.scroll_bar.place(relx=0, rely=1, anchor='sw', relwidth=1)
        self.canvas.bind('<Shift-Button-4>', lambda event: self.canvas.xview_scroll(-1, 'units'))
        self.canvas.bind('<Shift-Button-5>', lambda event: self.canvas.xview_scroll(1, 'units'))
        self.canvas.pack(expand=True, fill='both')

    def draw_tree(self, node, x, y, dx, dy, color, k):
        if node in self.adjacency_list:
            children = self.adjacency_list[node]
            num_children = len(children)
            radius = 15
            dx = dx / 7
            if num_children > 0:
                h = num_children // 2
                for i, child in enumerate(children):
                    if i < h:
                        x_child = x - (h - i) * dx
                    else:
                        x_child = x + (i - h) * dx
                    y_child = y + dy + radius
                    child_color = 'red'
                    if color == 'red':
                        child_color = 'yellow'
                    self.canvas.create_line(x, y, x_child, y_child)
                    self.draw_tree(child, x_child, y_child, dx, dy, child_color, k + 5)

            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
            self.canvas.create_text(x, y, text=str(self.values[node]))

    def display_tree(self):
        root_node = list(self.adjacency_list.keys())[0]
        self.draw_tree(root_node, 7000, 150, 14000, 100, 'red', 1)


def main():
    adjacency_list = {}
    for i in range(400):
        adjacency_list[i] = []
    for i in range(57):
        for j in range(1, 8):
            adjacency_list[i].append(i * 7 + j)
    for i in range(57, 400):
        adjacency_list[i] = []
    values = []
    for i in range(400):
        values.append(i)
    root = ctk.CTk()
    root.title("Tree Graph GUI")

    tree_gui = TreeGraphGUI(root, adjacency_list, values)
    tree_gui.display_tree()

    root.mainloop()


if __name__ == "__main__":
    main()
