class Profile:
    def __init__(self):
        self.name = "Akash Kunwar"
        self.tagline = "Constant repetition carries conviction"
        self.title = "Software Development Engineer"
        self.bio = (
            "Software Engineer at Digi Mantra Labs\n"
            "Works on USA-based client projects and Hyreworks (AI-powered hiring solution with project management)\n"
            "Expertise: MERN stack, SQL, Java, Cypress, Selenium\n"
            "Passionate about scalable solutions and AI/software innovations"
        )
        self.skills = {
            "Technical Skills": ["MERN Stack", "Java", "SQL", "Cypress", "Selenium"],
            "Non-Technical Skills": ["Content creation", "Storytelling", "Video editing"],
            "Core Strengths": ["Creating scalable solutions", "Turning dreams into code"]
        }
        self.experience = {
            "Company": "Digi Mantra Labs",
            "Position": "SDE",
            "Years of Experience": "1+ year",
            "Projects": ["Flight management system", "Automation test cases"]
        }
        self.social_links = {
            "LinkedIn": "https://www.linkedin.com/in/akashkunwaronline",
            "Twitter": "https://twitter.com/akashkunwar",
            "Instagram": "https://instagram.com/akashkunwar"
        }
        self.contact = {
            "Email": "akashkunwaronline@gmail.com",
            "Phone": "Your phone number here"
        }
        self.portfolio = {
            "YouTube Channel": "https://youtube.com/your-channel",
            "GitHub": "https://github.com/your-username"
        }
        self.design = {
            "Theme": "Dark theme (Blue and Black)",
            "Animations": "Yes, with a lot of effects",
            "Homepage Features": [
                "3D model of an animated college student with effects",
                "Intro section",
                "Animated sliding project cards"
            ]
        }

    def print_profile(self):
        print(f"Name: {self.name}")
        print(f"Tagline: {self.tagline}")
        print(f"Title: {self.title}\n")
        print("Bio:")
        print(self.bio)
        print("\nSkills:")
        for skill_type, skills_list in self.skills.items():
            print(f"{skill_type}: {', '.join(skills_list)}")
        print("\nExperience:")
        print(f"Company: {self.experience['Company']}")
        print(f"Position: {self.experience['Position']}")
        print(f"Years of Experience: {self.experience['Years of Experience']}")
        print(f"Projects: {', '.join(self.experience['Projects'])}")
        print("\nSocial Links:")
        for platform, link in self.social_links.items():
            print(f"{platform}: {link}")
        print("\nContact Details:")
        for method, value in self.contact.items():
            print(f"{method}: {value}")
        print("\nPortfolio:")
        for project, link in self.portfolio.items():
            print(f"{project}: {link}")
        print("\nDesign & Aesthetics:")
        print(f"Theme: {self.design['Theme']}")
        print(f"Animations: {self.design['Animations']}")
        print(f"Homepage Features: {', '.join(self.design['Homepage Features'])}")


# Create an instance of the Profile class
profile = Profile()

# Print the profile details to the console
profile.print_profile()
