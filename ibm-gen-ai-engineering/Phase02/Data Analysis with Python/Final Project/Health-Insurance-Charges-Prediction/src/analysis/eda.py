from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Dynamically resolve root directory and target paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PRO_DATA_LOC = BASE_DIR / "data" / "processed" / "insurance_cleaned.csv"
FIGURES_DIR = BASE_DIR / "reports" / "figures"


def save_and_format_plot(title, xlabel, ylabel, filename, output_dir=FIGURES_DIR):
    """Formats plot labels, sets axis bounds, saves figure to disk, and closes the plot.

    Parameters:
    ----------
    title : str
        The main title for the plot figure.
    xlabel : str
        Label text for the x-axis.
    ylabel : str
        Label text for the y-axis.
    filename : str
        File name for the saved PNG figure (e.g., 'bmi_vs_charges.png').
    output_dir : Path or str, default=FIGURES_DIR
        Directory where the output PNG will be stored.
    """
    plt.ylim(0)
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    # Fixed: Corrected variable reference from output_path to output_dir
    save_path = Path(output_dir) / filename
    save_path.parent.mkdir(parents=True, exist_ok=True)

    # Save and display figure
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    print(f"Figure successfully saved to: {save_path}")

    plt.show()
    plt.close()


def reg_plot(file_path=PRO_DATA_LOC, output_dir=FIGURES_DIR):
    """Generates a scatter plot with a linear regression line showing the relationship

    between BMI and medical insurance charges.

    Parameters:
    ----------
    file_path : Path or str, default=PRO_DATA_LOC
        Path to the cleaned dataset CSV file.
    output_dir : Path or str, default=FIGURES_DIR
        Directory where the output plot PNG will be saved.
    """
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 6))

    sns.regplot(
        x="bmi", 
        y="charges", 
        data=df, 
        line_kws={"color": "red"}
        )

    save_and_format_plot(
        title="BMI vs Insurance Charges",
        xlabel="BMI",
        ylabel="Charges ($)",
        filename="bmi_vs_charges.png",
        output_dir=output_dir,
    )


def box_plot(file_path=PRO_DATA_LOC, output_dir=FIGURES_DIR):
    """Generates a box plot showing the distribution of medical insurance charges

    categorized by smoker status.

    Parameters:
    ----------
    file_path : Path or str, default=PRO_DATA_LOC
        Path to the cleaned dataset CSV file.
    output_dir : Path or str, default=FIGURES_DIR
        Directory where the output plot PNG will be saved.
    """
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 6))
    sns.boxplot(
        x="smoker", 
        y="charges", 
        data=df
        )

    # Reused helper function and corrected xlabel from "BMI" to "Smoker Status"
    save_and_format_plot(
        title="Smoker Status vs Insurance Charges",
        xlabel="Smoker Status (0 = Non-Smoker, 1 = Smoker)",
        ylabel="Charges ($)",
        filename="smoker_vs_charges.png",
        output_dir=output_dir,
    )

def correlation_heatmap(file_path=PRO_DATA_LOC, output_dir=FIGURES_DIR):
    """Generates and saves a full correlation matrix heatmap."""
    df = pd.read_csv(file_path)

    # Set explicit square figure dimensions
    fig, ax = plt.subplots(figsize=(10, 8))

    # Calculate numeric correlations
    corr_matrix = df.corr(numeric_only=True)

    # Draw heatmap
    sns.heatmap(
        corr_matrix, 
        annot=True, 
        cmap="coolwarm", 
        fmt=".2f", 
        linewidths=0.5,
        ax=ax
    )
    plt.title("Correlation Matrix Heatmap", fontsize=14, pad=12)

    save_path = Path(output_dir) / "correlation_matrix.png"
    save_path.parent.mkdir(parents=True, exist_ok=True)

    # bbox_inches='tight' prevents axis labels from being clipped when saved
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    print(f"Heatmap successfully saved to: {save_path}")

    plt.show()
    plt.close()

def charge_distribution(file_path=PRO_DATA_LOC, output_dir=FIGURES_DIR):
    """Generates and saves a histogram with a KDE curve showing the distribution

    of medical insurance charges.
    """
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 6))
    sns.histplot(
        df["charges"], 
        kde=True, 
        bins=30, 
        color="skyblue"
        )

    save_and_format_plot(
        title="Distribution of Insurance Charges",
        xlabel="Charges ($)",
        ylabel="Frequency / Count",
        filename="charge_distribution.png",
        output_dir=output_dir,
    )

def age_vs_charges(file_path=PRO_DATA_LOC, output_dir=FIGURES_DIR):
    """Generates a scatter plot with a linear regression line showing the relationship
    between age and medical insurance charges.
    """
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 6))
    sns.regplot(x="age", y="charges", data=df, line_kws={"color": "red"})

    save_and_format_plot(
        title="Age vs Insurance Charges",
        xlabel="Age",
        ylabel="Charges ($)",
        filename="age_vs_charges.png",
        output_dir=output_dir,
    )


if __name__ == "__main__":
    reg_plot()
    box_plot()
    correlation_heatmap()
    charge_distribution()
    age_vs_charges()