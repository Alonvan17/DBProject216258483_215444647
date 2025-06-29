import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
import time
import random


class GradientFrame(tk.Canvas):
    """Custom frame with gradient background"""

    def __init__(self, parent, color1="#667eea", color2="#764ba2", **kwargs):
        super().__init__(parent, **kwargs)
        self.color1 = color1
        self.color2 = color2
        self.bind('<Configure>', self._draw_gradient)

    def _draw_gradient(self, event=None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()

        if width > 1 and height > 1:
            # Create gradient effect
            for i in range(height):
                ratio = i / height
                # Interpolate between colors
                r1, g1, b1 = self._hex_to_rgb(self.color1)
                r2, g2, b2 = self._hex_to_rgb(self.color2)

                r = int(r1 + (r2 - r1) * ratio)
                g = int(g1 + (g2 - g1) * ratio)
                b = int(b1 + (b2 - b1) * ratio)

                color = f"#{r:02x}{g:02x}{b:02x}"
                self.create_line(0, i, width, i, fill=color, tags="gradient")

    def _hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


class StyledButton(tk.Button):
    """Styled button with hover effects using tkinter Button"""

    def __init__(self, parent, text, command, bg_color="#ffffff", text_color="#333333",
                 hover_color="#f0f0f0", **kwargs):
        # Configure button style
        super().__init__(
            parent,
            text=text,
            command=command,
            bg=bg_color,
            fg=text_color,
            font=("Segoe UI", 10, "bold"),  # Reduced font size from 11 to 10
            relief="flat",
            bd=2,
            padx=15,  # Reduced padding from 20 to 15
            pady=8,  # Reduced padding from 12 to 8
            width=35,  # Reduced width from 38 to 35
            height=2,
            cursor="hand2",
            activebackground=hover_color,
            activeforeground=text_color,
            **kwargs
        )

        self.default_bg = bg_color
        self.hover_bg = hover_color
        self.text_color = text_color

        # Bind hover events
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def _on_enter(self, event):
        self.configure(bg=self.hover_bg, relief="raised")

    def _on_leave(self, event):
        self.configure(bg=self.default_bg, relief="flat")


class FloatingParticle:
    """Animated floating particle for background effect"""

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vx = (random.random() - 0.5) * 1.5
        self.vy = (random.random() - 0.5) * 1.5
        self.size = int(random.random() * 3) + 1

        # Use predefined colors
        colors = ["#ffffff", "#f0f0f0", "#e0e0e0"]
        color = random.choice(colors)

        self.particle = canvas.create_oval(
            x - self.size, y - self.size,
            x + self.size, y + self.size,
            fill=color, outline=""
        )

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off edges
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if canvas_width > 0 and canvas_height > 0:
            if self.x <= 0 or self.x >= canvas_width:
                self.vx *= -1
            if self.y <= 0 or self.y >= canvas_height:
                self.vy *= -1

            self.canvas.coords(
                self.particle,
                self.x - self.size, self.y - self.size,
                self.x + self.size, self.y + self.size
            )


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DB Project App - Advanced management system")
        self.configure(bg="#1a1a2e")

        # Set window to fullscreen
        self.state('zoomed')  # For Windows
        # Alternative for other systems: self.attributes('-zoomed', True)

        # Enable fullscreen toggle with F11 and Escape
        self.bind('<F11>', self.toggle_fullscreen)
        self.bind('<Escape>', self.end_fullscreen)

        # Track fullscreen state
        self.fullscreen_state = True

        self.resizable(True, True)

        # Create main gradient background
        self.bg_canvas = GradientFrame(
            self,
            color1="#667eea",
            color2="#764ba2",
            highlightthickness=0
        )
        self.bg_canvas.pack(fill=tk.BOTH, expand=True)

        # Initialize particles for background animation
        self.particles = []
        self.animation_running = True

        # Wait for canvas to be drawn before initializing particles
        self.after(100, self.init_particles)

        # Create main content
        self.create_main_content()

        # Start animation loop
        self.animate()

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode"""
        self.fullscreen_state = not self.fullscreen_state
        if self.fullscreen_state:
            self.state('zoomed')
        else:
            self.state('normal')
            self.geometry("950x750")
            self.center_window()
        # Recreate content with proper sizing
        self.after(100, self.recreate_content)

    def end_fullscreen(self, event=None):
        """Exit fullscreen mode"""
        self.fullscreen_state = False
        self.state('normal')
        self.geometry("950x750")
        self.center_window()
        # Recreate content with proper sizing
        self.after(100, self.recreate_content)

    def recreate_content(self):
        """Recreate main content with proper sizing"""
        # Clear existing content
        for widget in self.bg_canvas.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
        # Recreate content
        self.create_main_content()

    def center_window(self):
        """Center the window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (950 // 2)
        y = (self.winfo_screenheight() // 2) - (750 // 2)
        self.geometry(f"950x750+{x}+{y}")

    def init_particles(self):
        """Initialize floating particles"""
        canvas_width = self.bg_canvas.winfo_width()
        canvas_height = self.bg_canvas.winfo_height()

        if canvas_width > 1 and canvas_height > 1:
            # Increase particle count for fullscreen
            particle_count = max(15, int((canvas_width * canvas_height) / 20000))
            for _ in range(particle_count):
                x = random.randint(0, canvas_width)
                y = random.randint(0, canvas_height)
                particle = FloatingParticle(self.bg_canvas, x, y)
                self.particles.append(particle)

    def animate(self):
        """Animation loop for background effects"""
        if self.animation_running:
            try:
                for particle in self.particles:
                    particle.update()
                self.after(60, self.animate)  # Smoother animation - 60ms instead of 80ms
            except tk.TclError:
                # Handle case where window is destroyed
                pass

    def create_main_content(self):
        """Create the main application content"""
        # Main container frame with semi-transparent effect
        main_container = tk.Frame(self.bg_canvas, bg="#ffffff", bd=2, relief="raised")
        # Adjust height based on screen size - more height for fullscreen
        container_height = 0.92 if self.fullscreen_state else 0.85
        main_container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.82, relheight=container_height)

        # Create content frame that fills the container
        content_frame = tk.Frame(main_container, bg="#f8f9fa")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)

        # Title section
        self.create_title_section(content_frame)

        # Buttons section
        self.create_buttons_section(content_frame)

        # Footer
        self.create_footer(content_frame)

    def create_title_section(self, parent):
        """Create title section"""
        title_frame = tk.Frame(parent, bg="#f8f9fa")
        title_frame.pack(fill=tk.X, pady=(0, 15))  # Reduced padding from 20 to 15

        # Main title
        title_label = tk.Label(
            title_frame,
            text="Navy and Armored Corps database",
            font=("Segoe UI", 24, "bold"),  # Reduced font size from 28 to 24
            fg="#2c3e50",
            bg="#f8f9fa"
        )
        title_label.pack()

        # Subtitle
        subtitle_label = tk.Label(
            title_frame,
            text="Alon van gelder and Boaz singer",
            font=("Segoe UI", 11, "italic"),  # Reduced font size from 13 to 11
            fg="#6c757d",
            bg="#f8f9fa"
        )
        subtitle_label.pack(pady=(5, 0))

        # Instructions label
        instructions_label = tk.Label(
            title_frame,
            text="Press F11 for full screen | Press Escape to exit full screen",
            font=("Segoe UI", 9),  # Reduced font size from 10 to 9
            fg="#6c757d",
            bg="#f8f9fa"
        )
        instructions_label.pack(pady=(3, 0))  # Reduced padding from 5 to 3

        # Separator line
        separator = tk.Frame(title_frame, height=2, bg="#dee2e6")
        separator.pack(fill=tk.X, pady=(8, 0))  # Reduced padding from 12 to 8

    def create_buttons_section(self, parent):
        """Create buttons with modern design"""
        buttons_frame = tk.Frame(parent, bg="#f8f9fa")
        buttons_frame.pack(expand=True, fill=tk.BOTH, pady=(15, 10))  # Reduced padding

        # Create a centered container for buttons
        button_container = tk.Frame(buttons_frame, bg="#f8f9fa")
        button_container.pack(expand=True)

        # Button configurations
        button_configs = [
            {
                "text": "Soldiers",
                "command": self.open_Soldiers,
                "bg_color": "#e3f2fd",
                "hover_color": "#bbdefb",
                "text_color": "#1976d2"
            },
            {
                "text": "Commander",
                "command": self.open_Commander,
                "bg_color": "#e8f5e8",
                "hover_color": "#c8e6c9",
                "text_color": "#388e3c"
            },
            {
                "text": "Participates",
                "command": self.open_Participates,
                "bg_color": "#fff3e0",
                "hover_color": "#ffe0b2",
                "text_color": "#f57c00"
            },
            {
                "text": "Mission",
                "command": self.open_Mission,
                "bg_color": "#e0f7fa",
                "hover_color": "#b2ebf2",
                "text_color": "#0097a7"
            },
            {
                "text": "Queries and Procedures",
                "command": self.open_queries_screen,
                "bg_color": "#f3e5f5",
                "hover_color": "#e1bee7",
                "text_color": "#7b1fa2"
            }
        ]

        # Smaller button spacing for better fit
        button_pady = 8  # Reduced from 15/10

        # Create buttons with proper spacing and centering
        for i, config in enumerate(button_configs):
            btn = StyledButton(
                button_container,
                text=config["text"],
                command=config["command"],
                bg_color=config["bg_color"],
                hover_color=config["hover_color"],
                text_color=config["text_color"]
            )
            btn.pack(pady=button_pady, padx=10)  # Reduced padx from 15 to 10

    def create_footer(self, parent):
        """Create footer section"""
        footer_frame = tk.Frame(parent, bg="#f8f9fa", height=40)  # Reduced height from 50 to 40
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))  # Reduced padding from 15 to 10
        footer_frame.pack_propagate(False)

        # Copyright text
        copyright_label = tk.Label(
            footer_frame,
            text="© 2025 Database Management System",
            font=("Segoe UI", 8),  # Reduced font size from 9 to 8
            fg="#6c757d",
            bg="#f8f9fa"
        )
        copyright_label.pack(pady=(8, 2))  # Reduced padding from (12, 3) to (8, 2)

        # Status frame
        status_frame = tk.Frame(footer_frame, bg="#f8f9fa")
        status_frame.pack()

        # Status indicator
        status_canvas = tk.Canvas(status_frame, width=10, height=10, bg="#f8f9fa", highlightthickness=0)  # Reduced size
        status_canvas.pack(side=tk.LEFT)
        status_canvas.create_oval(1, 1, 9, 9, fill="#28a745", outline="#28a745")

        status_label = tk.Label(
            status_frame,
            text="Ready to use system",
            font=("Segoe UI", 8),  # Reduced font size from 9 to 8
            fg="#6c757d",
            bg="#f8f9fa"
        )
        status_label.pack(side=tk.LEFT, padx=(3, 0))  # Reduced padding from 4 to 3

    def open_Soldiers(self):
        """Open client management screen"""
        try:
            from Soldiers import Soldiers
            Soldiers(self)
        except ImportError:
            messagebox.showinfo("הודעה", "מסך ניהול לקוחות יפתח כאן")

    def open_Commander(self):
        """Open service center management screen"""
        try:
            from Commander import Commander
            Commander(self)
        except ImportError:
            messagebox.showinfo("הודעה", "מסך מרכזי שירות יפתח כאן")

    def open_Participates(self):
        """Open product management screen"""
        try:
            from Participates import Participates
            Participates(self)
        except ImportError:
            messagebox.showinfo("הודעה", "מסך ניהול מוצרים יפתח כאן")

    def open_Mission(self):
        """Open queries screen"""
        try:
            from Mission import Mission
            Mission(self)
        except ImportError:
            messagebox.showinfo("הודעה", "מסך שאילתות ונהלים יפתח כאן")

    def open_queries_screen(self):
        """Open Table 4 screen"""
        try:
            from queries_screen import QueriesScreen
            QueriesScreen(self)
        except ImportError:
            messagebox.showinfo("הודעה", "Table 4 screen will open here.")

    def on_closing(self):
        """Handle window closing"""
        self.animation_running = False
        self.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()