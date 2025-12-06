# プロジェクトへの貢献

> [!CAUTION]
>
> 現在のプロジェクトメンテナーは、ドキュメントの自動国際化を研究中です。そのため、ドキュメントの国際化／翻訳に関連する PR は一切受け付けません！
>
> ドキュメントの国際化／翻訳に関連する PR を提出しないでください！

このプロジェクトに興味を持っていただきありがとうございます！貢献を始める前に、以下のガイドラインを読んで、あなたの貢献がスムーズに受け入れられるようにしてください。

## 受け付けない貢献の種類

1. ドキュメントの国際化／翻訳  
2. HTTP API など、コアインフラストラクチャに関連する貢献  
3. 「助けが必要ない」と明示的にマークされたイシュー（[Byaidu/PDFMathTranslate](Byaidu/PDFMathTranslate) および [PDFMathTranslate-next/PDFMathTranslate-next](PDFMathTranslate-next/PDFMathTranslate-next) リポジトリ内のイシューを含む）。  
4. メンテナーが不適切と判断したその他の貢献。  
5. ドキュメントへの貢献だが、英語以外の言語でドキュメントを変更する場合。  
6. `PDF` ファイルの変更を必要とする PR。  
7. `pdf2zh_next/gui_translation.yaml` ファイルを変更する PR。

上記の種類に関連する PR は提出しないでください。

> [!NOTE]
>
> ドキュメントに貢献したい場合は、**英語版のドキュメントのみを修正してください**。他の言語バージョンは貢献者自身によって翻訳されます。

To ensure the quality of the code and the maintainability of the project, we recommend that you discuss with the maintainers via Issue before submitting the following types of PRs:

- **Large-scale refactoring**: If you plan to refactor a large amount of code, it is recommended that you discuss it with the maintainers via Issue first to ensure that the refactoring direction is consistent with the project's goals.
- **New features**: If you plan to add new features, it is recommended that you discuss it with the maintainers via Issue first to ensure that the new features are consistent with the project's goals.
- **Performance optimization**: If you plan to optimize the performance of the project, it is recommended that you discuss it with the maintainers via Issue first to ensure that the optimization direction is consistent with the project's goals.
- **Architecture changes**: If you plan to change the architecture of the project, it is recommended that you discuss it with the maintainers via Issue first to ensure that the architecture changes are consistent with the project's goals.

## PRs that are not recommended to be submitted
To ensure the quality of the code and the maintainability of the project, we do not recommend submitting the following types of PRs:

- **Code that does not follow the project's coding standards**: If your code does not follow the project's coding standards, it is recommended that you modify it to follow the project's coding standards before submitting a PR.
- **Code that does not have tests**: If your code does not have tests, it is recommended that you add tests before submitting a PR.
- **Code that does not have documentation**: If your code does not have documentation, it is recommended that you add documentation before submitting a PR.
- **Code that does not have a clear purpose**: If your code does not have a clear purpose, it is recommended that you clarify the purpose before submitting a PR.

---

### OUTPUT

## メンテナーと Issue を通じて事前に議論することを推奨する PR
コードの品質とプロジェクトの保守性を確保するため、以下の種類の PR を提出する前に、メンテナーと Issue を通じて議論することを推奨します：

- **大規模なリファクタリング**：大量のコードをリファクタリングする計画がある場合は、まず Issue を通じてメンテナーと議論し、リファクタリングの方向性がプロジェクトの目標と一致していることを確認することをお勧めします。
- **新機能の追加**：新機能を追加する計画がある場合は、まず Issue を通じてメンテナーと議論し、新機能がプロジェクトの目標と一致していることを確認することをお勧めします。
- **パフォーマンスの最適化**：プロジェクトのパフォーマンスを最適化する計画がある場合は、まず Issue を通じてメンテナーと議論し、最適化の方向性がプロジェクトの目標と一致していることを確認することをお勧めします。
- **アーキテクチャの変更**：プロジェクトのアーキテクチャを変更する計画がある場合は、まず Issue を通じてメンテナーと議論し、アーキテクチャの変更がプロジェクトの目標と一致していることを確認することをお勧めします。

## 提出を推奨しない PR
コードの品質とプロジェクトの保守性を確保するため、以下の種類の PR の提出は推奨しません：

- **プロジェクトのコーディング標準に従っていないコード**：コードがプロジェクトのコーディング標準に従っていない場合は、PR を提出する前に、プロジェクトのコーディング標準に従うように修正することをお勧めします。
- **テストがないコード**：コードにテストがない場合は、PR を提出する前にテストを追加することをお勧めします。
- **ドキュメントがないコード**：コードにドキュメントがない場合は、PR を提出する前にドキュメントを追加することをお勧めします。
- **明確な目的がないコード**：コードに明確な目的がない場合は、PR を提出する前に目的を明確にすることをお勧めします。

- Large-scale code refactoring
- Adding new features
- Performance optimization
- Architecture changes

The following types of PRs are not recommended for submission:
- Code that does not follow the project's coding standards
- Code without tests
- Code without documentation
- Code without a clear purpose

---

### OUTPUT

以下の種類の PR については、提出前にまずメンテナーと議論することを推奨します：
- 大規模なコードリファクタリング
- 新機能の追加
- パフォーマンスの最適化
- アーキテクチャの変更

以下の種類の PR は提出を推奨しません：
- プロジェクトのコーディング標準に従っていないコード
- テストがないコード
- ドキュメントがないコード
- 明確な目的がないコード

2. PRs related to implementing a user login system. (This project does not require a user login system).
3. PRs that involve integrating with third-party services beyond the scope of the project's current architecture. (Such as adding support for a new translation service that requires significant changes to the core architecture).
4. PRs that change the core functionality of the project without a clear and agreed-upon roadmap. (Such as changing the way the project handles PDF parsing without prior discussion).
5. PRs that add features that are not aligned with the project's goals. (Such as adding a social media sharing feature).

---

### OUTPUT

1. マルチユーザー共有機能に関連する PR（このプロジェクトは主にシングルユーザー向けに設計されており、包括的なマルチユーザーシステムを導入する予定はありません）。
2. ユーザーログインシステムの実装に関連する PR（このプロジェクトはユーザーログインシステムを必要としません）。
3. プロジェクトの現在のアーキテクチャの範囲を超えるサードパーティサービスとの統合を含む PR（例えば、コアアーキテクチャに大幅な変更を必要とする新しい翻訳サービスのサポートを追加するなど）。
4. 明確かつ合意されたロードマップなしにプロジェクトのコア機能を変更する PR（例えば、事前の議論なしにプロジェクトが PDF 解析を処理する方法を変更するなど）。
5. プロジェクトの目標に沿わない機能を追加する PR（例えば、ソーシャルメディア共有機能を追加するなど）。

## 貢献プロセス

1. このリポジトリをフォークし、ローカルにクローンします。
2. 新しいブランチを作成します：`git checkout -b feature/<feature-name>`。
3. 開発を行い、コードが要件を満たしていることを確認します。
4. コードをコミットします：
   ```bash
   git add .
   git commit -m "<semantic commit message>"
   ```
5. 自分のリポジトリにプッシュします：`git push origin feature/<feature-name>`。
6. GitHub で PR を作成し、詳細な説明を提供し、[@awwaawwa](https://github.com/awwaawwa) にレビューを依頼します。
7. すべての自動チェックが合格することを確認します。

> [!TIP]
>
> 開発が完全に完了するまで待つ必要はありません。早期に PR を作成することで、実装をレビューし、提案を提供することができます。
>
> ソースコードや関連事項について質問がある場合は、メンテナーまでお問い合わせください：aw@funstory.ai。
>
> バージョン 2.0 のリソースファイルは [BabelDOC](https://github.com/funstory-ai/BabelDOC) と共有されています。関連リソースをダウンロードするコードは BabelDOC にあります。新しいリソースファイルを追加したい場合は、BabelDOC のメンテナーまでお問い合わせください：aw@funstory.ai。

## 基本要件

<h4 id="sop">1. ワークフロー</h4>

   - `main` ブランチからフォークし、フォークしたブランチで開発を行ってください。
- プルリクエスト（PR）を提出する際は、変更内容の詳細な説明を提供してください。
- PR が自動チェックに合格しない場合（`checks failed` と赤い十字マークで表示されます）、対応する `details` を確認し、提出内容を修正して新しい PR がすべてのチェックに合格するようにしてください。


<h4 id="dev&test">2. 開発とテスト</h4>

   - 開発とテストには `pip install -e .` コマンドを使用してください。


<h4 id="format">3. コードフォーマット</h4>

   - `pre-commit` ツールを設定し、コードフォーマット用に `black` と `flake8` を有効にします。


<h4 id="requpdate">4. 依存関係の更新</h4>

   - 新しい依存関係を導入する場合は、`pyproject.toml` ファイル内の依存関係リストを適時更新してください。


<h4 id="docupdate">5. ドキュメント更新</h4>

   - 新しいコマンドラインオプションを追加する場合、`README.md` ファイルのすべての言語バージョンにあるコマンドラインオプションのリストを更新してください。


<h4 id="commitmsg">6. コミットメッセージ</h4>

   - [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) を使用してください。例：`feat(translator): add openai`。


<h4 id="codestyle">7. コーディングスタイル</h4>

   - 提出されたコードが基本的なコーディングスタイル標準に準拠していることを確認してください。
   - 変数名にはスネークケース（snake_case）またはキャメルケース（camelCase）を使用してください。


<h4 id="doctypo">8. ドキュメントのフォーマット</h4>

   - `README.md` のフォーマットについては、[中国語コピーライティングガイドライン](https://github.com/sparanoid/chinese-copywriting-guidelines) に従ってください。
   - 英語と中国語のドキュメントは常に最新の状態に保つようにしてください。他の言語のドキュメントの更新は任意です。

## 翻訳エンジンの追加

1. `pdf2zh/config/translate_engine_model.py` ファイルに新しい翻訳エンジン設定クラスを追加します。
2. 同じファイル内の `TRANSLATION_ENGINE_SETTING_TYPE` 型エイリアスに、新しい翻訳エンジン設定クラスのインスタンスを追加します。
3. `pdf2zh/translator/translator_impl` フォルダに新しい翻訳エンジン実装クラスを追加します。

> [!NOTE]
>
> このプロジェクトは、RPS（1 秒あたりのリクエスト数）が 4 未満の翻訳エンジンをサポートする意図はありません。そのようなエンジンのサポートを提出しないでください。
> 以下の種類の翻訳機も統合されません：
> - 上流のメンテナーによって廃止された翻訳機（deeplx など）
> - 大きな依存関係を持つ翻訳機（pytorch に依存するものなど）
> - 不安定な翻訳機
> - リバースエンジニアリング API に基づく翻訳機
>
> 翻訳機が要件を満たしているかどうかわからない場合は、メンテナーと議論するために issue を送信できます。

## プロジェクト構造

- **config フォルダ**：設定システム。
- **translator フォルダ**：翻訳関連の実装。
- **gui.py**：GUI インターフェースを提供。
- **const.py**：いくつかの定数。
- **main.py**：コマンドラインツールを提供。
- **high_level.py**：BabelDOC ベースの高レベルインターフェース。
- **http_api.py**：HTTP API を提供（未開始）。

Ask AI to understand the project: [DeepWiki](https://deepwiki.com/PDFMathTranslate-next/PDFMathTranslate-next)

---
- [Home](https://pdf2zh-next.com/)
- [Getting Started](https://pdf2zh-next.com/getting-started/)
  - [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html)
  - [Command Line](https://pdf2zh-next.com/getting-started/USAGE_cli.html)
  - [Usage](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
- [Language Code](https://pdf2zh-next.com/reference/LANGUAGE_CODE.html)
- [Documentation of Translation Services](https://pdf2zh-next.com/reference/TRANSLATION_SERVICES.html)
- [Advanced](https://pdf2zh-next.com/advanced/)
- [Supported Languages](https://pdf2zh-next.com/reference/SUPPORTED_LANGUAGES.html)
- [Community](https://pdf2zh-next.com/community/)
- [FAQ](https://pdf2zh-next.com/community/FAQ.html)
- [For Translators](https://pdf2zh-next.com/community/FOR_CONTRIBUTORS.html)
- [Immersive Translate](https://pdf2zh-next.com/community/IMMERSIVE_TRANSLATE.html)

---

プロジェクトを理解するために AI に質問：[DeepWiki](https://deepwiki.com/PDFMathTranslate-next/PDFMathTranslate-next)
プロジェクトを理解するために AI に質問：[DeepWiki](https://deepwiki.com/PDFMathTranslate-next/PDFMathTranslate-next)

---
- [ホーム](https://pdf2zh-next.com/)
- [始め方](https://pdf2zh-next.com/getting-started/)
  - [インストール](https://pdf2zh-next.com/getting-started/INSTALLATION.html)
  - [コマンドライン](https://pdf2zh-next.com/getting-started/USAGE_cli.html)
  - [使い方](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
- [言語コード](https://pdf2zh-next.com/reference/LANGUAGE_CODE.html)
- [翻訳サービスドキュメント](https://pdf2zh-next.com/reference/TRANSLATION_SERVICES.html)
- [高度な設定](https://pdf2zh-next.com/advanced/)
- [サポート言語](https://pdf2zh-next.com/reference/SUPPORTED_LANGUAGES.html)
- [コミュニティ](https://pdf2zh-next.com/community/)
- [よくある質問](https://pdf2zh-next.com/community/FAQ.html)
- [文書翻訳貢献ガイド](https://pdf2zh-next.com/community/FOR_CONTRIBUTORS.html)
- [没入型翻訳](https://pdf2zh-next.com/community/IMMERSIVE_TRANSLATE.html)

## お問い合わせ

ご質問がある場合は、Issue を通じてフィードバックを提出するか、Telegram グループに参加してください。ご協力ありがとうございます！

> [!TIP]
>
> [Immersive Translate](https://immersivetranslate.com) は、このプロジェクトに積極的に貢献する方々に月額プロ会員コードを提供しています。詳細については、[BabelDOC/PDFMathTranslate 貢献者報酬ルール](https://funstory-ai.github.io/BabelDOC/CONTRIBUTOR_REWARD/) をご覧ください。

<div align="right"> 
<h6><small>このページの一部のコンテンツは GPT によって翻訳されており、エラーが含まれている可能性があります。</small></h6>