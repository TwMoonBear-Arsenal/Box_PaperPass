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
    * Copy following repo files to a folder, named **releasePackage**:
      - **LICENSE**
      - **README.MD**
      - **source/Cfg_Docker/dockerfile**
      - **source/Scr_SimpleDemoBox/SimpleDemoBox.sh** 
    * Package(Zip) these files and upload for later use. 
  - Step: Deploy
    * Duplicate the **releasePackage** folder as **deployment** folder
    * In the **deployment** folder:
      - use the dockerfile to build and run a container with local port **2222** bind to container port **22**.
  - Step: Test
    * Copy the **Scr_PaperPassBox_Test** folder from repo as test folder.
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
# 此 GitHub Workflow 的功能是將指定文件複製到名為 releasePackage 的文件夾中，然後使用這些文件來構建和運行 Docker 容器，並進行測試。使用說明：
# 1. 將此文件保存為 .github/workflows/moduleTest.yml。
# 2. 當推送到 main 分支或 pull request 事件發生時，此工作流程將自動執行。

name: moduleTest

on: [push, pull_request]

jobs:
  build_and_test:
    runs-on: ubuntu-latest

    steps:
      # 檢出代碼
      - name: 檢出代碼
        uses: actions/checkout@v2

      # 打包步驟
      - name: 打包文件
        run: |
          mkdir releasePackage
          cp LICENSE README.md source/Cfg_Docker/dockerfile source/Scr_SimpleDemoBox/SimpleDemoBox.sh releasePackage/
          zip -r releasePackage.zip releasePackage/

      # 上傳打包文件
      - name: 上傳打包文件
        uses: actions/upload-artifact@v4
        with:
          name: releasePackage
          path: releasePackage.zip

      # 部署及執行Docker容器
      - name: 部署及執行 Docker 容器
        run: |
          mkdir deployment
          unzip releasePackage.zip -d deployment
          cd deployment/releasePackage
          docker build -t myapp:latest .
          docker run -d -p 2222:22 --name myapp_container myapp:latest

      # 準備測試環境
      - name: 準備 Python 測試環境
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      # 執行測試
      - name: 執行測試
        run: |
          cp -R source/Scr_PaperPassBox_Test test
          cd test
          pip install pipenv
          pipenv install --deploy --ignore-pipfile
          pipenv run pytest
```