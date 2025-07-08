from points_decorator import points

class TestProblem1:

    @points(0,"NOTE! The tests in this exercise simply test that you have completed the assignment, final grading is provided by the course teachers")
    @points(5, "Problem 1: Did you save your map as a PNG file?")
    def test_problem_2_plot_file_exists(self,problem2):
        section_data, namespace = problem2
        DATA_DIRECTORY = namespace['DATA_DIRECTORY']

        png_files = list(DATA_DIRECTORY.glob("*.png"))
        assert len(png_files) > 0

    @points(5, "Problem 1: Did you check that the PNG file is not empty?")
    def test_problem_2_plot_file_not_empty(self,problem2):
        section_data, namespace = problem2
        DATA_DIRECTORY = namespace['DATA_DIRECTORY']

        png_files = list(DATA_DIRECTORY.glob("*.png"))
        for png_file in png_files:
            assert png_file.stat().st_size > 0


    