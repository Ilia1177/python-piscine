import matplotlib.pyplot as plt
from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''Draw data using matplotlib'''
    data = load("../life_expectancy_years.csv")
    if data is None:
        print("Error on reading data")
        return
    france = data[data["country"] == "France"]
    years = [str(year) for year in range(1800, 2100)]
    if france.empty or not all(year in data.columns for year in years):
        print("Error: France not found in dataset")
        return
    france = france[years]
    ax = france.T.plot(legend=False)
    ax.set_title("France life expectancy")
    ax.set_xlabel("Year")
    ax.set_ylabel("Life expectancy (years)")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
