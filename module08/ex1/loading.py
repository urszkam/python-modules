import importlib
import sys


def check_dependencies() -> bool:
    print("Checking dependencies:")
    dependencies = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical computation',
        'matplotlib': 'Visualization'
    }
    import_success = True
    for name, description in dependencies.items():
        try:
            module = importlib.import_module(name)
            if name == "matplotlib":
                importlib.import_module(f"{name}.pyplot")
            print(
                f"[OK] {module.__name__} ({module.__version__}) - "
                f"{description} ready"
            )
        except ModuleNotFoundError:
            import_success = False
            print(f"Missing dependency: {name}")
            print("Installation instruction:")
            print(f"Poetry: poetry add {name}")
            print(f"Pip: pip install {name}")

    return import_success


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        return

    print("\nAnalyzing Matrix data...")
    np = sys.modules["numpy"]
    points = np.random.uniform(0, 100, size=1000)

    print("Processing 1000 data points...")
    pd = sys.modules["pandas"]
    df = pd.DataFrame({"value": points})

    print("Generating visualization...")
    plt = sys.modules["matplotlib.pyplot"]
    bins = 10
    df["value"].plot.hist(
        bins=bins,
        range=(0, 100),
        rwidth=0.7,
        title="Data distribution",
        xlabel="Value",
        ylabel="Points per bucket"
    )
    plt.axhline(len(df) / bins, color="red", linestyle=":")
    print("\nAnalysis complete!")

    dest_file = "matrix_analysis.png"
    plt.savefig(dest_file)
    plt.close()
    print(f"Results saved to: {dest_file}")


if __name__ == "__main__":
    main()
