"""simple_pipeline.py"""
from typing import Optional

from kfp import components, dsl
from kfp.dsl.base_component import BaseComponent


class SimplePipeline:
    """シンプルパイプラインクラス"""

    def __init__(self, project: str, location: str) -> None:
        """コンストラクタ"""
        self.project = project
        self.location = location

    def bq_op(self, project: str, table_id: str) -> components.YamlComponent:
        """BigQueryからデータを取得するコンポーネント

        Args:
            project (str): プロジェクトID
            table_id (str): テーブルID

        Returns:
            components.YamlComponent: コンポーネント
        """
        op = load_component_from_yaml(
            project=self.project,
            yaml_filepath="./components/bq-component/component.yaml",
        )
        return op(project=project, table_id=table_id)

    def display_op(self, result_dir: str) -> components.YamlComponent:
        """結果を表示するコンポーネント

        Args:
            result_dir (str): 前段の出力結果パス

        Returns:
            components.YamlComponent: コンポーネント
        """
        op = load_component_from_yaml(
            project=self.project,
            yaml_filepath="./components/display-component/component.yaml",
        )
        return op(result_dir=result_dir)

    def build_pipeline(self) -> BaseComponent:
        """パイプライン定義"""

        @dsl.pipeline()
        def pipeline(table_id: str) -> None:
            """シンプルパイプライン

            Args:
                table_id (str): テーブルID
            """
            bq_task = self.bq_op(
                project=self.project,
                table_id=table_id,
            )
            _ = self.display_op(result_dir=bq_task.outputs["output_dir"])

        return pipeline


def load_component_from_yaml(
    project: str,
    yaml_filepath: str,
    tag: Optional[str] = None,
) -> components.YamlComponent:
    """yamlファイルからコンポーネントの設定情報の読み込み

    Args:
        project (str): プロジェクトID
        yaml_filepath (str): yamlファイルパス
        tag (Optional[str], optional): タグ. Defaults to None.

    Returns:
        components.YamlComponent: コンポーネント情報
    """
    op = components.load_component_from_file(yaml_filepath)

    if tag is None:
        tag = "latest"

    template: str = op.component_spec.implementation.container.image
    op.component_spec.implementation.container.image = template.format(
        PROJECT_ID=project,
        TAG=tag,
    )

    return op
