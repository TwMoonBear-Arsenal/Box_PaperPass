請求協助事項說明
========
> by carlton0521

# 目的說明

## 未來運用構想

- I want to  use GitHub Action to check if specific files do exist in my repo.

# 擬請ChatGPT提供項目

- Please write a Github Action file contains following functions.Thank you.
  * Check "source/Cfg-Docker/dockerfile.txt" exists and not a empty file.
  * Check "source/Scr-SimpleBox/BoxSetting.sh" exists and not a empty file.

# 擬請ChatGPT作業流程

## When prepare the data:
- do the work step by step.make it easy to understand for students.
- provide clear explanation with traditional Chinese.
- give instructions about how to use this file in the beginning.

## When respond the data to me
- just show the action files only. If you need any thing for reminding, put it in the action file in comment style.

# 參考回復格式

```yaml
# 使用方式：將此檔案存放在...

name: Check File Existence

on:
  push:
    branches:
      - main

jobs:
  check_files:
    runs-on: ubuntu-latest
    steps:
      - name: Check dockerfile.txt existence and non-empty
        run: ...
          
      - name: Check BoxSetting.sh existence and non-empty
        run: ...
```