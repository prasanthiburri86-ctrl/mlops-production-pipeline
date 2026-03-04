def validate_data(df):
    print("Running Data Validation...")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values!")

    expected_columns = ["age", "salary", "experience", "purchased"]
    if list(df.columns) != expected_columns:
        raise ValueError("Dataset schema mismatch!")

    print("Data validation passed!\n")