# TOPSIS-Python: Multi-Criteria Decision Making Tool

## 🚀 Project Overview

**TOPSIS-Python** is a comprehensive solution for implementing the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**. This project simplifies complex decision-making processes where multiple conflicting criteria must be evaluated to find the most optimal alternative.

This repository provides a robust implementation of TOPSIS in three convenient formats:
1.  **Command-Line Interface (CLI):** A standalone script for quick local analysis.
2.  **PyPI Package:** A distributable Python library for easy integration into other projects.
3.  **Web Service:** A user-friendly web application to perform analysis without writing code.

---

## 📦 Part 1: Command-Line Interface (CLI)

The core logic is implemented in Python and can be executed directly from your terminal. It processes a CSV file containing your data, applies weights and impacts to each criterion, and outputs a ranked results file.

### How to Run

```bash
python run_cli.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Arguments

| Argument | Description | Example |
| :--- | :--- | :--- |
| **InputDataFile** | CSV file with data. First column is ID/Name. | `data.csv` |
| **Weights** | Comma-separated weights for criteria. | `1,1,1,2` |
| **Impacts** | Comma-separated impacts (`+` for benefit, `-` for cost). | `+,+,-,+` |
| **OutputResultFileName** | Name of the output CSV file. | `result.csv` |

### Example Usage

```bash
python run_cli.py sample_data/data.csv "1,1,1,1,2" "+,+,-,+,+" result.csv
```

**Input Format (`data.csv`):**
| Fund Name | P1 | P2 | P3 | P4 | P5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| M1 | 0.94 | 0.88 | 6.5 | 38.8 | 11.78 |
| M2 | 0.69 | 0.48 | 4.4 | 59.8 | 16.34 |
| ... | ... | ... | ... | ... | ... |

**Output Format (`result.csv`):**
| Fund Name | ... | Topsis Score | Rank |
| :--- | ... | :--- | :--- |
| M5 | ... | 0.6988 | 1 |
| M8 | ... | 0.5955 | 2 |
| ... | ... | ... | ... |

---

## 📦 Part 2: Python Package (PyPI)

This implementation is also available as a Python package, allowing you to install and use it globally on your system.

**Package Name:** `Topsis-Vishard-102317240`
**PyPI Link:** [https://pypi.org/project/Topsis-Vishard-102317240/](https://pypi.org/project/Topsis-Vishard-102317240/)

### Installation

```bash
pip install Topsis-Vishard-102317240
```

### Usage

Once installed, you can use the `topsis` command anywhere:

```bash
topsis data.csv "1,1,1,1,2" "+,+,-,+,+" output.csv
```

---

## 🌐 Part 3: Web Service

A web-based interface is available for users to upload their data and receive results via email.

**Live Demo:** [https://assign1-topsis.onrender.com/](https://assign1-topsis.onrender.com/)

**Features:**
*   Simple file upload (.csv/.xlsx).
*   Easy input for weights and impacts.
*   Results delivered directly to your email inbox.

*(Note: The live demo is hosted on a free tier and may have cold-start delays. Email functionality requires valid SMTP credentials configured in the backend.)*

<<<<<<< HEAD
#### Live Link: https://assign1-topsis.onrender.com/
**Live Deployment Status:** While the application is compatible with platforms like Render or Railway, outbound SMTP (Email) traffic on ports 587 and 465 is currently blocked by these providers' free-tier firewalls to prevent spam. Consequently, the email-sending feature is best demonstrated in a local environment where network ports are unrestricted.
=======
---

## 👤 Author

**Vishard Mehta**
*   **Email:** vmehta_be23@thapar.edu
*   **GitHub:** [Warning: link to github.com/VishardMehta doesn't exist]
*   **LinkedIn:** [Vishard Mehta](https://www.linkedin.com/in/vishard-mehta/)
>>>>>>> f3b463d (Rewrite documentation to be unique and professional)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
