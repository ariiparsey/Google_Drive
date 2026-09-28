from Drive_Organizer import organize_classes



def test_organizer(tmp_path):
    # Create a temporary folder structure for testing
    tmp_path = tmp_path / "test_organize_classes"
    tmp_path.mkdir(parents=True, exist_ok=True)
    # Test files for different classes
    test_files = [ 
        tmp_path / "Math150_Assignment1.pdf",
        tmp_path / "Math150_Assignment2.pdf",
        tmp_path / "Cst_Essay.docx",
        tmp_path / "Cst_Notes.txt",

    ]

    # Create the test files
    for file in test_files:
        file.touch()

    # Call the organize_classes function
    organize_classes(tmp_path)
    print(list(tmp_path.rglob("*")))

    assert (tmp_path / "MATH_150" / "Daily Assignments" / "Math150_Assignment1.pdf").exists()
    assert (tmp_path / "MATH_150" / "Daily Assignments" / "Math150_Assignment2.pdf").exists()
    assert (tmp_path / "CST_286" / "Papers" / "Cst_Essay.docx").exists()
    assert (tmp_path / "CST_286" / "Daily Assignments" / "Cst_Notes.txt").exists()
