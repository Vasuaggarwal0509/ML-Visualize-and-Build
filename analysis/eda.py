import pandas as pd
import numpy as np

from analyze_src.basic_data_inspection import DataInspector, DataTypesInspectionStrategy, SummaryStatisticsInspectionStrategy
from analyze_src.missing_values_analysis import MissingValuesAnalysisTemplate, SimpleMissingValuesAnalysis
from analyze_src.univariate_analysis import UnivariateAnalyzer, NumericalUnivariateAnalysis, CategoricalUnivariateAnalysis
from analyze_src.bivariate_analysis import BivariateAnalyzer, NumericalVsNumericalAnalysis, CategoricalVsNumericalAnalysis
from analyze_src.multivariate_analysis import SimpleMultivariateAnalysis

# Set display options for better readability
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Load the data
# Assuming you have already extracted the data into the 'extracted-data' folder

data_path = 'extracted_data/AmesHousing.csv'
df = pd.read_csv(data_path)

while True:
    print("\nExploratory Data Analysis Menu:")
    print("1. Basic Data Inspection")
    print("2. Missing Values Analysis")
    print("3. Univariate Analysis")
    print("4. Bivariate Analysis")
    print("5. Multivariate Analysis")
    print("6. Exit")

    choice = input("Select an option (1-6): ")

    if choice == '1':
        inspector = DataInspector()
        print("\nBasic Data Inspection:")
        print("a. Data Types Inspection")
        print("b. Summary Statistics Inspection")
        sub_choice = input("Select an option (a-b): ")
        if sub_choice == 'a':
            strategy = DataTypesInspectionStrategy()
            inspector.set_strategy(strategy)
            inspector.execute_inspection(df)
        elif sub_choice == 'b':
            strategy = SummaryStatisticsInspectionStrategy()
            inspector.set_strategy(strategy)
            inspector.execute_inspection(df)
        else:
            print("Invalid option.")

    elif choice == '2':
        analysis = SimpleMissingValuesAnalysis()
        analysis.identify_missing_values(df)
        analysis.visualize_missing_values(df)

    elif choice == '3':
        analyzer = UnivariateAnalyzer()
        print("\nUnivariate Analysis:")
        print("a. Numerical Variables")
        print("b. Categorical Variables")
        sub_choice = input("Select an option (a-b): ")
        if sub_choice == 'a':
            strategy = NumericalUnivariateAnalysis()
            analyzer.set_strategy(strategy)
            analyzer.execute_analysis(df,"Gr Liv Area")
        elif sub_choice == 'b':
            strategy = CategoricalUnivariateAnalysis()
            analyzer.set_strategy(strategy)
            analyzer.execute_analysis(df,"Order")
        else:
            print("Invalid option.")

    elif choice == '4':
        analyzer = BivariateAnalyzer()
        print("\nBivariate Analysis:")
        print("a. Numerical vs Numerical")
        print("b. Categorical vs Numerical")
        sub_choice = input("Select an option (a-b): ")
        if sub_choice == 'a':
            strategy = NumericalVsNumericalAnalysis()
            analyzer.set_strategy(strategy)
            analyzer.execute_analysis(df, 'Gr Liv Area', 'SalePrice')
        elif sub_choice == 'b':
            strategy = CategoricalVsNumericalAnalysis()
            analyzer.set_strategy(strategy)
            analyzer.execute_analysis(df, 'Order', 'SalePrice')
        else:
            print("Invalid option.")

    elif choice == '5':
        analysis = SimpleMultivariateAnalysis()
        analysis.generate_correlation_heatmap(df)
        print("Generating pair plot for selected features...")
        selected_features = df[['SalePrice', 'Gr Liv Area', 'Overall Qual', 'Total Bsmt SF', 'Year Built']]
        analysis.generate_pairplot(selected_features)

    elif choice == '6':
        print("Exiting EDA tool.")
        break

    else:
        print("Invalid")