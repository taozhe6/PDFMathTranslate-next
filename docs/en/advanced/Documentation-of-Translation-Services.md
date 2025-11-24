[**Advanced**](./introduction.md) > **Documentation of Translation Services** _(current)_

---

### Viewing Available Translate Services via Command Line

You can confirm the available translate services and their usage by printing the help message in the command line.

```bash
pdf2zh_next -h
```

At the end of the help message, you can view detailed information about the different translation services.


---

### Translation Engine Support Policy

#### Tier 1 (Official Support)

**Tier 1 translation engines** are directly maintained by the project maintainers. Although the maintainers do **not use this project regularly**, they will rely on GitHub issues to identify problems. When any of these engines encounter issues, the maintainers will fix them as soon as possible to ensure stability and reliability.


Currently supported Tier 1 translation engines include:
1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible

#### Tier 2 (Community Support)

**Tier 2 translation engines** are maintained and supported by the community.  
When these engines encounter issues, the project maintainers will not provide direct fixes. Instead, they will label the related issues with `help wanted` and welcome pull requests from contributors to help resolve them.

All engines that are supported by the program but not explicitly listed under Tier 1 are considered Tier 2 translation engines.

#### Deprecated Engines

The following translation engines have been **deprecated** and will no longer be maintained or supported:

1. Bing
2. Google
