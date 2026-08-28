# BMI Calculator (Python) - Version 2.0

A lightweight, robust, and highly efficient command-line application built in Python to calculate Body Mass Index (BMI), classify weight categories according to World Health Organization (WHO) standards, and provide personalized healthy weight ranges.

## Features & Improvements in v2.0
* **Algorithmic Efficiency:** Strict \(\mathcal{O}(1)\) Time Complexity and \(\mathcal{O}(1)\) Space Complexity.
* **WHO Standard Classification:** Standardized categories (Underweight, Normal weight, Overweight, Obese Class I/II/III).
* **Ideal Weight Span Estimation:** Automatically calculates the recommended healthy weight range for the user's height.
* **Input Validation & Resilience:** Robust protection against invalid entries (non-numeric, zero, negative, out-of-range inputs) and graceful termination on `Ctrl+C` (`KeyboardInterrupt`).
* **Clean Code & Modularity:** Fully typed (PEP 484), docstring-documented (PEP 257), and structured into reusable, testable functions.
* **Automated Unit Tests:** Built-in test suite covering calculations, boundary conditions, and exception cases.

## Algorithmic Complexity
* **Time Complexity:** \(\mathcal{O}(1)\) — Constant-time mathematical computations and fixed-size threshold lookups.
* **Space Complexity:** \(\mathcal{O}(1)\) — Minimal constant memory footprint with zero allocations on heap structures.

## How It Works
BMI is calculated using the standard metric formula:
\[\text{BMI} = \frac{\text{weight in kilograms}}{(\text{height in meters})^2}\]

## Getting Started

### Prerequisites
* Python 3.8 or higher

### Running the Application
```bash
python BMI.py
```

### Running Tests
```bash
python -m unittest test_bmi.py -v
```

## Example Usage
```text
=============================================
       BMI CALCULATOR - VERSION 2.0
=============================================
Enter your height in meters (e.g., 1.75): 1.75
Enter your weight in kilograms (e.g., 70.0): 70

---------------------------------------------
                  RESULTS
---------------------------------------------
 Height           : 1.75 m
 Weight           : 70.00 kg
 Calculated BMI   : 22.86
 Health Category  : Normal weight
 Ideal Weight Span: 56.7 kg - 76.3 kg
---------------------------------------------
```

## License
This project is open-source and available under the [MIT License](LICENSE).
