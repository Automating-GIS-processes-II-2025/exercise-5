from points_decorator import points

class TestProblem1:

    
    @points(5, "Problem 1: Did you save your map as a PNG file?")
    def test_problem_1_plot_file_exists(self,problem1):
        section_data, namespace = problem1
        OUTPUT_DIRECTORY = namespace['OUTPUT_DIRECTORY']

        png_files = list(OUTPUT_DIRECTORY.glob("*.png"))
        assert len(png_files) > 0

    @points(5, "Problem 1: Did you check that the PNG file is not empty?")
    def test_problem_1_plot_file_not_empty(self,problem1):
        section_data, namespace = problem1
        OUTPUT_DIRECTORY = namespace['OUTPUT_DIRECTORY']

        png_files = list(OUTPUT_DIRECTORY.glob("*.png"))
        for png_file in png_files:
            assert png_file.stat().st_size > 0


    
