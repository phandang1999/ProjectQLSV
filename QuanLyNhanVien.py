from abc import ABC, abstractmethod

class absNhanVien(ABC):
    @abstractmethod
    def tinhLuongHT(self):
        pass
    @abstractmethod
    def xuatTT(self):
        pass

class NhanVien(absNhanVien):
    def __init__(self, maNV, hoTen, luongCB):
        self._maNV = maNV
        self._hoTen = hoTen
        self._luongCB = luongCB
        self._luongHT = 0
    def tinhLuongHT(self):
        pass
    def xuatTT(self):
        pass

class NVVanPhong(NhanVien):
    def __init__(self, maNV, hoTen, luongCB, **kwargs):
        super().__init__(maNV, hoTen, luongCB)
        self.__soGL = kwargs.get('soGL', 0)

    def getmaNV(self):
        return self._maNV
    def setmaNV(self, maNV):
        self._maNV = maNV

    def getluongCB(self):
        return self._luongCB
    def setluongCB(self, luongCB):
        self._luongCB = luongCB

    def getluongHT(self):
        return self._luongHT
    def setluongHT(self, luongHT):
        self._luongHT = luongHT

    def getSoGL(self):
        return self.__soGL
    def setSoGL(self, soGL):
        self.__soGL = soGL

    def tinhluongHT(self):
        if (self.__soGL > 100):
            luong = self._luongCB + self.__soGL*150_000 + 5_000_000
        else:
            luong = self._luongCB + self.__soGL * 150_000
        self._luongHT = luong
        return luong
    def xuatTT(self):
        print("Thông tin nhân viên văn phòng:")
        print("\t+ Mã nhân viên:", self._maNV,)
        print("\t+ Họ tên:", self._hoTen,)
        print("\t+ Lương cơ bản:", self._luongCB,)
        print("\t+ Lương hằng tháng:", self._luongHT,)
        print("\t+ Số giờ làm:", self.__soGL,)

class NVSanXuat(NhanVien):
    def __init__(self, maNV, hoTen, luongCB, **kwargs):
        super().__init__(maNV, hoTen, luongCB)
        self.__soSP = kwargs.get('soSP', 0)

    def getmaNV(self):
        return self._maNV
    def setmaNV(self, maNV):
        self._maNV = maNV

    def getluongCB(self):
        return self._luongCB
    def setluongCB(self, luongCB):
        self._luongCB = luongCB

    def getluongHT(self):
        return self._luongHT
    def setluongHT(self, luongHT):
        self._luongHT = luongHT

    def getSP(self):
        return self.__soSP
    def setSoSP(self, soSP):
        self.__soSP = soSP

    def tinhluongHT(self):
        if (self.__soSP > 150):
            luong = (self._luongCB + self.__soSP*175_000)*1.2
        else:
            luong = self._luongCB + self.__soSP*175_000
        self._luongHT = luong
        return luong
    def xuatTT(self):
        print("Thông tin nhân viên sản xuất:")
        print("\t+ Mã nhân viên:", self._maNV)
        print("\t+ Họ tên:", self._hoTen,)
        print("\t+ Lương cơ bản:", self._luongCB)
        print("\t+ Lương hằng tháng:", self._luongHT)
        print("\t+ Số sản phẩm:", self.__soSP)

class NVQuanLy(NhanVien):
    def __init__(self, maNV, hoTen, luongCB, **kwargs):
        super().__init__(maNV, hoTen, luongCB)
        self.__heSoCV = kwargs.get('heSoCV', 0)
        self.__thuong = kwargs.get('thuong', 0)

    def getmaNV(self):
        return self._maNV
    def setmaNV(self, maNV):
        self._maNV = maNV

    def getluongCB(self):
        return self._luongCB
    def setluongCB(self, luongCB):
        self._luongCB = luongCB

    def getluongHT(self):
        return self._luongHT
    def setluongHT(self, luongHT):
        self._luongHT = luongHT

    def getHeSoCV(self):
        return self.__heSoCV
    def setHeSoCV(self, heSoCV):
        self.__heSoCV = heSoCV

    def getThuong(self):
        return self.__thuong
    def setThuong(self, thuong):
        self.__thuong = thuong

    def tinhluongHT(self):
        luong = (self._luongCB*self.__heSoCV + self.__thuong)*1.2
        self._luongHT = luong
        return luong
    def xuatTT(self):
        print("Thông tin nhân viên quản lý:")
        print("\t+ Mã nhân viên:", self._maNV)
        print("\t+ Họ tên:", self._hoTen)
        print("\t+ Lương cơ bản:", self._luongCB)
        print("\t+ Lương hằng tháng:", self._luongHT)
        print("\t+ Hệ số chức vụ:", self.__heSoCV)
        print("\t+ Thưởng:", self.__thuong)

class DaiLy:
    def __init__(self, maDL, tenDL):
        self.__maDL = maDL
        self.__tenDL = tenDL
        self.__ds = []

    def loadNV(self):
        vp1 = NVVanPhong(101, 'Nguyễn A', 4_500_000, soGL=200)
        vp2 = NVVanPhong(102, 'Nguyễn B', 5_600_000, soGL=100)
        vp3 = NVVanPhong(103, 'Nguyễn C', 8_900_000, soGL=90)

        sx1 = NVSanXuat(201, 'Nguyễn D', 7_800_000, soSP=250)
        sx2 = NVSanXuat(202, 'Nguyễn E', 4_500_000, soSP=110)
        sx3 = NVSanXuat(203, 'Nguyễn F', 6_600_000, soSP=360)

        ql1 = NVQuanLy(301, 'Nguyễn G', 8_500_000, heSoCV=1.3, thuong=19_500_000)
        ql2 = NVQuanLy(302, 'Nguyễn H', 7_600_000, heSoCV=1.2, thuong=18_600_000)
        self.__ds.extend([vp1, vp2, vp3, sx1, sx2, sx3, ql1, ql2])

    def showDsNV(self):
        for nv in self.__ds:
            nv.xuatTT()
    def show1NV(self, nv):
        nv.xuatTT()
    def tinhLuongHT(self):
        for nv in self.__ds:
            nv.tinhluongHT()

    def tinhLuongHT1NV(self, nv):
        nv.tinhluongHT()
    def searchNV(self, maNVSeach):
        for nv in self.__ds:
            if nv.getmaNV() == maNVSeach:
                return nv
    def tinhTBLuongHT(self):
        tongLuongHT = 0
        for nv in self.__ds:
            tongLuongHT += nv.getluongHT()
        luongTBHT = tongLuongHT / len(self.__ds)
        return luongTBHT
    def uploadLuongCBNV(self, maNVUpload, luongCBUpload):
        for nv in self.__ds:
            if nv.getmaNV() == maNVUpload:
                nv.setluongCB(luongCBUpload)
                return nv

if __name__ == '__main__':
    dl = DaiLy(22210040, 'PNND')
    #Câu 1
    print("----------------------------Câu 1---------------------------------")
    print("Load dữ liệu nhân viên")
    dl.loadNV()
    #Câu 2
    print("----------------------------Câu 2---------------------------------")
    dl.showDsNV()
    #Câu 3
    print("----------------------------Câu 3---------------------------------")
    dl.tinhLuongHT()
    dl.showDsNV()
    #Câu 4
    print("----------------------------Câu 4---------------------------------")
    maNVCanTim = 101
    print('Nhân viên cần tìm có mã NV', maNVCanTim)
    dl.show1NV(dl.searchNV(maNVCanTim))
    #Câu 5
    print("----------------------------Câu 5---------------------------------")
    print('Lương TB hằng tháng mà đại lý trả cho NV:', dl.tinhTBLuongHT())
    #Câu6
    print("----------------------------Câu 6---------------------------------")
    maNVVPCanUpload = 101
    luongCBCanUpload = 7_700_000
    print('Nhân viên có mã số NV', maNVVPCanUpload, 'cần Upload lương CB')
    nv = dl.uploadLuongCBNV(maNVVPCanUpload, luongCBCanUpload)
    dl.tinhLuongHT1NV(nv)
    dl.show1NV(nv)

