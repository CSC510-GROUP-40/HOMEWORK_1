[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: Apache-2-License](https://img.shields.io/badge/Licence-Apache--2--Licence-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-yellow.svg)](https://www.linux.org/)
[![Quadratic Equation Test](https://github.com/CSC510-GROUP-HLL/HOMEWORK_1/actions/workflows/main.yml/badge.svg)](https://github.com/CSC510-GROUP-HLL/HOMEWORK_1/actions/workflows/main.yml)
[![Coverage Status](https://coveralls.io/repos/github/CSC510-GROUP-HLL/HOMEWORK_1/badge.svg?branch=main)](https://coveralls.io/github/CSC510-GROUP-HLL/HOMEWORK_1?branch=main)


# Homework 1 - Quadratic Equation Solver

## Overview
This assignment involves creating a Python program that solves quadratic equations of the form:

$$ ax^2 + bx + c = 0 $$

where `a`, `b`, and `c` are real numbers, and `a` is not equal to 0. The program will calculate the roots of the quadratic equation using the quadratic formula:

$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

The program should handle all possible scenarios:
- Two distinct real roots
- One real root (a double root)
- No real roots (complex roots)

## Objectives

1. Implement a function to calculate the roots of a quadratic equation in the main file.
2. Handle edge cases, including:
   - Coefficient `a` is zero (which would make it a linear equation, not handled in this version).
   - The discriminant $b^2 - 4ac$ is negative, resulting in complex roots.
3. Write test cases in a separate test file to validate the solver function.

## File Structure

- `main.py`: The main file containing the implementation of the quadratic equation solver.
- `test_main.py`: A separate test file containing test cases for validating the solver function using `pytest`.

## Getting Started

### Prerequisites

- Python 3.13
- `pytest` for running the test cases

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CSC510-GROUP-HLL/HOMEWORK_1.git
   cd HOMEWORK_1
2. Install Dependencies: Install pytest for running test cases.

### Usage
To use the Quadratic Equation Solver, run the main program with the following command:
python3.13 main.py

Enter the following 

Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: 2
The roots are: (2.0, 1.0)

To Check for Test Cases, run pytest

### Contributing
Contributions to the Quadratic Equation Solver are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request. You can also open an issue to discuss your ideas.

To Contribute
- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes and commit them (git commit -m 'Add some feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.

### License
This project is licensed under the Apache License 2.0 See the LICENSE file for more details.

### Contact Information
In case of any issues, please raise an issue on this repository.<br> Our team of developers monitors the issues and would be happy to answer any and all questions you have about this project!
