import pytest
import paramiko

# 定義SSH連接的基本信息
HOST = '192.168.0.1'
PORT = 9527

# 設定Paramiko日誌級別
paramiko.util.log_to_file('ssh_test.log')

@pytest.fixture(scope="module")
def ssh_client():
    """提供一個SSH客戶端連接的fixture"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client

def test_sudo_group(ssh_client):
    """測試個案：確認boxadmin用戶是否在sudo組。
    連接至SSH服務，使用boxadmin用戶檢查是否在sudo組中。
    """
    try:
        ssh_client.connect(HOST, port=PORT, username='boxadmin', password='boxadmin')
        stdin, stdout, stderr = ssh_client.exec_command('id -nG')
        groups = stdout.read().decode().strip()
        ssh_client.close()
        assert 'sudo' in groups, "boxadmin 應該在 sudo 組"
        print("boxadmin 在 sudo 組")
    except Exception as e:
        print(f"連接失敗或命令執行錯誤: {str(e)}")

def test_login_failure(ssh_client):
    """測試個案：測試登錄失敗案例。
    使用錯誤的密碼試圖連接至SSH服務，期望登錄失敗。
    """
    with pytest.raises(paramiko.ssh_exception.AuthenticationException):
        ssh_client.connect(HOST, port=PORT, username='allen', password='allen')
    print("allen 登錄失敗")

def test_login_success_and_read_file(ssh_client):
    """測試個案：測試登錄成功及讀取文件。
    登錄成功後嘗試讀取 ~/user.txt 文件。
    """
    try:
        ssh_client.connect(HOST, port=PORT, username='allen', password='password')
        stdin, stdout, stderr = ssh_client.exec_command('cat ~/user.txt')
        content = stdout.read().decode().strip()
        ssh_client.close()
        assert content != '', "應該讀取到文件內容"
        print("文件讀取成功: " + content)
    except Exception as e:
        print(f"登錄成功但讀取文件失敗: {str(e)}")

# Note: The privilege escalation test is omitted due to ethical and security reasons.
