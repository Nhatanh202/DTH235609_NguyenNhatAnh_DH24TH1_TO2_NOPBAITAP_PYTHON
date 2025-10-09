import csv
import os
from dataclasses import dataclass
from typing import List, Tuple, Optional
import Phuongthuc as pt

def main():
    ds_danh_muc, ds_san_pham = pt.doc_du_lieu()

    # Thêm dữ liệu mẫu nếu file trống
    if not ds_danh_muc:
        ds_danh_muc = [
            pt.DanhMuc("DM01", "Nước giải khát"),
            pt.DanhMuc("DM02", "Bánh kẹo")
        ]

    while True:
        print("\n" + "="*10 + " MENU QUẢN LÝ SẢN PHẨM " + "="*10)
        print("1. Xem danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Sửa thông tin sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("6. Sắp xếp sản phẩm")
        print("7. Lưu và Thoát")
        print("0. Thoát không lưu")
        print("="*42)
        
        lua_chon = input("Vui lòng chọn chức năng: ")

        if lua_chon == '1':
            pt.hien_thi_san_pham(ds_san_pham, ds_danh_muc)
        elif lua_chon == '2':
            pt.them_san_pham(ds_san_pham, ds_danh_muc)
        elif lua_chon == '3':
            pt.sua_san_pham(ds_san_pham, ds_danh_muc)
        elif lua_chon == '4':
            pt.xoa_san_pham(ds_san_pham)
        elif lua_chon == '5':
            pt.tim_kiem_san_pham(ds_san_pham, ds_danh_muc)
        elif lua_chon == '6':
            pt.sap_xep_san_pham(ds_san_pham, ds_danh_muc)
        elif lua_chon == '7':
            pt.luu_danh_muc(ds_danh_muc)
            pt.luu_san_pham(ds_san_pham)
            print("Đã lưu dữ liệu. Tạm biệt!")
            break
        elif lua_chon == '0':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()