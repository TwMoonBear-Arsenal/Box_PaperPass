請求事項說明
========
> by carlton0521

# 運用構想：

I've prepared a vulnerable Ubuntu that with weak ssh password and cp-privilege vulnerabilities. I need a python test script.

# 擬請AI提供項目

* please provide a python script using pyTest to test following test cases.

## 說明：
* give detail instruction about how to use this script. especially the command to install libraries.

## 測試個案-管理設定
  * connect the ssh service  with  uid/pwd:boxadmin/boxadmin, the result should show that boxadmin is in sudo group.。

## 測試個案-外部滲透
  * connect the ssh service with  uid/pwd:allen/allen, the result should show login attempt fail.
  * connect the ssh service with  uid/pwd:allen/password, the result should show login attempt success.
  * read ~/user.txt, the result should show file access success.。

## 測試個案-內部提權
  * connect the ssh service with  uid/pwd:allen/password, the result should show login attempt success.
  * use cp-previlege escallation technology to read /root/root.txt , the result should show file access success. 

# 擬請AI作業流程

## When prepare the data:
- assume this file will be named test.py
- Write comment with traditional Chinese.
- In the file beginning, give detail instructions about how to use this file. Also tell user to use pytest -v for detail info.
- Do the work step by step. Make it easy to understand for students.

## When respond the data to me
- just show the action files only. If you need any thing for reminding, put it in the action file in comment style.

# 提供AI參考格式

```python
# 使用說明：
# 1. 將此腳本保存為 test_vulnerabilities.py。
# 2. 安裝 Python,  作法為...
# 3. 安裝 pytest, 作法為...
# 4. 安裝 paramiko, 作法為...
# 5. 在終端機中執行 pytest test_vulnerabilities.py 進行測試。

import pytest
import ...

# 指定參數
target_ip = "127.0.0.1"
target_port = 22

# 測試個案1
@pytest.fixture(params=["hello", "pytest", "12345", "空字符串"])
def string_fixture(request):
    """測試個案1：提供多個測試用例"""
    return request.param

# 測試個案2
def test_reverse_string(string, expected):
    """測試個案2：測試字符串反轉功能"""
    assert reverse_string(string) == expected, "字符串反轉結果不正確"

# 測試個案3
def test_is_substring(string_fixture):
    """測試個案3：測試子字符串檢查功能"""
    assert is_substring("hellopytest", string_fixture), f"{string_fixture} 應該是 'hellopytest' 的子字符串"
```