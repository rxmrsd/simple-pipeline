"""compile_pipeline.py"""
from typing import Optional

import click
from google.cloud import aiplatform


def exec_pipeline(
    project: str,
    location: str,
    pipeline_root: str,
    template_path: str,
    table_id: str,
    service_account: Optional[str] = None,
) -> None:
    """パイプライン実行

    Args:
        project (str): プロジェクトID
        location (str): リージョン
        pipeline_root (str): パイプライン結果の格納パス
        template_path (str): 実行するパイプラインファイル
        service_account (Optional[str], optional): \
            実行するサービスアカウント. Defaults to None.
    """
    aiplatform.init(
        project=project,
        location=location,
    )

    job = aiplatform.PipelineJob(
        display_name="simple_pipeline",
        template_path=template_path,
        pipeline_root=pipeline_root,
        parameter_values={
            "table_id": table_id,
        },
    )
    job.submit(
        service_account=service_account,
    )


@click.command()
@click.option(
    "--project",
    type=str,
    required=True,
    help="google cloud project name",
)
@click.option(
    "--location",
    type=str,
    required=True,
    help="region",
)
@click.option(
    "--pipeline_root",
    type=str,
    required=True,
    help="pipeline root",
)
@click.option(
    "--registry_template_path",
    type=str,
    required=True,
    help="pipeline registry",
)
@click.option(
    "--table_id",
    type=str,
    required=True,
    help="bigquery data table",
)
def main(
    project: str,
    location: str,
    pipeline_root: str,
    registry_template_path: str,
    table_id: str,
) -> None:
    """Main function"""
    exec_pipeline(
        project=project,
        location=location,
        pipeline_root=pipeline_root,
        template_path=registry_template_path,
        table_id=table_id,
    )


if __name__ == "__main__":
    main()
