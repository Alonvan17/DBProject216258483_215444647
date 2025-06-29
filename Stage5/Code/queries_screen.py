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
                 hover_color="#f0f0f0", width=30, **kwargs):
        # Configure button style
        super().__init__(
            parent,
            text=text,
            command=command,
            bg=bg_color,
            fg=text_color,
            font=("Segoe UI", 10, "bold"),  # קטנתי את הפונט
            relief="flat",
            bd=2,
            padx=12,
            pady=8,
            width=width,
            height=1,
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
        self.vx = (random.random() - 0.5) * 1.0
        self.vy = (random.random() - 0.5) * 1.0
        self.size = int(random.random() * 2) + 1

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


class QueriesScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Queries and Procedures - Advanced Management System")
        self.configure(bg="#1a1a2e")
        self.resizable(True, True)

        # Set to fullscreen automatically
        self.state('zoomed')  # Windows

        self.minsize(900, 650)

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

        # Initialize input widgets
        self.input_widgets = {}
        self.input_frame = None

        # Wait for canvas to be drawn before initializing particles
        self.after(100, self.init_particles)

        # Create main content
        self.create_main_content()

        # Start animation loop
        self.animate()

        # Handle window closing and add ESC key to exit fullscreen
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind('<Escape>', self.toggle_fullscreen)
        self.bind('<F11>', self.toggle_fullscreen)

    def center_window(self):
        """Center the window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (1000 // 2)
        y = (self.winfo_screenheight() // 2) - (700 // 2)
        self.geometry(f"1000x700+{x}+{y}")

    def init_particles(self):
        """Initialize floating particles"""
        canvas_width = self.bg_canvas.winfo_width()
        canvas_height = self.bg_canvas.winfo_height()

        if canvas_width > 1 and canvas_height > 1:
            for _ in range(12):
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
                self.after(80, self.animate)
            except tk.TclError:
                # Handle case where window is destroyed
                pass

    def create_main_content(self):
        """Create the main application content"""
        # Main container frame
        main_container = tk.Frame(self.bg_canvas, bg="#ffffff", bd=2, relief="raised")
        main_container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.88, relheight=0.88)

        # Create content frame
        content_frame = tk.Frame(main_container, bg="#f8f9fa")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)

        # Title section
        self.create_title_section(content_frame)

        # Create two-column layout
        main_layout = tk.Frame(content_frame, bg="#f8f9fa")
        main_layout.pack(fill=tk.BOTH, expand=True, pady=(20, 0))

        # Left side - buttons
        buttons_frame = tk.Frame(main_layout, bg="#f8f9fa", width=400)
        buttons_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        buttons_frame.pack_propagate(False)

        # Right side - results
        results_frame = tk.Frame(main_layout, bg="#f8f9fa")
        results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create buttons and results sections
        self.create_buttons_section(buttons_frame)
        self.create_results_section(results_frame)

    def create_title_section(self, parent):
        """Create title section"""
        title_frame = tk.Frame(parent, bg="#f8f9fa")
        title_frame.pack(fill=tk.X, pady=(0, 15))

        # Main title
        title_label = tk.Label(
            title_frame,
            text="Queries and Procedures",
            font=("Segoe UI", 22, "bold"),
            fg="#2c3e50",
            bg="#f8f9fa"
        )
        title_label.pack()

        # Subtitle
        subtitle_label = tk.Label(
            title_frame,
            text="Queries and Stored Procedures Management",
            font=("Segoe UI", 11, "italic"),
            fg="#6c757d",
            bg="#f8f9fa"
        )
        subtitle_label.pack(pady=(3, 0))

        # Separator line
        separator = tk.Frame(title_frame, height=2, bg="#dee2e6")
        separator.pack(fill=tk.X, pady=(10, 0))

    def create_buttons_section(self, parent):
        """Create buttons section"""
        # Section title
        queries_title = tk.Label(
            parent,
            text="Queries",
            font=("Segoe UI", 14, "bold"),
            fg="#495057",
            bg="#f8f9fa"
        )
        queries_title.pack(pady=(5, 10))

        # Query buttons
        query_configs = [
            {
                "text": "q1: Most sea vessels by base",
                "command": self.query_base_most_vessels,
                "bg_color": "#e3f2fd",
                "hover_color": "#bbdefb",
                "text_color": "#1976d2"
            },
            {
                "text": "q2: Expiring ships < 6 months",
                "command": self.query_expiring_leases,
                "bg_color": "#e8f5e8",
                "hover_color": "#c8e6c9",
                "text_color": "#388e3c"
            }
        ]

        for config in query_configs:
            btn = StyledButton(
                parent,
                text=config["text"],
                command=config["command"],
                bg_color=config["bg_color"],
                hover_color=config["hover_color"],
                text_color=config["text_color"],
                width=32
            )
            btn.pack(pady=5, padx=10)

        # Separator
        sep_frame = tk.Frame(parent, height=1, bg="#dee2e6")
        sep_frame.pack(fill=tk.X, pady=12, padx=20)

        # Procedures section title
        proc_title = tk.Label(
            parent,
            text="Function and Procedure",
            font=("Segoe UI", 14, "bold"),
            fg="#495057",
            bg="#f8f9fa"
        )
        proc_title.pack(pady=(5, 10))

        proc_configs = [
            {
                "text": "procedure: Auto Assign Crewmate",
                "command": self.run_proc_auto_assign_crewmate,
                "bg_color": "#fff3e0",
                "hover_color": "#ffe0b2",
                "text_color": "#f57c00"
            }
        ]

        for config in proc_configs:
            btn = StyledButton(
                parent,
                text=config["text"],
                command=config["command"],
                bg_color=config["bg_color"],
                hover_color=config["hover_color"],
                text_color=config["text_color"],
                width=32
            )
            btn.pack(pady=5, padx=10)

        # Function button
        func_btn = StyledButton(
            parent,
            text="function: Commander Performance",
            command=self.run_func_commander_performance,
            bg_color="#f3e5f5",
            hover_color="#e1bee7",
            text_color="#7b1fa2",
            width=32
        )
        func_btn.pack(pady=5, padx=10)

        # Clear results button
        clear_btn = StyledButton(
            parent,
            text="Clear results",
            command=self.clear_results,
            bg_color="#f5f5f5",
            hover_color="#e0e0e0",
            text_color="#424242",
            width=32
        )
        clear_btn.pack(pady=(15, 10), padx=10)

    def create_results_section(self, parent):
        """Create results display section"""
        results_title = tk.Label(
            parent,
            text="Query output",
            font=("Segoe UI", 14, "bold"),
            fg="#495057",
            bg="#f8f9fa"
        )
        results_title.pack(pady=(10, 10))

        # Create text widget with scrollbar in a frame
        text_frame = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

        # Text widget with custom styling
        self.text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg="#ffffff",
            fg="#212529",
            relief="flat",
            bd=0,
            padx=15,
            pady=15,
            selectbackground="#007bff",
            selectforeground="#ffffff"
        )

        # Scrollbar
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=scrollbar.set)

        # Pack text and scrollbar
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Initial message
        self.text.insert(tk.END, "Welcome to the query system!\n")
        self.text.insert(tk.END, "Select a query or procedure to run...\n\n")
        self.text.configure(state=tk.DISABLED)

    def create_input_form(self, fields):
        """Create input form in the results area"""
        self.text.configure(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)

        # הוראות מעל הטופס
        self.text.insert(tk.END, "📝 Please provide the following parameters:\n")
        self.text.insert(tk.END, "• Soldier ID (numeric)\n")
        self.text.insert(tk.END, "• Commander ID (numeric)\n")
        self.text.insert(tk.END, "• Crew Type (text)\n\n")

        # מסגרת הטופס
        self.input_frame = tk.Frame(self.text, bg="#ffffff", bd=1, relief="solid")
        self.input_frame.configure(highlightbackground="#ced4da", highlightthickness=1)
        self.input_frame.config(padx=20, pady=20)
        self.input_widgets.clear()

        style_font = ("Segoe UI", 10)
        label_fg = "#495057"
        entry_bg = "#f8f9fa"
        entry_bd = 1
        entry_relief = "flat"

        for i, (field_name, field_type) in enumerate(fields):
            # Label
            label = tk.Label(
                self.input_frame,
                text=f"{field_name}:",
                font=("Segoe UI", 10, "bold"),
                bg="#ffffff",
                fg=label_fg
            )
            label.grid(row=i, column=0, sticky="w", pady=8, padx=(0, 10))

            # Entry styled
            entry = tk.Entry(
                self.input_frame,
                font=style_font,
                bg=entry_bg,
                relief=entry_relief,
                bd=entry_bd,
                highlightthickness=1,
                highlightbackground="#ced4da",
                highlightcolor="#80bdff",
                insertbackground="#212529",
                width=28
            )
            entry.grid(row=i, column=1, sticky="ew", pady=8)
            self.input_widgets[field_name] = entry

        self.input_frame.grid_columnconfigure(1, weight=1)

        # כפתור ביצוע
        execute_btn = StyledButton(
            self.input_frame,
            text="Execute Procedure",
            command=self.execute_procedure,
            bg_color="#28a745",
            hover_color="#218838",
            text_color="#ffffff",
            width=24
        )
        execute_btn.grid(row=len(fields), column=0, columnspan=2, pady=(20, 5))

        self.text.window_create(tk.END, window=self.input_frame)
        self.text.insert(tk.END, "\n" + "=" * 50 + "\n")
        self.text.configure(state=tk.DISABLED)

    def execute_procedure(self):
        """Execute the procedure with the entered parameters"""
        try:
            # Get values from input widgets
            soldier_id_str = self.input_widgets["Soldier ID"].get().strip()
            commander_id_str = self.input_widgets["Commander ID"].get().strip()
            crew_type = self.input_widgets["Crew Type"].get().strip()

            # Validate inputs
            if not soldier_id_str or not commander_id_str or not crew_type:
                self.display_error("Please fill in all fields")
                return

            try:
                soldier_id = int(soldier_id_str)
                commander_id = int(commander_id_str)
            except ValueError:
                self.display_error("Soldier ID and Commander ID must be numeric values")
                return

            # Execute the procedure
            conn = connect()
            cur = conn.cursor()
            cur.execute("CALL pr_auto_assign_crewmate(%s, %s, %s)", (soldier_id, commander_id, crew_type))
            conn.commit()
            cur.close()
            conn.close()

            # Display success message
            self.display_results("Procedure: Auto Assign Crewmate - SUCCESS",
                                 f"Crewmate auto assignment procedure executed successfully!\n\n"
                                 f"Parameters used:\n"
                                 f"• Soldier ID: {soldier_id}\n"
                                 f"• Commander ID: {commander_id}\n"
                                 f"• Crew Type: {crew_type}\n\n"
                                 f"The procedure has been executed and the database has been updated.")

        except Exception as e:
            self.display_error(f"Error executing procedure: {str(e)}")

    def display_error(self, error_message):
        """Display error message in the results area"""
        self.text.configure(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, "=== ERROR ===\n\n")
        self.text.insert(tk.END, error_message)
        self.text.insert(tk.END, "\n\n" + "=" * 50 + "\n")
        self.text.configure(state=tk.DISABLED)

    def clear_results(self):
        """Clear the results text area"""
        self.text.configure(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, "The results have been cleared.\n")
        self.text.insert(tk.END, "Select a query or procedure to run...\n\n")
        self.text.configure(state=tk.DISABLED)

        # Clear input widgets
        self.input_widgets.clear()
        if self.input_frame:
            self.input_frame.destroy()
            self.input_frame = None

    def display_results(self, title, data):
        """Display results in the text widget"""
        self.text.configure(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)

        # Title
        self.text.insert(tk.END, f"=== {title} ===\n\n")

        # Data
        if isinstance(data, list):
            if data:
                for i, row in enumerate(data, 1):
                    if isinstance(row, tuple):
                        self.text.insert(tk.END, f"{i}. {' - '.join(str(item) for item in row)}\n")
                    else:
                        self.text.insert(tk.END, f"{i}. {row}\n")
                self.text.insert(tk.END, f"\nTotal found: {len(data)} results.")
            else:
                self.text.insert(tk.END, "No results found.")
        else:
            self.text.insert(tk.END, str(data))

        self.text.insert(tk.END, "\n\n" + "=" * 50 + "\n")
        self.text.configure(state=tk.DISABLED)

    def query_base_most_vessels(self):
        """Execute query 1: Find the base with the most sea vessels"""
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("""
                SELECT b.base_ID, b.location, COUNT(sv.sea_ID) AS vessel_count
                FROM Base b
                JOIN Sea_vessel sv ON b.base_ID = sv.base_ID
                GROUP BY b.base_ID, b.location
                ORDER BY vessel_count DESC
                FETCH FIRST 1 ROWS ONLY
            """)
            rows = cur.fetchall()
            cur.close()
            conn.close()

            if rows:
                # Format the results nicely
                formatted_results = []
                for row in rows:
                    base_id, location, vessel_count = row
                    formatted_results.append(f"Base ID: {base_id}, Location: {location}, Vessel Count: {vessel_count}")

                self.display_results("Base with Most Sea Vessels", formatted_results)
            else:
                self.display_results("Base with Most Sea Vessels", "No data found")

        except Exception as e:
            messagebox.showerror("Error", f"Error executing query:\n{str(e)}")

    def query_expiring_leases(self):
        """Execute query 2: List ships with leases expiring in less than 6 months"""
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    sea_ID, nickname, lease_expiration_date,
                    EXTRACT(YEAR FROM lease_expiration_date) AS exp_year,
                    EXTRACT(MONTH FROM lease_expiration_date) AS exp_month
                FROM Sea_vessel
                WHERE lease_expiration_date IS NOT NULL
                  AND lease_expiration_date < CURRENT_DATE + INTERVAL '6 months'
            """)
            rows = cur.fetchall()
            cur.close()
            conn.close()

            if rows:
                # Format the results nicely
                formatted_results = []
                for row in rows:
                    sea_id, nickname, exp_date, exp_year, exp_month = row
                    formatted_results.append(
                        f"Sea ID: {sea_id}, Nickname: {nickname}, "
                        f"Expiration: {exp_date}, Year: {exp_year}, Month: {exp_month}"
                    )

                self.display_results("Ships with Expiring Leases (Less than 6 months)", formatted_results)
            else:
                self.display_results("Ships with Expiring Leases (Less than 6 months)",
                                     "No ships found with leases expiring in the next 6 months")

        except Exception as e:
            messagebox.showerror("Error", f"Error executing query:\n{str(e)}")

    def run_proc_auto_assign_crewmate(self):
        """Execute procedure to auto assign crewmate - now with inline input"""
        # Define the input fields needed
        fields = [
            ("Soldier ID", "int"),
            ("Commander ID", "int"),
            ("Crew Type", "str")
        ]

        # Create the input form
        self.create_input_form(fields)

    def run_func_commander_performance(self):
        """Execute function to get commander performance"""
        try:
            conn = connect()
            cur = conn.cursor()

            # Call the function that returns a refcursor
            cur.execute("SELECT fn_commander_performance()")
            cursor_name = cur.fetchone()[0]

            # Fetch from the returned cursor
            cur.execute(f"FETCH ALL FROM \"{cursor_name}\"")
            results = cur.fetchall()

            cur.close()
            conn.close()

            if results:
                # Format the results nicely
                formatted_results = []
                for row in results:
                    commander_id, num_tanks, num_missions, experience_level = row
                    formatted_results.append(
                        f"Commander ID: {commander_id}, Tanks: {num_tanks}, "
                        f"Missions: {num_missions}, Experience: {experience_level}"
                    )

                self.display_results("Function: Commander Performance", formatted_results)
            else:
                self.display_results("Function: Commander Performance", "No commander performance data found")

        except Exception as e:
            messagebox.showerror("Error", f"Error executing function:\n{str(e)}")

    def toggle_fullscreen(self, event=None):
        """Toggle between fullscreen and windowed mode"""
        try:
            # Check current state and toggle
            if self.state() == 'zoomed':
                self.state('normal')
                self.geometry("1000x700")
                self.center_window()
            else:
                self.state('zoomed')
        except:
            # Fallback method for different systems
            current_state = self.attributes('-fullscreen')
            self.attributes('-fullscreen', not current_state)

    def on_closing(self):
        """Handle window closing"""
        self.animation_running = False
        self.destroy()