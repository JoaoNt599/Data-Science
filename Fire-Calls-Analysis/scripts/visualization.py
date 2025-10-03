import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_calls_per_year(df):
    calls_per_year = df.groupby('Year').size()
    calls_per_year.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title("Number of Calls per Year")
    plt.xlabel("Year")
    plt.ylabel("Call Number")
    plt.show()


def plot_calls_per_year_seabor(df):
    sns.set_theme(style="whitegrid")

    call_per_year = df.groupby('Year').size().reset_index(name='NumberofCalls')

    plt.figure(figsize=(12, 6))
    sns.barplot(data=call_per_year, x='Year', y='NumberofCalls', palette='viridis')
    plt.title("Number of Calls per Year", fontsize=16)
    plt.xlabel("Yaer", fontsize=12)
    plt.ylabel("Number of Calls", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_response_time_distribution(df):
    sns.set_theme(style="darkgrid")
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Delay', bins=30, kde=True, color="blue")
    plt.title("Response Time Distribution", fontsize=16)
    plt.xlabel("Response Time (minutes)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    file_path = "./data/sf-fire-calls.csv"
    df = pd.read_csv(file_path)

    df['CallDate'] = pd.to_datetime(df['CallDate'])
    df['Year'] = df['CallDate'].dt.year

    plot_calls_per_year_seabor(df)
    plot_calls_per_year(df)
    plot_response_time_distribution(df)