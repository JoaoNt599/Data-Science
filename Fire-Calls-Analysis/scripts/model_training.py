import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def train_model(df):
    
    # Fill in the NaN in the Delay column with the average
    df['Delay'] = df['Delay'].fillna(df['Delay'].mean())

    features = ['Year', 'CallTypeGroup']
    
    if 'Delay' not in df.columns:
        raise KeyError("'Delay' not found in columns")
    
    df = pd.get_dummies(df[features + ['Delay']], drop_first=True)

    # Defines X (characteristics) and y (target variable)
    X = df.drop(columns=['Delay'])
    y = df['Delay']

    # Division into training and testing 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)


    # Prediction and evaluation
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    return model


if __name__ == "__main__":
    file_path = "./data/sf-fire-calls.csv"
    df = pd.read_csv(file_path)
    print(df.columns)

    df['CallDate'] = pd.to_datetime(df['CallDate'])
    df['Year'] = df['CallDate'].dt.year
    model = train_model(df)
    
