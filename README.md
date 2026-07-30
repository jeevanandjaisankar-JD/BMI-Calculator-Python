# Simple BMI Calculator

A lightweight command-line interface (CLI) application built in Python to calculate Body Mass Index (BMI) and determine weight categories based on standard metric measurements.

## Features
* **Instant calculation:** Computes BMI instantly from user input.
* **Health classification:** Categorizes results automatically (Underweight, Normal, Overweight, Obese).
* **High precision:** Outputs results rounded to two decimal places.
* **No external dependencies:** Runs purely on standard Python libraries.

## How It Works
The script collects height (meters) and weight (kilograms) to compute BMI using the standard mathematical formula:
\[\text{BMI} = \frac{\text{weight in kilograms}}{\text{height in meters}^2}\]

## Requirements
* Python 3.x

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project folder:
   ```bash
   cd your-repo-name
   ```
3. Run the script:
   ```bash
   python bmi_calculator.py
   ```

## Example Usage
```text
Enter your height in meters: 1.75
Enter your weight in kilograms: 70

Your BMI is: 22.86
Category: Normal weight
```

## License
This project is open-source and available under the [MIT License](LICENSE).
