import os
import shutil
from pathlib import Path

Drive_Path = Path(r"H:\My Drive")

# Organizing Rules

Classes = {
    "HCOM_110": ["hcom", "communication", "intro to communication"],
    "FYS_145": [ "first year seminar", "first year", "seminar", "fys"],
    "CST_286": ["cst", "comp", "programming", "computer physics"],
    "MATH_150": ["math", "calc", "calculus", "trig", "algebra", "geometry"]
}

Assignment_types = {
    "Daily Assignments": ["daily","writing", "homework", "hw", "assignments", "notes", "assignment", "monday", "tuesday", "wednesday", "thursday", "friday"],
    "Labs": ["lab", "report", "experiment", "project"],
    "Tests/Study info": ["test", "exam", "study", "quiz", "assessment"],
    "Papers": ["paper", "essay", "research", "thesis", "draft", "outline"]
}


#Scan and route files to class folders
def organize_classes(target_directory: Path):
    if not target_directory.exists():
        return
    for item in target_directory.iterdir():
        if item.is_dir():
            continue


        filename_lower = item.name.lower()
        matched_class = None
        matched_category = None

        # matching classes by searching for the keyword, assigning the variables the match if accurate 
        for class_folder, keywords in Classes.items():
            if any(keyword in filename_lower for keyword in keywords):
                matched_class = class_folder 
                break

        # match assignment type to category
        for category, keywords in Assignment_types.items():
            if any(keyword in filename_lower for keyword in keywords):
                matched_category = category
                break


        if matched_class:
            if not matched_category:
                matched_category = "Daily Assignments"  # Default category if none matched


        # Target folder path for the matched class and category
         
            destination_folder = target_directory / matched_class / matched_category
        
            destination_folder.mkdir(parents=True, exist_ok=True)

            destination_file_path = destination_folder / item.name

        # Move the file to the destination folder
            shutil.move(str(item), str(destination_file_path))
        else:
            print(f"No class matched for file: {item.name}.")



if __name__ == "__main__":
    organize_classes(Drive_Path)