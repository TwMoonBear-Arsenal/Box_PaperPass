# Dockerfile 說明
# 本 Dockerfile 用於建立一個具有基本漏洞的 Ubuntu 環境，適用於教學目的。
# 使用前，請確保 boxsetting.sh 文件和 Dockerfile 位於同一目錄下。
# 在終端機中執行以下指令來構建 Docker 映像：
# docker build -t vulnerable-ubuntu .
# 構建完成後，可以使用以下指令來啟動容器：
# docker run -d -p 22:22 -p 9527:9527 vulnerable-ubuntu
# 這樣將映射容器的 22 和 9527 端口到本機的相應端口。

# 設定基底容器
# 選用最新且體積小的 Ubuntu 基底映像檔
FROM ubuntu:latest
# 更新 Ubuntu 套件清單，確保安裝時使用最新版本的軟體
RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# 複製檔案及初始化設定
# 複製 boxsetting.sh 腳本到容器的 root 家目錄
COPY boxsetting.sh /root/boxsetting.sh
# 給予 boxsetting.sh 執行權限
RUN chmod +x /root/boxsetting.sh
# 執行 boxsetting.sh 來設定 Ubuntu
RUN /root/boxsetting.sh

# 設定網路
# EXPOSE 指令用於宣告容器將使用哪些網路端口
EXPOSE 22 9527

# 設定容器啟動時執行的命令
# 這裡設定為啟動 bash，讓容器保持運行
CMD ["bash"]
