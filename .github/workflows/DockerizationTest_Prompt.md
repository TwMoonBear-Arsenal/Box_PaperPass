請求事項說明
========
> by carlton0521

# 運用構想

- I need ChatGPT provide me a Github action file. 
- I want to use the action file to test if my dockerfile works well. 

# 擬請AI提供項目

- Please write a Github Action file contains following functions.Thank you.
  * name the action as "DockerizationTest".
  * set this action workflow_run after the "BuildTest" workflow is complete.
  * Copy the "source/Scr_SimpleBox/BoxSetting.sh" and "source/Cfg_Docker/dockerfile" to same work folder.
  * test whether the dockerfile works well.

# 擬請AI作業流程

## When prepare the data:
- give instructions about how to use this file in the beginning.
- do the work step by step.make it easy to understand for students.
- provide clear explanation with traditional Chinese.

## When respond the data to me
- just show the action files only. If you need any thing for reminding, put it in the action file in comment style.

# 提供AI參考格式

```yaml
# 使用方式：
# 1 將此檔案存放在...
# 2 然後...

name: ...
on:
  push:
    branches:
      - main

jobs:
  check_files:
    runs-on: ubuntu-latest
    steps:
      - name: 
```