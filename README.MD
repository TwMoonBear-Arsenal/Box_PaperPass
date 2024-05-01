Paper Pass Box
====
> Asst. Prof. Carlton.Chen

* Static Info:
  ![版權宣告](https://img.shields.io/github/license/TwMoonBear-Arsenal/Box_PaperPass)
  ![Bash使用](https://img.shields.io/badge/Bash_Script-2A2Ba2)
  ![Docker使用](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
  ![Python使用](https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white)
* Development:
  [![可維護度](https://api.codeclimate.com/v1/badges/da0c547d8c6236d10e0e/maintainability)](https://codeclimate.com/github/TwMoonBear-Arsenal/Box_PaperPass/maintainability)
  ![GitHub repo size](https://img.shields.io/github/repo-size/TwMoonBear-Arsenal/Box_PaperPass)
  ![GitHub Tag](https://img.shields.io/github/v/tag/TwMoonBear-Arsenal/Box_PaperPass)
  ![釋出版本](https://img.shields.io/github/v/release/TwMoonBear-Arsenal/Box_PaperPass)
  ![釋出日期](https://img.shields.io/github/release-date/TwMoonBear-Arsenal/Box_PaperPass)

# 摘要說明

* 提供一組Docker相關腳本，運行腳本後可建立簡單紅隊靶機，作為示範教學使

# 項目介紹

* Release Assets
  - **BoxSetting.sh**：將Ubuntu設定ssh弱密碼及cp提權弱點，可做為簡單滲透提權使用。
  - **DockerFile**：可初始化一個Ubuntu容器，並將上述**BashScript**複製進去後執行。

# 運用流程

## 一、模組設計

設計(滾修)後直接於Readme註記。

## 二、模發測佈

### (一)測試準備

* 於develop branch更新。
* 配合統一性，使用Python+Pipenv。
* 省略未做單元測試，僅做黑箱模組測試。
  1. 個案：**BoxAdmin**可遠端連線**BoxContainer**並具備管理權。
  2. 個案：**BoxUser**可遠端連線**BoxContainer**並以弱密碼(password)登入後，讀取user.flag。
  3. 個案：**BoxUser**可遠端連線**BoxContainer**登入後，操作cp提權讀取root.flag。

### (二)模組發展

* 主要編寫bash腳本用以初始化靶機。
* 開發中配合已設定之策試Gtihub Workflow進行測試。

### (三)併版發佈

* 本專案設為公開專案，有設定main protection，以pull request併入main。
* 檢核後手動發佈
