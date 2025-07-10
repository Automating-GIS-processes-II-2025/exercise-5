from points_decorator import points
import os
import glob

class TestProblem2:


    @points(5, "Problem 2: Did you save your interactive map as a HTML file?")
    def test_problem_2_plot_file_exists(self,problem2):
        section_data, namespace = problem2
        DATA_DIRECTORY = namespace['DATA_DIRECTORY']

        png_files = list(DATA_DIRECTORY.glob("*.html"))
        assert len(png_files) > 0

    @points(5, "Problem 2: Did you check that the HTML file is not empty?")
    def test_problem_2_plot_file_not_empty(self, problem2):
        # Look for HTML files in the current working directory and subdirectories
        html_files = glob.glob("docs/*.html", recursive=True)
        
        # Check that each HTML file has content
        for html_file in html_files:
            assert os.path.getsize(html_file) > 0


    
