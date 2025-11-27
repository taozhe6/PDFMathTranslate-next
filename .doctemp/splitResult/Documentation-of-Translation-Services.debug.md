<!-- CHUNK ID: chunk_9221A870  CHUNK TYPE: paragraph START_LINE:1 -->
[**Advanced**](./introduction.md) > **Documentation of Translation Services** _(current)_

<!-- CHUNK ID: h_rule_8e49692a  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_7775DA81  CHUNK TYPE: header START_LINE:5 -->
### Viewing Available Translate Services via Command Line

<!-- CHUNK ID: chunk_4919DFD2  CHUNK TYPE: paragraph START_LINE:7 -->
You can confirm the available translate services and their usage by printing the help message in the command line.

<!-- CHUNK ID: chunk_756565E6  CHUNK TYPE: code_block START_LINE:9 -->
```bash
pdf2zh_next -h
```

<!-- CHUNK ID: chunk_C2A1A031  CHUNK TYPE: paragraph START_LINE:13 -->
At the end of the help message, you can view detailed information about the different translation services.


<!-- CHUNK ID: h_rule_74ef211f  CHUNK TYPE: h_rule START_LINE:16 -->
---

<!-- CHUNK ID: chunk_2DBF0B10  CHUNK TYPE: header START_LINE:18 -->
### Translation Engine Support Policy

<!-- CHUNK ID: chunk_0BB83C9D  CHUNK TYPE: header START_LINE:20 -->
#### Tier 1 (Official Support)

<!-- CHUNK ID: chunk_4E37F5F8  CHUNK TYPE: paragraph START_LINE:22 -->
**Tier 1 translation engines** are directly maintained by the project maintainers. Although the maintainers do **not use this project regularly**, they will rely on GitHub issues to identify problems. When any of these engines encounter issues, the maintainers will fix them as soon as possible to ensure stability and reliability.


Currently supported Tier 1 translation engines include:
<!-- CHUNK ID: chunk_610CC359  CHUNK TYPE: list START_LINE:26 -->
1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible

<!-- CHUNK ID: chunk_939CF562  CHUNK TYPE: header START_LINE:34 -->
#### Tier 2 (Community Support)

<!-- CHUNK ID: chunk_35662E12  CHUNK TYPE: paragraph START_LINE:36 -->
**Tier 2 translation engines** are maintained and supported by the community.  
When these engines encounter issues, the project maintainers will not provide direct fixes. Instead, they will label the related issues with `help wanted` and welcome pull requests from contributors to help resolve them.

All engines that are supported by the program but not explicitly listed under Tier 1 are considered Tier 2 translation engines.

<!-- CHUNK ID: chunk_DCD0732A  CHUNK TYPE: header START_LINE:41 -->
#### Deprecated Engines

<!-- CHUNK ID: chunk_7C961DFD  CHUNK TYPE: paragraph START_LINE:43 -->
The following translation engines have been **deprecated** and will no longer be maintained or supported:

<!-- CHUNK ID: chunk_2ADE6979  CHUNK TYPE: list START_LINE:45 -->
1. Bing
2. Google
