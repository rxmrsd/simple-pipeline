"""main.py"""
from pathlib import Path

import click
import pandas as pd
from google.cloud import bigquery


def get_data_from_bq(
    client: bigquery.Client,
    project: str,
    table_id: str,
) -> pd.DataFrame:
    """BigQueryからデータを取得する

    Args:
        client (bigquery.Client): BigQueryクライアント
        project (str): プロジェクトID
        table_id (str): テーブルID

    Returns:
        int: テーブルのサイズ
    """
    sql_path = Path(__file__).parent.joinpath("sql")
    query = sql_path.joinpath("sample.sql").read_text()
    query = query.format(project_id=project, table_id=table_id)
    result = client.query(query=query)

    return result.to_dataframe()


@click.command()
@click.option(
    "--project",
    type=str,
    required=True,
    help="project_id",
)
@click.option(
    "--table_id",
    type=str,
    required=True,
    help="table_id(dataset.table)",
)
@click.option(
    "--output_dir",
    type=str,
    required=True,
    help="output directory",
)
def main(project: str, table_id: str, output_dir) -> None:
    """Main function"""
    bq_client = bigquery.Client(project=project)
    table_len = get_data_from_bq(
        client=bq_client, project=project, table_id=table_id,
    )

    _output_dir = Path(output_dir)
    _output_dir.mkdir(parents=True, exist_ok=True)
    filepath = _output_dir.joinpath("result.parquet")
    table_len.to_parquet(filepath, index=False)


if __name__ == "__main__":
    main()
