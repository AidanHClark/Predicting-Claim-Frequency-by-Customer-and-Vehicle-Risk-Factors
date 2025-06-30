import pandas as pd
import matplotlib.pyplot as plt

def plot_claims_and_frequency(df_analysis: pd.DataFrame, output_path: str = "plots/claims_frequency_by_vehicle_age.png"):
    
    df_sorted = df_analysis.sort_values(by="vehicle_age")

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.bar(df_sorted["vehicle_age"], df_sorted["total_claims"], color='skyblue', label="Number of Claims")
    ax1.set_xlabel("Vehicle Age")
    ax1.set_ylabel("Number of Claims", color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')

   
    ax2 = ax1.twinx()
    ax2.plot(df_sorted["vehicle_age"], df_sorted["claim_frequency"], color='orange', marker='o', label="Claim Frequency")
    ax2.set_ylabel("Claim Frequency", color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    
    plt.title("Number of Claims and Claim Frequency by Vehicle Age")
    fig.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_claims_and_frequency_by_customer_age(df_analysis: pd.DataFrame, output_path: str = "plots/claims_frequency_by_customer_age.png"):
    df_sorted = df_analysis.sort_values(by="customer_age")

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Bar plot: Number of Claims
    ax1.bar(df_sorted["customer_age"], df_sorted["total_claims"], color="lightblue", label="Number of Claims")
    ax1.set_xlabel("Customer Age")
    ax1.set_ylabel("Number of Claims", color="lightblue")
    ax1.tick_params(axis="y", labelcolor="lightblue")

    # Line plot: Claim Frequency
    ax2 = ax1.twinx()
    ax2.plot(df_sorted["customer_age"], df_sorted["claim_frequency"], color="darkorange", marker="o", label="Claim Frequency")
    ax2.set_ylabel("Claim Frequency", color="darkorange")
    ax2.tick_params(axis="y", labelcolor="darkorange")

    plt.title("Number of Claims and Claim Frequency by Customer Age")
    fig.tight_layout()
    plt.savefig(output_path)
    plt.close()
def plot_claims_and_frequency_by_ncap(df_analysis: pd.DataFrame, output_path: str = "plots/claims_frequency_by_ncap_rating.png"):
    df_sorted = df_analysis.sort_values(by="ncap_rating")

    fig, ax1 = plt.subplots(figsize=(12, 6))

 
    ax1.bar(df_sorted["ncap_rating"], df_sorted["total_claims"], color='skyblue', label="Number of Claims")
    ax1.set_xlabel("NCAP Rating")
    ax1.set_ylabel("Number of Claims", color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')

    
    ax2 = ax1.twinx()
    ax2.plot(df_sorted["ncap_rating"], df_sorted["claim_frequency"], color='orange', marker='o', label="Claim Frequency")
    ax2.set_ylabel("Claim Frequency", color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    plt.title("Number of Claims and Claim Frequency by NCAP Rating")
    fig.tight_layout()
    plt.savefig(output_path)
    plt.close()
if __name__ == "__main__":
    from analyze_vehicle_risk import df_analysis
    plot_claims_and_frequency(df_analysis)

    from analyze_customer_risk import df_customer_risk
    plot_claims_and_frequency_by_customer_age(df_customer_risk)

    from analyze_ncap_rating import df_analysis
    plot_claims_and_frequency_by_ncap(df_analysis)