import tkinter as tk

class Calculator:
    # Map for 7-segment unicode representation
    SEGMENT_MAP = {
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰',
        '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵',
        '.': '.', '+': '+', '-': '-', '*': '×', '/': '÷', '=': '=', 'E': 'E', 'r': 'r', 'o': 'o'
    }

    def to_seven_segment(self, s):
        # Not used anymore, but kept for reference
        return ''.join(self.SEGMENT_MAP[ch] if ch in self.SEGMENT_MAP else ch for ch in s)

    # 7-segment segment map: a,b,c,d,e,f,g (see segment order below)
    SEGMENTS = {
        '0': (1,1,1,1,1,1,0),
        '1': (0,1,1,0,0,0,0),
        '2': (1,1,0,1,1,0,1),
        '3': (1,1,1,1,0,0,1),
        '4': (0,1,1,0,0,1,1),
        '5': (1,0,1,1,0,1,1),
        '6': (1,0,1,1,1,1,1),
        '7': (1,1,1,0,0,0,0),
        '8': (1,1,1,1,1,1,1),
        '9': (1,1,1,1,0,1,1),
        '-': (0,0,0,0,0,0,1),
        '+': (0,0,0,0,0,0,2),  # 2 means draw plus
        '*': (0,0,0,0,0,0,3),  # 3 means draw star
        '/': (0,0,0,0,0,0,4),  # 4 means draw slash
        '.': (0,0,0,0,0,0,5),  # 5 means draw dot
        'E': (1,0,0,1,1,1,1),
        'r': (0,0,0,0,1,0,1),
        'o': (0,0,1,1,1,0,1),
        ' ': (0,0,0,0,0,0,0),
    }

    def draw_lcd(self, value):
        # Draw the value as 7-segment digits on the canvas
        self.lcd_canvas.delete('all')
        value = value[-12:].rjust(12)  # Show up to 12 digits, right-aligned
        digit_width = 38
        x0 = 16
        for i, ch in enumerate(value):
            self.draw_digit(x0 + i*digit_width, 10, ch)
        # Redraw border after digits
        self.lcd_canvas.create_rectangle(5, 5, 5 + 12*digit_width + 10, 65, outline='#7fd47f', width=4)

    def draw_digit(self, x, y, ch):
        # Segment coordinates (relative to x, y)
        seg = [
            [(4,0),(24,0),(20,4),(8,4)],      # a
            [(24,0),(28,4),(28,20),(24,24)],  # b
            [(24,24),(28,28),(28,44),(24,48)],# c
            [(4,48),(24,48),(20,44),(8,44)],  # d
            [(0,24),(4,28),(4,44),(0,40)],    # e
            [(0,0),(4,4),(4,24),(0,20)],      # f
            [(4,24),(8,20),(20,20),(24,24),(20,28),(8,28)], # g
        ]
        segments = self.SEGMENTS.get(ch, self.SEGMENTS[' '])
        for i, on in enumerate(segments):
            if i < 6:
                color = '#222' if on else '#b6ffb6'
                self.lcd_canvas.create_polygon(
                    [(x+px, y+py) for (px,py) in seg[i]],
                    fill=color, outline='#7fd47f', width=1
                )
            else:
                # Special handling for g segment for operators
                if on == 1:
                    color = '#222'
                    self.lcd_canvas.create_polygon(
                        [(x+px, y+py) for (px,py) in seg[i]],
                        fill=color, outline='#7fd47f', width=1
                    )
                elif on == 2:  # plus
                    # Draw horizontal and vertical lines for plus
                    self.lcd_canvas.create_line(x+6, y+24, x+26, y+24, fill='#222', width=4)
                    self.lcd_canvas.create_line(x+16, y+14, x+16, y+34, fill='#222', width=4)
                elif on == 3:  # star (*)
                    # Draw a simple star (X)
                    self.lcd_canvas.create_line(x+8, y+16, x+24, y+32, fill='#222', width=3)
                    self.lcd_canvas.create_line(x+24, y+16, x+8, y+32, fill='#222', width=3)
                    self.lcd_canvas.create_line(x+16, y+10, x+16, y+38, fill='#222', width=2)
                elif on == 4:  # slash (/)
                    self.lcd_canvas.create_line(x+24, y+8, x+8, y+40, fill='#222', width=4)
                elif on == 5:  # dot
                    self.lcd_canvas.create_oval(x+20, y+44, x+28, y+52, fill='#222', outline='#7fd47f', width=1)
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.geometry("540x270") # Adjusted size for LCD and buttons

        self.expression = ""
        self.display_var = tk.StringVar()

        # LCD-style display using a Canvas for true 7-segment effect
        digit_width = 38
        canvas_width = 5 + 12*digit_width + 15
        self.lcd_canvas = tk.Canvas(master, width=canvas_width, height=70, bg='#b6ffb6', bd=0, highlightthickness=0)
        self.lcd_canvas.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=8, pady=(8, 4))
        self.lcd_canvas.create_rectangle(5, 5, 5 + 12*digit_width + 10, 65, outline='#7fd47f', width=4)
        self.draw_lcd('0')

        # Button layout with physical calculator look
        btn_font = ("Arial", 16, "bold")
        btn_bg = "#444"
        btn_fg = "#fff"
        op_bg = "#f90"
        eq_bg = "#0c0"
        clr_bg = "#c00"
        btn_style = {"font": btn_font, "width": 4, "height": 2, "bd": 3, "relief": "raised", "bg": btn_bg, "fg": btn_fg, "activebackground": "#666", "activeforeground": "#fff"}

        buttons = [
            ('7', 1, 0, btn_style), ('8', 1, 1, btn_style), ('9', 1, 2, btn_style), ('/', 1, 3, {**btn_style, "bg": op_bg}),
            ('4', 2, 0, btn_style), ('5', 2, 1, btn_style), ('6', 2, 2, btn_style), ('*', 2, 3, {**btn_style, "bg": op_bg}),
            ('1', 3, 0, btn_style), ('2', 3, 1, btn_style), ('3', 3, 2, btn_style), ('-', 3, 3, {**btn_style, "bg": op_bg}),
            ('0', 4, 0, {**btn_style, "width": 10}), ('.', 4, 1, btn_style), ('=', 4, 2, {**btn_style, "bg": eq_bg, "fg": "#fff"}), ('+', 4, 3, {**btn_style, "bg": op_bg}),
        ]
        for (text, row, col, style) in buttons:
            if text == '=':
                btn = tk.Button(master, text=text, command=self.calculate, **style)
            else:
                btn = tk.Button(master, text=text, command=lambda t=text: self.press(t), **style)
            btn.grid(row=row, column=col, padx=3, pady=3, sticky='nsew')

        # Clear button styled
        clear_btn = tk.Button(master, text='C', command=self.clear, font=btn_font, width=20, height=1, bd=3, relief="raised", bg=clr_bg, fg="#fff", activebackground="#f66", activeforeground="#fff")
        clear_btn.grid(row=5, column=0, columnspan=4, sticky='nsew', padx=8, pady=(4, 8))

        # Configure grid weights for resizing
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def press(self, key):
        # Prevent multiple decimals in a number
        if key == '.':
            import re
            tokens = re.split(r'([+\-*/])', self.expression)
            if '.' in tokens[-1]:
                return
        self.expression += str(key)
        self.display_var.set(self.expression)
        self.draw_lcd(self.expression if self.expression else '0')

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.draw_lcd(result)
            self.expression = result # Allow further operations on result
        except:
            self.display_var.set("Error")
            self.draw_lcd("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.display_var.set("")
        self.draw_lcd('0')

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()