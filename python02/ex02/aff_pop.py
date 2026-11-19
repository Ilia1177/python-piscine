from load_csv import load
import matplotlib.pyplot as plt


def convert_population(x):
    return float(x.removesuffix("M")) * 1_000_000


def main():
    '''Draw data using matplotlib'''
    data = load("../population_total.csv")
    if data is None:
        print("Error on reading data")
        return
    years = [str(year) for year in range(1800, 2051)]
    france = data[data["country"] == "France"][years]
    kazak = data[data["country"] == "Kazakhstan"][years]
    if france.empty or kazak.empty:
        print("Error: France not found in dataset")
        return

    france = france.map(convert_population)
    kazak = kazak.map(convert_population)

    france.index = ["France"]
    kazak.index = ["Kazakhstan"]

    ax = france.T.plot()
    kazak.T.plot(ax=ax)

    ax.set_title("Population projection")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")

    ax.legend()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
