# 💊 The Excipient Expert: Support Vector Machine (SVM) Formulation Classifier

An interactive Supervised Learning simulation designed to teach **Support Vector Machines (SVM)** and **Maximum-Margin Hyperplanes** from scratch. You play as a Pharmaceutical Formulations Scientist mapping manufacturing metrics, calculating structural decision boundaries to guarantee raw chemical mixtures compress into uniform tablets rather than fracturing into unusable powder.

## 🎓 Learning Objectives

This project focuses on teaching:
* **Support Vector Machines (SVM):** A geometric classification algorithm that isolates structural classes by establishing optimized separation planes.
* **Maximum-Margin Hyperplanes:** Identifying the mathematically perfect boundary line that maximizes the spatial gap between frontline opposing data records.
* **Support Vectors:** Highlighting the critical edge-case data arrays that act as structural anchors holding the decision boundary in position.
* **Sign Activation Logic:** Utilizing binary sign vectors (Positive vs. Negative mappings) to generate immediate hard-categorical evaluation judgments.

---

## ✨ Features

* **Industrial Pharmacy Scenario:** Contextualizes multi-dimensional optimization space inside a heavy hydraulic pill pressing and compliance workflow.
* **Matrix Projection Telemetry:** Calculates and outputs the exact linear dot product combinations and operational margin thresholds step-by-step.
* **Interactive Weight Manipulation:** Enables players to adjust dimensional weights and baseline intercepts to see how hyperplane slants alter classification parameters.
* **Pure Mathematical Branching:** Programmed strictly with fundamental Python expressions, conducting vector separation math without importing data matrix frames or packaging wrappers.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You only need **Python 3** installed.

### 2. Setup and Execution
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/excipient-expert-svm.git](https://github.com/YOUR_USERNAME/excipient-expert-svm.git)
    cd excipient-expert-svm
    ```
2.  **Save the Code:** Save the provided script as `tablet_press_svm.py`.
3.  **Run the Script:**
    ```bash
    python tablet_press_svm.py
    ```

### 3. Gameplay Instructions
1.  **Examine Compaction Logs:** Review the physical features (Compaction Pressure vs. Moisture Content) alongside their structural labels ($-1 = \text{Stable Pill}$, $1 = \text{Unstable Powder}$).
2.  **Align the Separation Hyperplane:** Enter structural values for Weight 1, Weight 2, and Bias to lock in the linear boundary equation: $f(x) = w \cdot x + b$.
3.  **Activate the Hydraulic Press:** Monitor the automated feed line as a borderline chemical trial matrix ($38.0\text{ MPa}$, $2.5\%\text{ Moisture}$) is processed.
4.  **Audit the Sign Output:** Analyze whether the functional margin resolved as a positive or negative coefficient to verify if the formula successfully compressed.

---

## 🧠 Code Structure Highlights

### Hyperplane Linear Dot Product
The system measures directional margins across continuous material dimensions by executing a fast linear accumulation across properties.

```python
# Linear Projection Formula: f(x) = (w1 * x1) + (w2 * x2) + b
raw_score = (test_batch[0] * weights[0]) + (test_batch[1] * weights[1]) + bias

