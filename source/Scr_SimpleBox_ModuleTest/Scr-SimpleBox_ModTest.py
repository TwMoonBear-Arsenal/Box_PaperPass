# 使用方式：
# 1. 確保Python環境已安裝pytest和paramiko。
# 2. 將此檔案存放於您的測試環境中。
# 3. 在終端機中運行命令 `pytest -v 本檔案名.py` 進行測試。

import pytest
import paramiko

# 公用連接函式
def ssh_connect(username, password, hostname="localhost", port=22):
    """使用提供的用戶名和密碼嘗試SSH連接"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port=port, username=username, password=password, timeout=10)
        return client
    except Exception as e:
        return str(e)

# 測試個案-管理設定
def test_ssh_login_as_admin():
    """測試個案：使用boxadmin/boxadmin登入，並檢查是否在sudo群組中"""
    client = ssh_connect('boxadmin', 'boxadmin')
    if isinstance(client, str):
        assert False, f"連接失敗: {client}"
    stdin, stdout, stderr = client.exec_command('groups')
    groups = stdout.read().decode().strip()
    client.close()
    assert "sudo" in groups, "boxadmin應該在sudo群組中"

# 測試個案-外部滲透
@pytest.mark.parametrize("username,password,expected", [
    ('allen', 'allen', False),
    ('allen', 'password', True)
])
def test_ssh_login_attempts(username, password, expected):
    """測試個案：外部滲透，測試不同的登入嘗試"""
    result = ssh_connect(username, password)
    if expected:
        assert isinstance(result, paramiko.SSHClient), "應能成功登入"
        result.close()
    else:
        assert isinstance(result, str), "應登入失敗"

def test_read_user_txt():
    """測試個案：讀取~/user.txt，確認文件訪問成功"""
    client = ssh_connect('allen', 'password')
    if isinstance(client, str):
        assert False, f"連接失敗: {client}"
    sftp = client.open_sftp()
    try:
        with sftp.file('user.txt', 'r') as file:
            content = file.read()
            assert content, "應能讀取user.txt文件內容"
    finally:
        sftp.close()
        client.close()

# 測試個案-內部提權
def test_cp_privilege_escalation():
    """測試個案：使用提權漏洞讀取/root/root.txt"""
    client = ssh_connect('allen', 'password')
    if isinstance(client, str):
        assert False, f"連接失敗: {client}"
    # 假設使用某個特定的漏洞提權技術，這裡需要根據具體情況修改
    stdin, stdout, stderr = client.exec_command('sudo cat /root/root.txt')
    content = stdout.read().decode().strip()
    client.close()
    assert content, "應能利用提權漏洞讀取/root/root.txt"
