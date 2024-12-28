import pandas as pd
import numpy as np

def generate_dataset(output_file='simulated_demand_data.csv', num_samples=5000, seed=42):
    """
    Generate a synthetic dataset for linear regression on product demand.
    
    Args:
        output_file (str): The name of the file to save the dataset.
        num_samples (int): The number of rows in the dataset.
        seed (int): Random seed for reproducibility.
    """
    # Set seed for reproducibility
    np.random.seed(seed)

    # Parameters
    categories = ['Confectionery', 'Beverages', 'Snacks']
    months = np.arange(1, 13)

    # Generate synthetic data
    data = {
        'Month': np.random.choice(months, size=num_samples),
        'Product_Category': np.random.choice(categories, size=num_samples),
        'Previous_Sales': np.random.randint(50, 500, size=num_samples),
    }

    # Seasonality factor based on month (e.g., festive months have higher demand)
    seasonality = {1: 1.0, 2: 1.1, 3: 1.2, 4: 1.0, 5: 1.3, 6: 1.5,
                   7: 1.4, 8: 1.2, 9: 1.3, 10: 1.4, 11: 1.6, 12: 1.8}

    # Apply seasonality and random noise to generate demand
    data['Seasonality_Factor'] = [seasonality[m] for m in data['Month']]
    data['Demand'] = (data['Previous_Sales'] * data['Seasonality_Factor']
                      * np.random.uniform(0.8, 1.2, size=num_samples)).astype(int)

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Dataset successfully saved to {output_file}")

# Generate and save the dataset
if __name__ == "__main__":
    generate_dataset()
