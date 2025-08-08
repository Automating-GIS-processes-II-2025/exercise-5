from points_decorator import points
import glob
import os

class TestProblem1:

   
    @points(5, "Problem 2: Did you save your map as a png file?")
    def test_problem_1_png_file_exists(self, problem1):
        
        png_files = glob.glob("docs/*.png", recursive=True)
        assert len(png_files) > 0

    @points(5, "Problem 2: Did you check that the png file is not empty?")
    def test_problem_1_png_file_not_empty(self, problem1):
        
        png_files = glob.glob("docs/*.png", recursive=True)
        
        # Check that each png file has content
        for png_file in png_files:
            assert os.path.getsize(png_file) > 0


    
