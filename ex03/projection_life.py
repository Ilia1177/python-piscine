import matplotlib.pyplot as plt
from load_csv import load


def main():
    '''Draw data using matplotlib'''
    income_path="../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_path="../life_expectancy_years.csv"
    life = load(life_path)
    income = load(income_path)
    if life is None or income is None:
        print("Error on reading data")
        return
    income = income["1900"]
    life = life["1900"]
    ax = plt.subplots()[1]
    ax.scatter(income, life)
    ax.set_xscale("symlog", linthresh=1000)
    ax.set_title("1900 time")
    ax.set_xlabel("Income per person")
    ax.set_ylabel("Life expectancy (years)")

    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
