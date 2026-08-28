import unittest
from BMI import calculate_bmi, get_bmi_category, get_healthy_weight_range


class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi_standard_values(self):
        # Height: 1.75m, Weight: 70kg -> BMI ≈ 22.86
        bmi = calculate_bmi(weight_kg=70.0, height_m=1.75)
        self.assertAlmostEqual(bmi, 22.857142857142858, places=4)

    def test_calculate_bmi_boundary_values(self):
        # Height: 2.0m, Weight: 80kg -> BMI = 20.0
        bmi = calculate_bmi(weight_kg=80.0, height_m=2.0)
        self.assertEqual(bmi, 20.0)

    def test_calculate_bmi_invalid_inputs(self):
        # Negative or zero height
        with self.assertRaises(ValueError):
            calculate_bmi(weight_kg=70.0, height_m=0)
        with self.assertRaises(ValueError):
            calculate_bmi(weight_kg=70.0, height_m=-1.5)

        # Negative or zero weight
        with self.assertRaises(ValueError):
            calculate_bmi(weight_kg=0, height_m=1.75)
        with self.assertRaises(ValueError):
            calculate_bmi(weight_kg=-70.0, height_m=1.75)

    def test_get_bmi_category_thresholds(self):
        self.assertEqual(get_bmi_category(16.0), "Underweight")
        self.assertEqual(get_bmi_category(18.49), "Underweight")
        self.assertEqual(get_bmi_category(18.5), "Normal weight")
        self.assertEqual(get_bmi_category(22.5), "Normal weight")
        self.assertEqual(get_bmi_category(24.99), "Normal weight")
        self.assertEqual(get_bmi_category(25.0), "Overweight")
        self.assertEqual(get_bmi_category(29.99), "Overweight")
        self.assertEqual(get_bmi_category(30.0), "Obese (Class I)")
        self.assertEqual(get_bmi_category(34.99), "Obese (Class I)")
        self.assertEqual(get_bmi_category(35.0), "Obese (Class II)")
        self.assertEqual(get_bmi_category(39.99), "Obese (Class II)")
        self.assertEqual(get_bmi_category(40.0), "Obese (Class III - Severe/Morbid)")
        self.assertEqual(get_bmi_category(55.0), "Obese (Class III - Severe/Morbid)")

    def test_get_bmi_category_negative_input(self):
        with self.assertRaises(ValueError):
            get_bmi_category(-5.0)

    def test_get_healthy_weight_range(self):
        # Height 1.80m -> 1.8^2 = 3.24
        # Min: 18.5 * 3.24 = 59.94 kg
        # Max: 24.9 * 3.24 = 80.676 kg
        min_w, max_w = get_healthy_weight_range(1.80)
        self.assertAlmostEqual(min_w, 59.94, places=2)
        self.assertAlmostEqual(max_w, 80.676, places=2)

    def test_get_healthy_weight_range_invalid(self):
        with self.assertRaises(ValueError):
            get_healthy_weight_range(0)
        with self.assertRaises(ValueError):
            get_healthy_weight_range(-1.75)


if __name__ == "__main__":
    unittest.main()
