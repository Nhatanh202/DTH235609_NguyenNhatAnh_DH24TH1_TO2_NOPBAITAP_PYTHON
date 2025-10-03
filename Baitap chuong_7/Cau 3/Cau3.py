from xml.dom import minidom

xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<employees>
    <employee>
        <id>1</id>
        <name>Trần Duy Thanh</name>
    </employee>
    <employee>
        <id>2</id>
        <name>Lê Hoành Sĩ</name>
    </employee>
    <employee>
        <id>3</id>
        <name>Hồ Trung Thành</name>
    </employee>
</employees>
"""

# Ghi ra file
with open("employees.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)
from xml.dom import minidom

# Đọc file XML
doc = minidom.parse("employees.xml")

# Lấy tất cả các node <employee>
employees = doc.getElementsByTagName("employee")

# In dữ liệu từng nhân viên
for emp in employees:
    emp_id = emp.getElementsByTagName("id")[0].firstChild.data
    emp_name = emp.getElementsByTagName("name")[0].firstChild.data
    print(f"ID: {emp_id} - Họ tên: {emp_name}")
