def svm_pharmacy_game():
    # 1. Scenario: Pharmaceutical Solid-Dose Manufacturing
    print("--- 💊 THE EXCIPIENT EXPERT: SUPPORT VECTOR MACHINE SIM 💊 ---")
    print("Mission: Predict if a raw excipient mix will successfully compress into a stable tablet.")
    print("Goal: Establish a Maximum-Margin Hyperplane to separate structural compound states.")

    # 2. Historical Manufacturing Batches (Continuous Physical Metrics)
    # Features: [Compaction Pressure (MPa), Moisture Content (%)] -> Label: -1 = Stable, 1 = Unstable
    # SVMs mathematically favor using -1 and +1 for binary target states.
    print("\n--- 🖥️ HISTORICAL COMPACTION TELEMETRY ---")
    batches = [
        {"features": [40.0, 1.2], "label": -1, "status": "Stable Pill"},
        {"features": [45.0, 1.8], "label": -1, "status": "Stable Pill"},
        {"features": [15.0, 4.5], "label": 1, "status": "Unstable Powder"},
        {"features": [20.0, 5.0], "label": 1, "status": "Unstable Powder"},
    ]
    for idx, b in enumerate(batches):
        print(f"Batch {idx+1}: Pressure = {b['features'][0]} MPa | Moisture = {b['features'][1]}% -> [{b['status']}]")

    # 3. Game Inputs: Setting Hyperplane Coefficients (Weights and Bias)
    print("\n--- STEP 1: POSITION THE MAXIMUM-MARGIN HYPERPLANE ---")
    print("The SVM boundary line is defined by: f(x) = (w1 * Pressure) + (w2 * Moisture) + bias")
    print("Points where f(x) < 0 are classified as Stable (-1). Points where f(x) > 0 are Unstable (+1).")
    try:
        w1 = float(input("Enter Weight 1 (Pressure impact, e.g., -0.2): "))
        w2 = float(input("Enter Weight 2 (Moisture impact, e.g., 2.0): "))
        bias = float(input("Enter Base Bias parameter (e.g., -3.0): "))
    except ValueError:
        w1, w2, bias = -0.2, 2.0, -3.0

    weights = [w1, w2]

    # 4. Incoming Intercepted Batch Telemetry
    # A new pilot batch is loaded into the hydraulic tablet press
    test_batch = [38.0, 2.5] # Borderline high pressure but moderate moisture
    print(f"\n--- 🚨 COMPRESSION LINE: NEW MIX UNDER ANALYSIS ---")
    print(f"Incoming Profile -> Compaction Pressure: {test_batch[0]} MPa | Moisture Content: {test_batch[1]}%")

    # 5. The Math: Computing the Dot Product Hyperplane Distance
    print("\n--- 🔄 EXECUTING MATRIX HYPERPLANE PROJECTIONS ---")
    
    # Linear projection: f(x) = w • x + b
    raw_score = (test_batch[0] * weights[0]) + (test_batch[1] * weights[1]) + bias
    print(f"Calculated Functional Margin Score f(x): {raw_score:.4f}")

    # 6. The Sign Activation Function
    # In an SVM, the classification depends purely on the sign (positive or negative) of the result
    if raw_score >= 0:
        prediction = 1
        verdict = "❌ UNSTABLE COMPLEX: MIX WILL CRUMBLE INTO POWDER"
    else:
        prediction = -1
        verdict = "✅ STABLE COMPLEX: OPTIMAL INTERLOCKING PILLED MATRIX"

    print(f"Classifier Output Sign: {'+' if raw_score >= 0 else '-'}")
    print(f"Automated Manufacturing Verdict: {verdict}")

    # 7. Ground Truth Validation
    actual_truth = -1 # A pressure of 38 MPa and 2.5% moisture falls safely within the stable boundaries
    if prediction == actual_truth:
        print("\n🏆 SUCCESS: Your SVM parameters correctly identified a manufacture-ready pill formula!")
        print("The factory line runs at peak performance with zero industrial product fracturing.")
    else:
        print("\n💥 LINE CRASH: Misclassification error! The pill fractured on ejection or a valid mix was rejected.")

if __name__ == "__main__":
    svm_pharmacy_game()
