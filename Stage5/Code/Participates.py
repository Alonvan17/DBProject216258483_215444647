import tkinter as tk
from tkinter import ttk, messagebox
from db_utils import connect
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
    """Styled button with hover effects"""

    def __init__(self, parent, text, command, bg_color="#ffffff", text_color="#333333",
                 hover_color="#f0f0f0", **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            bg=bg_color,
            fg=text_color,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=2,
            padx=15,
            pady=8,
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


class Participates(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Participates Management - Advanced System")
        self.configure(bg="#1a1a2e")

        # Set fullscreen by default
        self.state('zoomed')  # Windows
        # For Linux/Mac use: self.attributes('-zoomed', True)

        self.fullscreen_state = True

        # Enable fullscreen toggle
        self.bind('<F11>', self.toggle_fullscreen)
        self.bind('<Escape>', self.end_fullscreen)

        self.resizable(True, True)

        # Create main gradient background
        self.bg_canvas = GradientFrame(
            self,
            color1="#667eea",
            color2="#764ba2",
            highlightthickness=0
        )
        self.bg_canvas.pack(fill=tk.BOTH, expand=True)

        # Initialize particles
        self.particles = []
        self.animation_running = True
        self.after(100, self.init_particles)

        # Create main content
        self.create_main_content()

        # Start animation
        self.animate()

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode"""
        self.fullscreen_state = not self.fullscreen_state
        if self.fullscreen_state:
            self.state('zoomed')
        else:
            self.state('normal')
            self.geometry("1000x700")

    def end_fullscreen(self, event=None):
        """Exit fullscreen mode"""
        self.fullscreen_state = False
        self.state('normal')
        self.geometry("1000x700")

    def init_particles(self):
        """Initialize floating particles"""
        canvas_width = self.bg_canvas.winfo_width()
        canvas_height = self.bg_canvas.winfo_height()

        if canvas_width > 1 and canvas_height > 1:
            particle_count = max(10, int((canvas_width * canvas_height) / 25000))
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
                self.after(60, self.animate)
            except tk.TclError:
                pass

    def create_main_content(self):
        """Create the main application content"""
        # Main container frame
        main_container = tk.Frame(self.bg_canvas, bg="#ffffff", bd=2, relief="raised")
        main_container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.95)

        # Content frame
        content_frame = tk.Frame(main_container, bg="#f8f9fa")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title section
        self.create_title_section(content_frame)

        # Main content area with two columns
        main_area = tk.Frame(content_frame, bg="#f8f9fa")
        main_area.pack(fill=tk.BOTH, expand=True, pady=10)

        # Left column - Form
        left_frame = tk.Frame(main_area, bg="#ffffff", bd=1, relief="solid")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Right column - List and buttons
        right_frame = tk.Frame(main_area, bg="#ffffff", bd=1, relief="solid")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

        # Create form section
        self.create_form_section(left_frame)

        # Create list and buttons section
        self.create_list_section(right_frame)

        # Load initial data
        self.load_participates()

    def create_title_section(self, parent):
        """Create title section"""
        title_frame = tk.Frame(parent, bg="#f8f9fa")
        title_frame.pack(fill=tk.X, pady=(0, 15))

        # Main title
        title_label = tk.Label(
            title_frame,
            text="Participates Management",
            font=("Arial", 20, "bold"),
            fg="#2c3e50",
            bg="#f8f9fa"
        )
        title_label.pack()

        # Subtitle
        subtitle_label = tk.Label(
            title_frame,
            text="Mission and Unit participation system",
            font=("Arial", 11, "italic"),
            fg="#6c757d",
            bg="#f8f9fa"
        )
        subtitle_label.pack(pady=(5, 0))

        # Separator line
        separator = tk.Frame(title_frame, height=2, bg="#dee2e6")
        separator.pack(fill=tk.X, pady=(10, 0))

    def create_form_section(self, parent):
        """Create form section"""
        # Form header
        form_header = tk.Frame(parent, bg="#e3f2fd", height=40)
        form_header.pack(fill=tk.X)
        form_header.pack_propagate(False)

        header_label = tk.Label(
            form_header,
            text="Participation Details",
            font=("Arial", 12, "bold"),
            fg="#1976d2",
            bg="#e3f2fd"
        )
        header_label.pack(pady=10)

        # Form content
        form_content = tk.Frame(parent, bg="#ffffff")
        form_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.fields = {}
        field_labels = {
            "mid": "Mission ID",
            "unid": "Unit ID"
        }

        for i, (field, label) in enumerate(field_labels.items()):
            # Label
            label_widget = tk.Label(
                form_content,
                text=label,
                font=("Arial", 10, "bold"),
                fg="#333333",
                bg="#ffffff",
                anchor="e"
            )
            label_widget.grid(row=i, column=0, sticky='e', padx=(0, 10), pady=15)

            # Entry
            entry = tk.Entry(
                form_content,
                font=("Arial", 10),
                bg="#f8f9fa",
                fg="#333333",
                bd=1,
                relief="solid",
                width=25
            )
            entry.grid(row=i, column=1, sticky='ew', pady=15)
            self.fields[field] = entry

        # Configure grid weights
        form_content.grid_columnconfigure(1, weight=1)

        # Add combo boxes for better user experience
        self.create_dropdown_sections(form_content)

    def create_dropdown_sections(self, parent):
        """Create dropdown sections for missions and units"""
        # Mission dropdown section
        mission_frame = tk.Frame(parent, bg="#ffffff")
        mission_frame.grid(row=2, column=0, columnspan=2, sticky='ew', pady=10)

        tk.Label(
            mission_frame,
            text="Available Missions:",
            font=("Arial", 9, "bold"),
            fg="#666666",
            bg="#ffffff"
        ).pack(anchor='w')

        self.mission_combo = ttk.Combobox(
            mission_frame,
            font=("Arial", 9),
            width=30,
            state="readonly"
        )
        self.mission_combo.pack(fill=tk.X, pady=5)
        self.mission_combo.bind('<<ComboboxSelected>>', self.on_mission_select)

        # Unit dropdown section
        unit_frame = tk.Frame(parent, bg="#ffffff")
        unit_frame.grid(row=3, column=0, columnspan=2, sticky='ew', pady=10)

        tk.Label(
            unit_frame,
            text="Available Units:",
            font=("Arial", 9, "bold"),
            fg="#666666",
            bg="#ffffff"
        ).pack(anchor='w')

        self.unit_combo = ttk.Combobox(
            unit_frame,
            font=("Arial", 9),
            width=30,
            state="readonly"
        )
        self.unit_combo.pack(fill=tk.X, pady=5)
        self.unit_combo.bind('<<ComboboxSelected>>', self.on_unit_select)

        # Load dropdown data
        self.load_dropdowns()

    def load_dropdowns(self):
        """Load data for dropdown menus"""
        try:
            conn = connect()
            cur = conn.cursor()

            # Load missions
            cur.execute("SELECT mid, mdate FROM mission ORDER BY mid")
            missions = cur.fetchall()
            mission_values = [f"{row[0]} - {row[1]}" for row in missions]
            self.mission_combo['values'] = mission_values

            # Load units
            cur.execute("SELECT unid, uname FROM unit ORDER BY unid")
            units = cur.fetchall()
            unit_values = [f"{row[0]} - {row[1]}" for row in units]
            self.unit_combo['values'] = unit_values

            cur.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בטעינת נתונים: {str(e)}")

    def on_mission_select(self, event):
        """Handle mission selection"""
        selection = self.mission_combo.get()
        if selection:
            mid = selection.split(' - ')[0]
            self.fields["mid"].delete(0, tk.END)
            self.fields["mid"].insert(0, mid)

    def on_unit_select(self, event):
        """Handle unit selection"""
        selection = self.unit_combo.get()
        if selection:
            unid = selection.split(' - ')[0]
            self.fields["unid"].delete(0, tk.END)
            self.fields["unid"].insert(0, unid)

    def create_list_section(self, parent):
        """Create list and buttons section"""
        # List header
        list_header = tk.Frame(parent, bg="#e8f5e8", height=40)
        list_header.pack(fill=tk.X)
        list_header.pack_propagate(False)

        header_label = tk.Label(
            list_header,
            text="Participation List",
            font=("Arial", 12, "bold"),
            fg="#388e3c",
            bg="#e8f5e8"
        )
        header_label.pack(pady=10)

        # List content
        list_content = tk.Frame(parent, bg="#ffffff")
        list_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Listbox with scrollbar
        list_frame = tk.Frame(list_content, bg="#ffffff")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # Treeview for better display
        columns = ("mid", "unid", "mission_date", "unit_name")
        self.tree = ttk.Treeview(
            list_frame,
            columns=columns,
            show="headings",
            height=8
        )

        # Configure columns
        column_widths = {"mid": 100, "unid": 100, "mission_date": 120, "unit_name": 150}
        column_names = {
            "mid": "Mission ID",
            "unid": "Unit ID",
            "mission_date": "Mission Date",
            "unit_name": "Unit Name"
        }

        for col in columns:
            self.tree.heading(col, text=column_names[col])
            self.tree.column(col, width=column_widths[col], anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind treeview selection
        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        # Buttons section
        self.create_buttons_section(list_content)

    def create_buttons_section(self, parent):
        """Create buttons section"""
        buttons_frame = tk.Frame(parent, bg="#ffffff")
        buttons_frame.pack(fill=tk.X, pady=(10, 0))

        # Button configurations
        button_configs = [
            {"text": "Add", "command": self.add_participation, "bg_color": "#e3f2fd", "hover_color": "#bbdefb",
             "text_color": "#1976d2"},
            {"text": "Find", "command": self.find_and_load_participation, "bg_color": "#f3e5f5",
             "hover_color": "#e1bee7", "text_color": "#7b1fa2"},
            {"text": "Delete", "command": self.delete_participation, "bg_color": "#ffebee", "hover_color": "#ffcdd2",
             "text_color": "#d32f2f"},
            {"text": "Refresh", "command": self.load_participates, "bg_color": "#fff3e0", "hover_color": "#ffe0b2",
             "text_color": "#f57c00"},
            {"text": "Clear", "command": self.clear_form, "bg_color": "#f5f5f5", "hover_color": "#e0e0e0",
             "text_color": "#616161"},
            {"text": "Reload Lists", "command": self.load_dropdowns, "bg_color": "#e0f7fa", "hover_color": "#b2ebf2",
             "text_color": "#0097a7"},
        ]

        # Create buttons in a grid (3x2)
        for i, config in enumerate(button_configs):
            btn = StyledButton(
                buttons_frame,
                text=config["text"],
                command=config["command"],
                bg_color=config["bg_color"],
                hover_color=config["hover_color"],
                text_color=config["text_color"],
                width=12
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky='ew')

        # Configure grid weights
        for col in range(3):
            buttons_frame.grid_columnconfigure(col, weight=1)

    def find_and_load_participation(self):
        """Find and load participation by Mission ID and Unit ID"""
        mid = self.fields["mid"].get().strip()
        unid = self.fields["unid"].get().strip()

        if not mid and not unid:
            messagebox.showwarning("אזהרה", "יש להזין לפחות מספר משימה או מספר יחידה לחיפוש")
            return

        try:
            conn = connect()
            cur = conn.cursor()

            if mid and unid:
                # Search by both IDs
                cur.execute("""
                    SELECT p.mid, p.unid, m.mdate, u.uname 
                    FROM participates p
                    JOIN mission m ON p.mid = m.mid
                    JOIN unit u ON p.unid = u.unid
                    WHERE p.mid = %s AND p.unid = %s
                """, (mid, unid))
            elif mid:
                # Search by mission ID only
                cur.execute("""
                    SELECT p.mid, p.unid, m.mdate, u.uname 
                    FROM participates p
                    JOIN mission m ON p.mid = m.mid
                    JOIN unit u ON p.unid = u.unid
                    WHERE p.mid = %s
                """, (mid,))
            else:
                # Search by unit ID only
                cur.execute("""
                    SELECT p.mid, p.unid, m.mdate, u.uname 
                    FROM participates p
                    JOIN mission m ON p.mid = m.mid
                    JOIN unit u ON p.unid = u.unid
                    WHERE p.unid = %s
                """, (unid,))

            results = cur.fetchall()

            if results:
                # Clear tree first
                for item in self.tree.get_children():
                    self.tree.delete(item)

                # Add found records to tree
                for row in results:
                    formatted_row = tuple(str(value) if value is not None else '' for value in row)
                    self.tree.insert('', 'end', values=formatted_row)

                # Load first result into form if only one result
                if len(results) == 1:
                    self.fields["mid"].delete(0, tk.END)
                    self.fields["unid"].delete(0, tk.END)
                    self.fields["mid"].insert(0, str(results[0][0]))
                    self.fields["unid"].insert(0, str(results[0][1]))

                self.show_status_message(f"Found {len(results)} participation record(s)", "success")
            else:
                messagebox.showwarning("אזהרה", "לא נמצאו רשומות השתתפות")

            cur.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בחיפוש השתתפות: {str(e)}")

    def on_select(self, event):
        """Handle treeview selection"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            values = self.tree.item(item, 'values')
            if values:
                # Clear all fields first
                for field in self.fields.values():
                    field.delete(0, tk.END)
                # Fill fields with selected values
                self.fields["mid"].insert(0, str(values[0]))
                self.fields["unid"].insert(0, str(values[1]))

    def load_participates(self):
        """Load participates from database"""
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("""
                SELECT p.mid, p.unid, m.mdate, u.uname 
                FROM participates p
                JOIN mission m ON p.mid = m.mid
                JOIN unit u ON p.unid = u.unid
                ORDER BY p.mid, p.unid
            """)

            # Clear existing data
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Add data to treeview
            for row in cur.fetchall():
                # Convert None values to empty strings for better display
                formatted_row = tuple(str(value) if value is not None else '' for value in row)
                self.tree.insert('', 'end', values=formatted_row)

            cur.close()
            conn.close()

            # Show success message
            self.show_status_message("Data loaded successfully", "success")

        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בטעינת נתונים: {str(e)}")

    def add_participation(self):
        """Add new participation"""
        try:
            # Validate required fields
            mid = self.fields["mid"].get().strip()
            unid = self.fields["unid"].get().strip()

            if not mid or not unid:
                messagebox.showwarning("אזהרה", "יש להזין מספר משימה ומספר יחידה")
                return

            conn = connect()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO participates (mid, unid)
                VALUES (%s, %s)
            """, (mid, unid))
            conn.commit()
            cur.close()
            conn.close()

            # Clear form
            for field in self.fields.values():
                field.delete(0, tk.END)

            self.load_participates()
            self.show_status_message("Participation added successfully", "success")

        except Exception as e:
            error_msg = str(e).lower()
            if "duplicate" in error_msg or "unique" in error_msg:
                messagebox.showerror("שגיאה", "השתתפות זו כבר קיימת במערכת")
            elif "foreign key" in error_msg:
                messagebox.showerror("שגיאה", "מספר המשימה או היחידה לא קיים במערכת")
            else:
                messagebox.showerror("שגיאה", f"שגיאה בהוספת השתתפות: {str(e)}")

    def delete_participation(self):
        """Delete participation"""
        mid = self.fields["mid"].get().strip()
        unid = self.fields["unid"].get().strip()

        if not mid or not unid:
            messagebox.showwarning("אזהרה", "יש להזין מספר משימה ומספר יחידה למחיקה")
            return

        # Confirm deletion
        if messagebox.askyesno("אישור מחיקה", f"האם אתה בטוח שברצונך למחוק את ההשתתפות?\nמשימה: {mid}, יחידה: {unid}"):
            try:
                conn = connect()
                cur = conn.cursor()
                cur.execute("DELETE FROM participates WHERE mid = %s AND unid = %s", (mid, unid))

                if cur.rowcount > 0:
                    conn.commit()
                    self.load_participates()
                    self.show_status_message("Participation deleted successfully", "success")
                    for field in self.fields.values():
                        field.delete(0, tk.END)
                else:
                    messagebox.showwarning("אזהרה", "לא נמצאה השתתפות עם הפרטים הללו")

                cur.close()
                conn.close()

            except Exception as e:
                messagebox.showerror("שגיאה", f"שגיאה במחיקת השתתפות: {str(e)}")

    def clear_form(self):
        """Clear all form fields"""
        for field in self.fields.values():
            field.delete(0, tk.END)
        self.mission_combo.set('')
        self.unit_combo.set('')
        self.show_status_message("Form cleared", "success")

    def show_status_message(self, message, msg_type="info"):
        """Show status message"""
        # Create a temporary status label
        if hasattr(self, 'status_label'):
            self.status_label.destroy()

        color = "#28a745" if msg_type == "success" else "#6c757d"
        self.status_label = tk.Label(
            self.bg_canvas,
            text=message,
            font=("Arial", 10, "bold"),
            fg=color,
            bg="#ffffff",
            bd=1,
            relief="solid",
            padx=10,
            pady=5
        )
        self.status_label.place(relx=0.5, rely=0.95, anchor="center")

        # Remove after 3 seconds
        self.after(3000, lambda: self.status_label.destroy() if hasattr(self, 'status_label') else None)

    def on_closing(self):
        """Handle window closing"""
        self.animation_running = False
        self.destroy()