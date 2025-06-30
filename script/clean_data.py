def convert_yes_no_to_binary(df):
    
    yes_no_columns = []

    # Loop through each column
    for column in df.columns:
        unique_values = df[column].unique()

       
        if set(unique_values) == {"Yes", "No"} or set(unique_values) == {"No", "Yes"}:
            yes_no_columns.append(column)

            
            for i in range(len(df)):
                value = df.at[i, column]
                if value == "Yes":
                    df.at[i, column] = 1
                elif value == "No":
                    df.at[i, column] = 0

            
            df[column] = df[column].astype(int)

    return df, yes_no_columns
