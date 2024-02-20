"""main.py"""
from pathlib import Path

import click
import pandas as pd


@click.command()
@click.option(
    "--result_dir",
    type=str,
    required=True,
    help="result bq-component directory",
)
def main(result_dir: str) -> None:
    """Main function"""
    result = pd.read_parquet(Path(result_dir).joinpath("result.parquet"))
    print(result)


if __name__ == "__main__":
    main()
