# pyeilcd 使用说明

[![PyPI](https://img.shields.io/pypi/v/pyeilcd.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/pyeilcd)][pypi status]

[pypi status]: https://pypi.org/project/pyeilcd/

[English](https://github.com/linancn/pyilcd/blob/main/README.md) | [中文](https://github.com/linancn/pyilcd/blob/main/README_CN.md)

**注意：** 本工具包仅支持 Python 3.8 至 3.12 版本。

## 1. 介绍

pyeilcd 是一个用于校验扩展ILCD（eILCD）XML数据文件的Python包，它基于 [pyilcd](https://github.com/brightway-lca/pyilcd) 库构建。

---

## 2. pyeilcd 使用方法

### (1) 安装说明

您可以通过 [pip] 从 [PyPI] 安装 _pyeilcd_：

```console
$ pip install pyeilcd
```

### (2) 功能

pyeilcd 主要提供以下功能：

- 根据ILCD Schema对eILCD XML文件进行格式和内容的规范性检查。

- 兼容ILCD标准定义的数据集类型，包括但不限于：ContactDataset、ProcessDataset 等。

- 底层验证逻辑基于 [pyilcd](https://github.com/brightway-lca/pyilcd) 库实现。

### (3) 使用示例

```python
from pyeilcd import validate_file_contact_dataset, Defaults

# 如有需要，可以覆盖默认设置，否则跳过。默认设置已预先配置。
Defaults.config_defaults("config.ini")  # 替换为您自己的配置文件

# 根据 ContactDataset schema验证 ContactDataset 类。
validate_file_contact_dataset("data/invalid/sample_contact_invalid.xml")  # 替换为您自己的 XML 文件
>> data/contact/sample_contact_invalid.xml:17:0:ERROR:SCHEMASV:SCHEMAV_CVC_DATATYPE_VALID_1_2_1: Element '{http://lca.jrc.it/ILCD/Common}class', attribute 'level': 'a' is not a valid value of the atomic type '{http://lca.jrc.it/ILCD/Common}LevelType'. data/contact/sample_contact_invalid.xml:17:0:ERROR:SCHEMASV:SCHEMAV_CVC_IDC: Element '{http://lca.jrc.it/ILCD/Common}class', attribute 'level': Warning: No precomputed value available, the value was either invalid or something strange happened.
```

## 3. 自动构建构建并发布（CI/CD）

本项目支持自动构建和发布，当您向 git 仓库推送以 `v版本号` 命名的 tag 时，会自动触发。例如：

```bash
# 列出已有的 tag
git tag
# 创建新 tag（例如版本 v7.0.12）
git tag v7.0.12
# 将新创建的 tag 推送到远程仓库，触发自动构建和发布
git push origin v7.0.12
```

## 4. 许可证

_pyeilcd_ 依据 GPL 3.0 协议发布，属于免费开源软件。


[pip]: https://pip.pypa.io/en/stable/
[PyPI]: https://pypi.org/project/pyeilcd/