# MSCS532 Assignment 1

## Overview
This repository contains the implementation of the Insertion Sort algorithm in Python, specifically sorting an array in monotonically decreasing order. The assignment also includes the setup of a Python environment and Visual Studio Code as the Integrated Development Environment (IDE).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Installation

1. **Python Installation**
   - Download and install Python version 3.8 or higher from the [official Python website](https://www.python.org/downloads).
   - Ensure to add Python to your PATH during installation.

2. **Visual Studio Code Installation**
   - Download and install Visual Studio Code from [VS Code's website](https://code.visualstudio.com/).
   - Install the official Python extension from the Extensions view.

3. **Clone this Repository**
   ```bash
   git clone https://github.com/your_username/MSCS532_Assignment1.git
## Usage
## To run the Insertion Sort program:

1. Open the terminal in VS Code.
2. Navigate to the cloned repository folder.
3. Run the following command:

python insertion_sort.py

## Example
The program sorts a sample array in monotonically decreasing order. Here’s a sample implementation in insertion_sort.py:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:  # Sorting in decreasing order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    insertion_sort(sample_array)
    print("Sorted array in decreasing order:", sample_array)
```


## Contributing
Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.




