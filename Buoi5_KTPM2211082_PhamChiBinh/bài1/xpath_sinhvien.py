from lxml import etree

# ======== ĐỌC FILE SINHVIEN.XML ========
tree = etree.parse("sinhvien.xml")
root = tree.getroot()

def show(title, result):
    print(f"\n-- {title} --")
    if isinstance(result, list):
        for r in result:
            if isinstance(r, etree._Element):
                print(etree.tostring(r, pretty_print=True, encoding='unicode').strip())
            else:
                print(r)
    else:
        print(result)

# ======== DANH SÁCH CÂU TRUY VẤN XPATH ========
queries = [
    ("Lấy tất cả sinh viên", "//student"),
    ("Liệt kê tên tất cả sinh viên", "//student/name/text()"),
    ("Lấy tất cả id của sinh viên", "//student/id/text()"),
    ("Lấy ngày sinh của SV có id='SV01'", "//student[id='SV01']/date/text()"),
    ("Lấy tất cả khóa học", "//course/text()"),
    ("Lấy toàn bộ thông tin của sinh viên đầu tiên", "(//student)[1]"),
    ("Lấy mã SV đăng ký khóa học 'Vatly203'", "//enrollment[course='Vatly203']/studentRef/text()"),
    ("Lấy tên SV học môn 'Toan101'", "//student[id=//enrollment[course='Toan101']/studentRef]/name/text()"),
    ("Lấy tên SV học môn 'Vatly203'", "//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()"),
    ("Lấy tên và ngày sinh của SV sinh năm 1997", "//student[starts-with(date,'1997')]"),
    ("Lấy tên của SV sinh trước năm 1998", "//student[number(substring(date,1,4))<1998]/name/text()"),
    ("Đếm tổng số sinh viên", "count(//student)"),
    ("Lấy SV chưa đăng ký môn học nào", "//student[not(id=//enrollment/studentRef)]/name/text()"),
    ("Lấy phần tử <date> ngay sau <name> của SV01", "//student[id='SV01']/name/following-sibling::date[1]/text()"),
    ("Lấy phần tử <id> ngay trước <name> của SV02", "//student[id='SV02']/name/preceding-sibling::id[1]/text()"),
    ("Lấy toàn bộ node <course> trong enrollment của SV03", "//enrollment[studentRef='SV03']/course"),
    ("Lấy SV có họ 'Lê'", "//student[starts-with(name,'Lê')]/name/text()"),
    ("Lấy năm sinh của SV01", "substring(//student[id='SV01']/date,1,4)")
]

# ======== THỰC THI CÁC TRUY VẤN ========
print("=== KẾT QUẢ TRUY VẤN TRÊN FILE SINHVIEN.XML ===")
for title, expr in queries:
    try:
        result = root.xpath(expr)
        show(title, result)
    except etree.XPathEvalError as e:
        print(f"Lỗi XPath ở '{title}': {e}")
