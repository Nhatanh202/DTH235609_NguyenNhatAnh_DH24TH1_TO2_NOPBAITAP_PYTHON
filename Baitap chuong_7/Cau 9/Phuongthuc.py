import csv
import os

# Simple classes for categories and products
class DanhMuc:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class SanPham:
    def __init__(self, ma, ten, don_gia, ma_danh_muc):
        self.ma = ma
        self.ten = ten
        self.don_gia = don_gia
        self.ma_danh_muc = ma_danh_muc

# File paths (same folder as script)
BASE_DIR = os.path.dirname(__file__)
DM_FILE = os.path.join(BASE_DIR, "danh_muc.csv")
SP_FILE = os.path.join(BASE_DIR, "san_pham.csv")

def doc_du_lieu():
    """Đọc dữ liệu từ file CSV và trả về danh sách danh mục và sản phẩm"""
    ds_danh_muc = []
    ds_san_pham = []

    # Đọc danh mục
    if os.path.exists(DM_FILE):
        try:
            with open(DM_FILE, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        ds_danh_muc.append(DanhMuc(row[0], row[1]))
        except Exception:
            pass

    # Đọc sản phẩm
    if os.path.exists(SP_FILE):
        try:
            with open(SP_FILE, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 4:
                        try:
                            don_gia = float(row[2])
                        except ValueError:
                            don_gia = 0.0
                        ds_san_pham.append(SanPham(row[0], row[1], don_gia, row[3]))
        except Exception:
            pass

    return ds_danh_muc, ds_san_pham

def hien_thi_san_pham(ds_san_pham, ds_danh_muc):
    """Hiển thị danh sách sản phẩm"""
    # Tạo dictionary map mã danh mục -> tên danh mục
    dm_map = {}
    for dm in ds_danh_muc:
        dm_map[dm.ma] = dm.ten
    
    if not ds_san_pham:
        print("Không có sản phẩm nào.")
        return
    
    print("{0:10} {1:30} {2:10} {3:15}".format('Mã', 'Tên', 'Đơn giá', 'Danh mục'))
    print("-" * 70)
    for sp in ds_san_pham:
        ten_dm = dm_map.get(sp.ma_danh_muc, "N/A")
        print("{0:10} {1:30} {2:10.2f} {3:15}".format(sp.ma, sp.ten, sp.don_gia, ten_dm))

def them_san_pham(ds_san_pham, ds_danh_muc):
    """Thêm sản phẩm mới"""
    ma = input("Nhập mã sản phẩm: ").strip()
    
    # Kiểm tra mã đã tồn tại
    for sp in ds_san_pham:
        if sp.ma == ma:
            print("Mã đã tồn tại.")
            return
    
    ten = input("Nhập tên sản phẩm: ").strip()
    
    try:
        don_gia = float(input("Nhập đơn giá: ").strip())
    except ValueError:
        don_gia = 0.0
    
    print("Danh mục hiện có:")
    for dm in ds_danh_muc:
        print("{0}: {1}".format(dm.ma, dm.ten))
    
    ma_dm = input("Nhập mã danh mục: ").strip()
    ds_san_pham.append(SanPham(ma, ten, don_gia, ma_dm))
    print("Đã thêm sản phẩm.")

def sua_san_pham(ds_san_pham, ds_danh_muc):
    """Sửa thông tin sản phẩm"""
    ma = input("Nhập mã sản phẩm cần sửa: ").strip()
    
    for sp in ds_san_pham:
        if sp.ma == ma:
            print("Sửa sản phẩm {0} - {1}".format(sp.ma, sp.ten))
            
            ten_moi = input("Tên mới ({0}): ".format(sp.ten)).strip()
            if ten_moi:
                sp.ten = ten_moi
            
            try:
                don_gia_input = input("Đơn giá mới ({0}): ".format(sp.don_gia)).strip()
                if don_gia_input:
                    sp.don_gia = float(don_gia_input)
            except ValueError:
                pass
            
            print("Danh mục hiện có:")
            for dm in ds_danh_muc:
                print("{0}: {1}".format(dm.ma, dm.ten))
            
            ma_dm_moi = input("Mã danh mục mới ({0}): ".format(sp.ma_danh_muc)).strip()
            if ma_dm_moi:
                sp.ma_danh_muc = ma_dm_moi
            
            print("Đã cập nhật sản phẩm.")
            return
    
    print("Không tìm thấy sản phẩm.")

def xoa_san_pham(ds_san_pham):
    """Xóa sản phẩm"""
    ma = input("Nhập mã sản phẩm cần xóa: ").strip()
    
    for i in range(len(ds_san_pham)):
        if ds_san_pham[i].ma == ma:
            confirm = input("Xóa sản phẩm {0}? (y/n): ".format(ds_san_pham[i].ten)).strip().lower()
            if confirm == 'y':
                ds_san_pham.pop(i)
                print("Đã xóa.")
            else:
                print("Hủy xóa.")
            return
    
    print("Không tìm thấy sản phẩm.")

def tim_kiem_san_pham(ds_san_pham, ds_danh_muc):
    """Tìm kiếm sản phẩm theo mã hoặc tên"""
    kw = input("Nhập từ khóa tìm kiếm (mã hoặc tên): ").strip().lower()
    
    ketqua = []
    for sp in ds_san_pham:
        if kw in sp.ma.lower() or kw in sp.ten.lower():
            ketqua.append(sp)
    
    if not ketqua:
        print("Không tìm thấy sản phẩm phù hợp.")
        return
    
    hien_thi_san_pham(ketqua, ds_danh_muc)

def sap_xep_san_pham(ds_san_pham, ds_danh_muc):
    """Sắp xếp sản phẩm theo tiêu chí"""
    print("Sắp xếp theo: 1. Mã  2. Tên  3. Đơn giá")
    ch = input("Chọn: ").strip()
    
    if ch == '1':
        ds_san_pham.sort(key=lambda x: x.ma)
    elif ch == '2':
        ds_san_pham.sort(key=lambda x: x.ten)
    elif ch == '3':
        ds_san_pham.sort(key=lambda x: x.don_gia)
    else:
        print("Lựa chọn không hợp lệ.")
        return
    
    print("Đã sắp xếp.")
    hien_thi_san_pham(ds_san_pham, ds_danh_muc)

def luu_danh_muc(ds_danh_muc):
    """Lưu danh sách danh mục vào file CSV"""
    try:
        with open(DM_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for dm in ds_danh_muc:
                writer.writerow([dm.ma, dm.ten])
    except Exception as e:
        print("Lỗi khi lưu danh mục:", e)

def luu_san_pham(ds_san_pham):
    """Lưu danh sách sản phẩm vào file CSV"""
    try:
        with open(SP_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for sp in ds_san_pham:
                writer.writerow([sp.ma, sp.ten, "{0:.2f}".format(sp.don_gia), sp.ma_danh_muc])
    except Exception as e:
        print("Lỗi khi lưu sản phẩm:", e)