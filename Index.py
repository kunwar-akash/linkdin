import tkinter as tk

# Create a class for the profile
class ProfileGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Profile - Akash Kunwar")
        self.root.geometry("400x600")  # Window size
        # Create labels for each section
        self.name_label = tk.Label(root, text="Name: Akash Kunwar", font=("Arial", 14, "bold"))
        self.name_label.pack(pady=10)

        self.tagline_label = tk.Label(root, text="Tagline: Constant repetition carries conviction", font=("Arial", 12))
        self.tagline_label.pack(pady=10)

        self.title_label = tk.Label(root, text="Title: Software Development Engineer", font=("Arial", 12))
        self.title_label.pack(pady=10)

        self.bio_label = tk.Label(root, text="Bio: Software Engineer at Digi Mantra Labs", font=("Arial", 10))
        self.bio_label.pack(pady=10)

        self.skills_label = tk.Label(root, text="Skills: MERN Stack, Java, SQL, Cypress, Selenium", font=("Arial", 10))
        self.skills_label.pack(pady=10)

        self.social_label = tk.Label(root, text="Social Links: LinkedIn, Twitter, Instagram", font=("Arial", 10))
        self.social_label.pack(pady=10)

        self.contact_label = tk.Label(root, text="Contact: akashkunwaronline@gmail.com", font=("Arial", 10))
        self.contact_label.pack(pady=10)

# Create the main application window
root = tk.Tk()

# Create an instance of the ProfileGUI class
profile_app = ProfileGUI(root)

# Run the GUI application
root.mainloop()
