"""compile_pipeline.py"""
from typing import Optional

import click
from kfp import compiler
from kfp.registry import RegistryClient

from src.simple_pipeline import SimplePipeline


def compile_pipeline(
    project: str,
    location: str,
    template_path: str,
    pipeline_name: str,
) -> None:
    """コンパイル

    Args:
        project (str): プロジェクトID
        location (str): リージョン
        template_path (str): 出力ファイルパス
        pipeline_name (str): パイプライン名
    """
    simple_pipeline = SimplePipeline(
        project=project,
        location=location,
    )
    compiler.Compiler().compile(
        pipeline_func=simple_pipeline.build_pipeline(),
        package_path=template_path,
        pipeline_name=pipeline_name,
    )


def upload_to_registry(
    template_path: str,
    registry_path: str,
    tag: str,
    description: Optional[str] = None,
) -> str:
    """パイプラインyamlファイルをArtifact Registryにアップロードする

    Args:
        template_path (str): ローカルのyamlファイルパス
        registry_path (str): アップロード先のregistryパス
        tag (str): タグ
        description (Optional[str], optional): \
            パイプラインの説明. Defaults to None.

    Returns:
        str: Artifact Registryでのパイプラインのパス
    """
    client = RegistryClient(host=registry_path)

    extra_headers = (
        {"description": description} if description is not None else None
    )
    package_name, version_name = client.upload_pipeline(
        file_name=template_path,
        tags=tag,
        extra_headers=extra_headers,
    )
    return f"{registry_path}/{package_name}/{version_name}"


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
    "--pipeline_name",
    type=str,
    required=True,
    help="pipeline name",
)
@click.option(
    "--tag",
    type=str,
    required=True,
    help="pipeline tag",
)
@click.option(
    "--registry_path",
    type=str,
    required=True,
    help="pipeline registry",
)
def main(
    project: str,
    location: str,
    pipeline_name: str,
    tag: str,
    registry_path: str,
) -> None:
    """Main function"""
    template_path = "./simple_pipeline.yaml"

    compile_pipeline(
        project=project,
        location=location,
        template_path=template_path,
        pipeline_name=pipeline_name,
    )

    _ = upload_to_registry(
        template_path=template_path,
        registry_path=registry_path,
        tag=tag,
    )


if __name__ == "__main__":
    main()
