import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_tpr(data, actual_col, predicted_col):
    """Calculate True Positive Rate (Sensitivity/Recall).

    Args:
        data (pd.DataFrame): DataFrame containing the actual and predicted labels.
        actual_col (str): Column name for actual labels.
        predicted_col (str): Column name for predicted labels.

    Returns:
        float: True Positive Rate.
    """
    true_positives = data[(data[actual_col] == 1) & (data[predicted_col] == 1)].shape[0]
    false_negatives = data[(data[actual_col] == 1) & (data[predicted_col] == 0)].shape[0]

    tpr = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    return tpr

def TPR_analysis(df, diseases, categories, category_name, run_num, number):
    plt.rcParams.update({'font.size': 18})
    results = []

    for category in categories:
        GAP_y = []
        percentage_y = []
        total_y = []
        positive_y = []
        negative_y = []

        for disease in diseases:
            pred_disease = f"{disease}_classified"  # Adjusted for predictions
            lab_disease = f"{disease}_labs"  # Adjusted for true labels
            
            # Filter data for the current category and disease
            category_data = df[df[category_name] == category]
            disease_positive = category_data[category_data[lab_disease] == 1]
            disease_negative = category_data[category_data[lab_disease] == 0]
            disease_predicted_positive = disease_positive[disease_positive[pred_disease] == 1]
            
            Total = len(disease_positive) + len(disease_negative)
            Positive = len(disease_positive)
            Negative = len(disease_negative)

            # Calculate TPR and percentages
            overall_positive = df[lab_disease].sum()
            percentage = Positive / overall_positive if overall_positive > 0 else 0

            TPR =  calculate_tpr(df[df[category_name] == category], lab_disease, pred_disease)

            print(TPR)

            GAP_y.append(TPR)
            percentage_y.append(percentage)
            total_y.append(Total)
            positive_y.append(Positive)
            negative_y.append(Negative)

        results.append({
            "Category": category,
            "Total": total_y,
            "Positive": positive_y,
            "Negative": negative_y,
            "GAP": GAP_y,
            "Percentage": percentage_y
        })

    result_df = pd.DataFrame(results)
    result_df.to_csv(f"./results/results{number}/Run{run_num}_TPR_{category_name}.csv", index=False)

# Define conditions and categories
diseases = ['slvh', 'dlv', 'composite', 'no_finding']

def run(number, run_num):
    metadata_df = pd.read_csv(f'./results/results{number}/metadata_with_predictions_output_labels_{number}.csv')

    metadata_df['age_decile'] = pd.cut(metadata_df['age'], bins=[0, 20, 40, 60, 80, 100], labels=['0-20', '20-40', '40-60', '60-80', '80+'])
    genders = metadata_df['sex'].unique()
    age_deciles = metadata_df['age_decile'].unique()

    TPR_analysis(metadata_df, diseases, age_deciles, 'age_decile', run_num, number)
    TPR_analysis(metadata_df, diseases, genders, 'sex', run_num, number)

if __name__ == "__main__":

    for run_num, number in [(1, 9), (2, 21), (3, 25), (4, 35), (5, 42)]:
        run(number, run_num)