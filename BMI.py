"""
Body Mass Index (BMI) Calculator - Version 2.0
A robust, high-efficiency, and modular CLI application to compute BMI,
classify health categories (WHO standards), and estimate healthy weight ranges.

Time Complexity: O(1)
Space Complexity: O(1)
"""

from typing import Tuple


# WHO BMI Categories defined as immutable thresholds: (upper_bound, category_label)
# Evaluated in ascending order in O(1) time complexity.
BMI_CATEGORIES: Tuple[Tuple[float, str], ...] = (
    (18.5, "Underweight"),
    (25.0, "Normal weight"),
    (30.0, "Overweight"),
    (35.0, "Obese (Class I)"),
    (40.0, "Obese (Class II)"),
    (float("inf"), "Obese (Class III - Severe/Morbid)"),
)


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Formula: BMI = weight (kg) / [height (m)]^2

    :param weight_kg: Body weight in kilograms (must be positive).
    :param height_m: Height in meters (must be positive).
    :return: Calculated BMI as a float.
    :raises ValueError: If weight_kg <= 0 or height_m <= 0.
    """
    if height_m <= 0:
        raise ValueError("Height must be a positive number greater than 0.")
    if weight_kg <= 0:
        raise ValueError("Weight must be a positive number greater than 0.")

    return weight_kg / (height_m * height_m)


def get_bmi_category(bmi: float) -> str:
    """
    Determine the health category based on WHO BMI standards.

    :param bmi: Calculated BMI value.
    :return: String category label.
    :raises ValueError: If bmi is negative.
    """
    if bmi < 0:
        raise ValueError("BMI cannot be negative.")

    for threshold, category in BMI_CATEGORIES:
        if bmi < threshold:
            return category

    return "Obese (Class III - Severe/Morbid)"


def get_healthy_weight_range(height_m: float) -> Tuple[float, float]:
    """
    Calculate the healthy weight range (kg) for a given height based on
    a normal BMI range of 18.5 to 24.9.

    :param height_m: Height in meters.
    :return: Tuple of (min_healthy_weight_kg, max_healthy_weight_kg).
    :raises ValueError: If height_m <= 0.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than 0.")

    h_sq = height_m * height_m
    min_weight = 18.5 * h_sq
    max_weight = 24.9 * h_sq
    return min_weight, max_weight


def get_valid_float(prompt: str, min_val: float, max_val: float) -> float:
    """
    Prompt the user repeatedly until a valid float within [min_val, max_val] is entered.

    :param prompt: Prompt message to display.
    :param min_val: Minimum acceptable value (inclusive).
    :param max_val: Maximum acceptable value (inclusive).
    :return: Validated float value.
    """
    while True:
        try:
            raw_input = input(prompt).strip()
            val = float(raw_input)
            if min_val <= val <= max_val:
                return val
            print(f"  [!] Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  [!] Invalid input. Please enter a valid numerical value.")


def main() -> None:
    """
    Main application runner.
    """
    print("=" * 45)
    print("       BMI CALCULATOR - VERSION 2.0")
    print("=" * 45)

    try:
        height = get_valid_float(
            prompt="Enter your height in meters (e.g., 1.75): ",
            min_val=0.5,
            max_val=2.8,
        )
        weight = get_valid_float(
            prompt="Enter your weight in kilograms (e.g., 70.0): ",
            min_val=10.0,
            max_val=500.0,
        )

        bmi = calculate_bmi(weight_kg=weight, height_m=height)
        category = get_bmi_category(bmi)
        min_w, max_w = get_healthy_weight_range(height)

        print("\n" + "-" * 45)
        print("                  RESULTS")
        print("-" * 45)
        print(f" Height           : {height:.2f} m")
        print(f" Weight           : {weight:.2f} kg")
        print(f" Calculated BMI   : {bmi:.2f}")
        print(f" Health Category  : {category}")
        print(f" Ideal Weight Span: {min_w:.1f} kg - {max_w:.1f} kg")
        print("-" * 45)

    except (KeyboardInterrupt, EOFError):
        print("\n\nOperation cancelled by user. Exiting gracefully.")


if __name__ == "__main__":
    main()

