# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
from pathlib import Path

# Create a new folder
screenshot_dir = Path.home() / "Desktop" / "Screenshots"
screenshot_dir.mkdir(exist_ok=True)

# Find the path to my Desktop
desktop = Path.home() / "Desktop"
for filepath in desktop.iterdir():
    # Filter for screenshots only
    if (filepath.suffix == ".png" and str(filepath.name).startswith("Screenshot")):
        print(f"Found: {filepath}")

        # Create a new path for each file
        new_path = Path(screenshot_dir / filepath.name)

        # Move the screenshot there
        print(f"Moving to: {new_path}...")
        filepath.replace(new_path)
        print(f"Moved.")
