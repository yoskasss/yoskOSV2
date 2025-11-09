# pixel_editor.py - NIHAI VE EN KARARLI VERSİYON
import tkinter as tk
from tkinter import colorchooser, filedialog
import os

class PixelArtEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Piksel Sanat Editörü (Static Kaydedici)")
        self.pixel_size = 10
        self.grid_width = 64
        self.grid_height = 64
        self.current_color = "black"
        self.is_drawing = False

        control_frame = tk.Frame(master)
        control_frame.pack(pady=10)
        canvas_frame = tk.Frame(master)
        canvas_frame.pack()

        tk.Button(control_frame, text="Renk Seç", command=self.choose_color).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Temizle", command=self.clear_canvas).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Farklı Kaydet (.h)", command=self.save_to_header).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(canvas_frame,
                                width=self.grid_width * self.pixel_size,
                                height=self.grid_height * self.pixel_size,
                                bg="white")
        self.canvas.pack()

        self.pixels = {}
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                x1, y1 = x * self.pixel_size, y * self.pixel_size
                x2, y2 = x1 + self.pixel_size, y1 + self.pixel_size
                self.pixels[(x, y)] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Renk Seç")
        if color_code: self.current_color = color_code[1]

    def clear_canvas(self):
        for pixel in self.pixels.values(): self.canvas.itemconfig(pixel, fill="white")

    def start_drawing(self, event):
        self.is_drawing = True
        self.draw(event)

    def draw(self, event):
        if self.is_drawing:
            x, y = event.x // self.pixel_size, event.y // self.pixel_size
            if (x, y) in self.pixels: self.canvas.itemconfig(self.pixels[(x, y)], fill=self.current_color)

    def stop_drawing(self, event): self.is_drawing = False

    def save_to_header(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".h", filetypes=[("C Header files", "*.h")])
        if not file_path: return

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        c_prefix = f"image_{base_name}"

        hex_values = []
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                rgb = self.master.winfo_rgb(self.canvas.itemcget(self.pixels[(x, y)], "fill"))
                r, g, b = rgb[0] // 256, rgb[1] // 256, rgb[2] // 256
                hex_values.extend([f"0x{r:02x}", f"0x{g:02x}", f"0x{b:02x}"])

        if hex_values:
            array_content = ",\n  ".join(", ".join(hex_values[i:i+12]) for i in range(0, len(hex_values), 12))
            
            # *** DEĞİŞİKLİK: Tüm değişkenlerin başına "static const" ekleniyor ***
            header_content = f"""
// Resim verisi: {base_name}
static const unsigned char {c_prefix}_data[] = {{
  {array_content}
}};
static const unsigned int {c_prefix}_len = {len(hex_values)};

#define BITMAP_WIDTH_{base_name} {self.grid_width}
#define BITMAP_HEIGHT_{base_name} {self.grid_height}
"""
            with open(file_path, "w") as f: f.write(header_content)
            print(f"Bitmap başarıyla {file_path} dosyasına kaydedildi ({c_prefix}_data).")

if __name__ == "__main__":
    root = tk.Tk()
    app = PixelArtEditor(root)
    root.mainloop()