# first-scripts
"My personal coding workspace and daily Python practice scripts. Building my path towards remote international tech roles."
The Ultimate Lightweight Fitness & Nutrition Suite"

🚀 1. Executive Summary & Vision
Calory is a high-performance, lightweight Command Line Interface (CLI) application built for fitness enthusiasts. Its primary objective is to streamline daily health tracking—covering calories, macronutrients, hydration, and physical activity—directly in the terminal without the clutter of heavy, over-engineered graphical user interfaces. Built entirely in Python, it demonstrates clean software architecture, modular functions, and robust control loops.

🧩 2. Core Architecture & Features Breakdown
The application is driven by a central, interactive Main Menu System (while True loop) that seamlessly routes users through three core tracking modules:

🔹 Module 1: Calorie & Macro Tracker (calorie_tracker)
Dynamic Calorie Target Loop: Prompts the user for their daily caloric intake. If the target is unfulfilled, it calculates the precise deficit and allows users to log extra meals dynamically until the goal is met.

Automated Macro Breakdown: Once the caloric target is secured, it instantly computes a science-backed nutrient distribution:

Protein: 30% of total calories (converted to grams at 4 kcal/g)

Carbs: 40% of total calories (converted to grams at 4 kcal/g)

Fats: 30% of total calories (converted to grams at 9 kcal/g)

Clean Formatting: Renders clean, precise terminal metrics using formatted float outputs (.1f).

🔹 Module 2: Step Counter & Distance Tracker (total_step_taken)
Progressive Step Goal Loop: Enforces step goals (e.g., a 3,000-step baseline) by interactively prompting for remaining steps until the target is successfully cleared.

Automated Metrics Calculation:

Calorie Burn: Automatically evaluates approximate calories burned based on step intervals (0.4 kcal per 10 steps).

Distance Traveled: Converts total steps into covered distance in meters (steps * 0.5m).

🔹 Module 3: Hydration Tracker (total_water_intake)
Live Water Intake Logging: Tracks consumed fluids in milliliters.

Interactive Deficit Tracking: Dynamically calculates remaining hydration goals until the target (e.g., 3,000ml) is reached, providing real-time feedback loops.

⚙️ 3. Technical Highlights
Modular Design: Each health parameter is isolated into its own encapsulated, reusable function, adhering to clean code standards.

Persistent Control Loop (main()): Ensures the application loops smoothly back to the main menu after executing tasks, preventing crashes or unexpected exits until the user explicitly selects the exit option.

Zero Bloatware: Built using core Python standard libraries (input, print, while, if-elif) ensuring blazing-fast execution speeds and zero external dependencies.

🎯 Conclusion
Calory is more than just a script—it bridges the gap between software development logic and real-world health optimization. It provides a fast, efficient, and distraction-free way to maintain daily discipline.
