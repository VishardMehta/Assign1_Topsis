# TOPSIS-Vishard-102317240

## 📝 Overview

**Topsis-Vishard-102317240** is a Python library for performing **Multi-Criteria Decision Making (MCDM)** using the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) algorithm. It allows you to rank alternatives based on multiple conflicting criteria, providing a robust mathematical approach to decision-making.

This package is designed to be simple, efficient, and easy to integrate into your data analysis workflows.

---

## 🔧 Installation

You can install the package directly from PyPI using pip:

```bash
pip install Topsis-Vishard-102317240
```

---

## 🚀 Usage

The package provides a command-line interface (CLI) for ease of use.

### Syntax

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Parameters

*   **InputDataFile**: Path to the input CSV file containing the data.
*   **Weights**: Comma-separated numbers representing the importance of each criterion (e.g., `1,1,1,2`).
*   **Impacts**: Comma-separated signs (`+` or `-`) indicating if a criterion is beneficial (`+`) or non-beneficial (`-`).
*   **ResultFileName**: Path where the output CSV file with results will be saved.

### Example

```bash
topsis data.csv "1,1,1,1,2" "+,+,-,+,+" result.csv
```

---

## 📊 Input Data Format

The input CSV file should strictly follow this structure:
1.  **First Column**: Object/Alternative Name (e.g., M1, M2, M3).
2.  **Subsequent Columns**: Numeric values for each criterion.

| Fund Name | P1 | P2 | P3 | P4 | P5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| M1 | 0.94 | 0.88 | 6.5 | 38.8 | 11.78 |
| M2 | 0.69 | 0.48 | 4.4 | 59.8 | 16.34 |
| ... | ... | ... | ... | ... | ... |

---

## 📤 Output

The output file will contain the original data along with two new columns:
*   **Topsis Score**: The calculated score for each alternative (higher is better).
*   **Rank**: The ranking of the alternative based on the score (1 is best).

| Fund Name | ... | Topsis Score | Rank |
| :--- | :--- | :--- | :--- |
| M5 | ... | 0.6988 | 1 |
| M8 | ... | 0.5955 | 2 |
| ... | ... | ... | ... |

---

## 📜 License

This project is licensed under the MIT License.

## 👤 Author

**Vishard Mehta**
*   **Email:** vmehta_be23@thapar.edu
*   **PyPI:** [Topsis-Vishard-102317240](https://pypi.org/project/Topsis-Vishard-102317240/)
