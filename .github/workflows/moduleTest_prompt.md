請求事項說明
========
> by github.com/carlton0521<br/>

# 運用構想

- I need AI provide me a Github workflow file. 
- I want to use the action file to dockerize my app and test it. 

# 擬請AI提供項目

- Please write a Github workflow file, named **moduleTest**. This Github workflow file should contain following steps:
  - Use Ubuntu OS
  - Step: Package
    * Copy following repo files to a folder, named **release**:
      - **LICENSE**
      - **README.MD**
      - **src/Cfg_Docker/dockerfile**
      - **src/scr_paperPassBox/boxInitialize.sh** 
    * Package(Zip) these files and upload for later use. 
  - Step: Deploy
    * Duplicate the **release** folder as **deployment** folder
    * In the **deployment** folder:
      - use the dockerfile to build and run a container with local port **2222** bind to container port **22**.
  - Step: Test
    * Copy the **scr_paperPassBox_test** folder from repo as test folder.
    * In the test folder
      - Restore pipenv base on the Pipfile
      - Run the pipEnv shell, and use pytest test the running container.

# 擬請AI作業流程

## 通用要求:When prepare the data:
- give instructions about how to use this file in the beginning.
- do the work step by step.make it easy to understand for students.
- provide clear explanation with traditional Chinese.

## 通用要求:When respond the data to me
- just show the action files only. If you need any thing for reminding, put it in the action file in comment style.

# 提供AI參考格式

```yaml
# 此 GitHub Workflow 的功能是將指定文件複製到名為 release 的文件夾中，然後使用這些文件來構建和運行 Docker 容器，並進行測試。使用說明：
# 1. 將此文件保存為 .github/workflows/moduleTest.yml。
# 2. 當推送到 main 分支或 pull request 事件發生時，此工作流程將自動執行。

name: moduleTest

on: [push, pull_request]

jobs:
  build_and_test:
    runs-on: ubuntu-latest

    steps:
      # 取出代碼
      - name: 取出代碼
        uses: actions/checkout@v2

      # 打包文件(1/2)-蒐整檔案
      - name: 打包文件(1/2)-蒐整檔案
        run: |
          mkdir release
          cp LICENSE release/
          cp README.MD release/
          cp src/cfg_docker/dockerfile release/
          cp src/scr_paperPassBox/boxInitialize.sh release/

      # 打包檔案(2/2)-壓縮上傳
      - name: 打包檔案(2/2)-壓縮上傳
        uses: actions/upload-artifact@v4
        with:
          name: release
          path: release

      # 準備Docker受測容器
      - name: 準備Docker受測容器
        run: |
          cp -r ./release ./deployment
          cd deployment
          docker build -t myapp:latest .
          docker run -d -p 2222:22 --name myapp_container myapp:latest

      # 執行Pytest測試個案(1/3)-安裝Python(須配合pipenv版本)
      - name: 執行Pytest測試個案(1/3)-安裝Python(須配合pipenv版本)
        uses: actions/setup-python@v2
        with:
          python-version: '3.10.10'

      # 執行Pytest測試(2/3)-安裝pipenv並復原虛擬環境
      - name: 執行Pytest測試(2/3)-安裝pipenv並復原虛擬環境
        run: |
          cp -R src/scr_paperPassBox_test test
          cd test
          pip install pipenv
          pipenv install --deploy --ignore-pipfile

      # 執行Pytest測試(3/3)-執行Pytest測試
      - name: 執行Pytest測試(3/3)-執行Pytest測試
        run: |
          pipenv run pytest
```