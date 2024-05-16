# Changelog

All notable changes to this project will be documented in this file.


## 16.05.2024

### Task 4 Abstraction and Decomposition 
In our project, we apply abstraction and decomposition by organizing different modules responsible for distinct tasks.

For instance, in `merge_minutes.py`, we've created a class to merge data from various CSV files into a single CSV file.

Inside the class, we have different methods responsible for specific aspects of merging, such as reading, processing, merging, and writing the data. Then, a main function calls these methods to execute the merging process.

Another crucial file is `dashboard.py`, which generates the dashboard for data visualization.

Abstraction is implemented through a callback function that updates plots based on selected values. The implementation details are encapsulated within this function. It takes various inputs, processes them, and returns a list of plots.

We also use decomposition, as the complex task of updating plots is broken down into simpler tasks, such as selecting the subject, date range, and resolution, which are handled by separate functions.

In both files, docstring comments further abstract the functionality of methods and functions. These comments provide a high-level overview of each method or function's purpose.

### Added 
- Added the ability to display multiple users' data simultaneously in the visualizations.
- Introduced bar plots and line plots for better data representation and analysis, which can be accessed through the plotlib library.
- Improved error handling for data processing and plotting functionalities.

### Changed
- Enhanced the user interface for easier navigation between single and multiple user data views.

## 09.05.2025

### Added
- Initial release of the project with basic functionality.
- Manipulated dataset to prepare it for analysis and visualization.
- Added a basic Dashboard for data visualization with the plotlib library.
- Implemented functionality to display a specific user's data using the plotlib library.

### Fixed
- Fixed issues with dataset handling that affected graph generation.

##  02.05.2024

### Added
- Set up the initial project structure and version control.
- Added initial dataset manipulation scripts to clean and prepare data for analysis.

### Notes
- This is the first setup and there might be updates and bug fixes following based on user feedback and further testing.
