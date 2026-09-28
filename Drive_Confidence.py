from pathlib import Path #locations
import shutil #file operations
import re # searches for patterns in text
from dataclasses import dataclass # creates classes for
import argparse # command line arguments
from __future__ import annotations # allows for type hinting of classes that are defined later in the code



#Rules
 # ↓
#Clean filename
 # ↓
#Find matching keywords
 # ↓
#Calculate confidence score
 # ↓
#Preview or move file

Drive_Path = Path(r"H:\My Drive")

review_cutoff = 80 # Confidence score threshold

# Organizing Rules

course_rules = {
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

@dataclass 
class Match:
    class_name: str | None
    score: int
    matched_keywords: list[str]
    runner_up_score: int = 0

    @property
    def confidence(self) -> int:
        if self.name is None:
            return "none"
        if self.score >= 90:
            return "high"
        if self.score >= review_cutoff:
            return "medium"
        return "low"



def punctuate(text: str) -> str:
    # Remove special characters and convert to lowercase
    return re.sub(r"[^a-zA-Z0-9]+", " ", text.lower()).strip()

def keyword_matches(text: str, keyword: str) -> bool:
    text = punctuate(text)
    keyword= punctuate(keyword)


    return bool(
        # ensures that the keyword is not part of a larger word by using negative lookbehind and negative lookahead assertions
        re.search(rf"(?<!\w){re.escape(keyword)}(?!\w)", text)  
    )


 # decides where the file should be moved based on the confidence score and matched keywords/ rules
 # rules being dicts of categories and keyword pairs
def confidence_score_rules(text: str, rules:  dict[str, list[str]]) -> Match: # "subject", score, matched keywords, runner up score
    candidates = []

    for class_name, keywords in rules.items():  #rules.items pulls dict key value pairs and iterates through them
        matched_keywords = [
            keyword for keyword in keywords if keyword_matches(text, keyword)
        ]

        if not matched_keywords:
            candidates.append((class_name, 0, []))
            continue
        








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
        for class_folder, keywords in course_rules.items():
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