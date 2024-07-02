# 파이썬 DB 연동 프로그램

import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import webbrowser

from PyQt5.QtWidgets import QWidget

## MSSQL 연동할 라이브러리 (모듈)
import pymssql

## 전역 변수 (나중에 변경시 여기만 변경하면 됨)
serverName = '127.0.0.1'
userId = 'sa'
userPass = 'mssql_p@ss'
dbName = 'Madang'
dbCharset = 'UTF8'
# 저장버튼 클릭시 삽입, 수정을 구분 짓기
mode = 'I' # I : Insert   ,  U : Update

class qtApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./aaaa/MadangBook.ui',self)
        self.initUI()

    def initUI(self)-> None:
        # 입력제한
        self.txtBookid.setValidator(QIntValidator(self)) # 숫자만 입력하도록 제한
        self.txtPrice.setValidator(QIntValidator(self)) # 숫자만 입력하도록 제한
        # Button 4개에 대해서 사용등록
        self.btnNew.clicked.connect(self.btnNewClicked) # 신규
        self.btnSave.clicked.connect(self.btnSaveClicked) # 저장
        self.btnDel.clicked.connect(self.btnDelClicked) # 삭제
        self.btnReload.clicked.connect(self.btnReloadClicked) # 조회버튼
        self.tblBooks.itemSelectionChanged.connect(self.tblBooksSelected) # 테이블 위젯 결과를 클릭시 발생
        self.show()

        self.btnReloadClicked()

    def btnNewClicked(self): # 신규버튼 클릭
        global mode
        mode = 'I'
        self.txtBookid.setText('')
        self.txtBookName.setText('')
        self.txtPublisher.setText('')
        self.txtPrice.setText('')
        # 선택한 데이터에서 신규를 누르면 self.txtBookId 사용여부는 변경해줘야함
        self.txtBookid.setEnabled(True) # 사용 

    def btnSaveClicked(self): # 저장버튼 클릭
        # 입력 검증(Validation Check) 을 반드시 해야함
        # 1. 텍스트 박스를 비워두고 저장버튼 누르면 안되요!!
        bookid = self.txtBookid.text()
        bookName = self.txtBookName.text()
        publisher = self.txtPublisher.text()
        price = self.txtPrice.text()

        warningMsg = ''
        isValid = True # 빈 값이 있으면 False로 변경
        if bookid == None or bookid == '':
            warningMsg += '책 번호가 없습니다.\n'
            isValid = False
        if bookName == None or bookName == '':
            warningMsg += '책 제목이 없습니다.\n'
            isValid = False
        if publisher == None or publisher == '':
            warningMsg += '출판사가 없습니다.\n'
            isValid = False   
        if price == None or price == '':
            warningMsg += '정가가 없습니다.\n'
            isValid = False  

        if isValid == False : # 위 입력값중에 하나라도 빈값이라면
            QMessageBox.warning(self,'저장 경고', warningMsg)
            return
            

        ## mode = 'I'일떄는 중복번호를 체크 해야하지만, mode = 'U'일떄는 체크해서 막으면 수정 자체가 안됨
        if mode == 'I': # INSERT
        # 2. 현재 존재하는 번호를 사용했는지 체크, 이미 있는 번호면 DB 입력 쿼리 실행이 안되도록 막아야함
            conn = pymssql.connect(server = serverName, user = userId, password = userPass, database = dbName, charset = dbCharset)
            cursor = conn.cursor(as_dict = False)  # COUNT(*)는 데이터가 딱 1개이기 떄문에 as_dict = False로 해야함
            query = f'''SELECT COUNT(*)
                        FROM Book
                        WHERE bookid = {bookid} 
                    ''' # 현재 입력하고자 하는 번호가 있는지 확인하는 쿼리
            cursor.execute(query)
            #print(cursor.fetchone()[0]) # COUNT(*)는 데이터가 딱 1개이기 떄문에 cursor.fetchone() 함수로 (1, ) 튜플을 가져옴
            valid = cursor.fetchone()[0]
            conn.close()
            if valid == 1 : # DB Book 테이블에 같은 번호가 이미 존재
                QMessageBox.warning(self,'저장 경고', '이미 같은 번호의 데이터가 존재합니다!! \n 번호를 변경하세요')
                return # 함수 탈출!!
  
        ## 3. 입력검증 후 DB Book테이블에 삽입 시작!
        # bookid, bookName, publisher, price
        if mode == 'I':
            query = f'''
                    INSERT INTO Book
                    VALUES ({bookid},N'{bookName}',N'{publisher}',{price})
                    '''
        elif mode == 'U':
            query = f'''
                        UPDATE Book
                        SET bookname = N'{bookName}'
                        , publisher = N'{publisher}'
                        , price = {price}
                        WHERE bookid = {bookid}
                     '''
        conn = pymssql.connect(server = serverName, user = userId, password = userPass, database = dbName, charset = dbCharset)
        cursor = conn.cursor(as_dict = False) # INSERT는 데이터를 가져오는게 아니라서 
    
        try:
            cursor.execute(query)
            conn.commit() # 저장을 확립

            if mode == 'I':
                QMessageBox.about(self,'저장성공', '데이터를 저장했습니다')
            else:
                QMessageBox.about(self,'수정성공', '데이터를 수정했습니다')

        except Exception as e:
            QMessageBox.warning(self,'저장 실패',f'{e}')
            conn.rollback() # 원상복귀
        finally:
            conn.close() #오류가 나든 안나든, DB는 닫는다

        self.btnReloadClicked()

    def btnDelClicked(self): # 삭제버튼 클릭
        # 삭제기능
        bookid = self.txtBookid.text()
        print(bookid)
        # Validation Check
        if bookid == None or bookid == '':
            QMessageBox.warning(self, '삭제경고', '책 번호 없이 삭제할 수 없습니다.')
            return
        
        re = QMessageBox.question(self,'삭제 경고', '정말로 삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.No:
            return

        conn = pymssql.connect(server = serverName,user = userId, password = userPass,database = dbName, charset = dbCharset)
        cursor = conn.cursor(as_dict=False) # INSERT는 데이터를 가져오는게 아니라서
        query = f'''DELETE FROM Book
                      WHERE bookid = {bookid}
                  '''
        
        try:
            cursor.execute(query)
            conn.commit()

            QMessageBox.about(self, '삭제성공', '데이터를 삭제했습니다.')
        except Exception as e:
            QMessageBox.warning(self, '삭제실패', f'{e}')
            conn.rollback()
        finally:
            conn.close()

        self.btnReloadClicked() # 삭제 후에도 재조회 해야함

    def btnReloadClicked(self): # 조회버튼 클릭
        lstResult = []
        conn = pymssql.connect(server = serverName, user = userId, password = userPass, database = dbName, charset = dbCharset)
        cursor = conn.cursor(as_dict = True)

        query = '''
                SELECT bookid
                , bookname
                , publisher
                , ISNULL(FORMAT(price, '#,#'),'0')AS price
                FROM Madang.dbo.Book
            
                '''
        
        cursor.execute(query)
        for row in cursor:
            #print(f'bookid = {row["bookid"]}, bookname = {row["bookname"]}, publisher = {row["publisher"]}, price = {row["price"]}')
            # dictionary 로 만든 결과를 lstResult에 append 하기
            temp = {'bookid' : row['bookid'], 'bookname' : row['bookname'], 'publisher' : row['publisher'], 'price': row['price']}
            lstResult.append(temp)

        conn.close() # DB는 접속해서 일이 끝나면 무조건 닫는다!!
        #print(lstResult)
        self.makeTable(lstResult)

    def makeTable(self, data): # tblBooks 위젯을 데이터와 컬럼 생성해주는 함수
        self.tblBooks.setColumnCount(4) # bookid, bookname, publisher, price
        self.tblBooks.setRowCount(len(data)) # 조회에서 나온 리스트 갯수로 결정
        self.tblBooks.setHorizontalHeaderLabels(['책 번호', '책 제목', '출판사', '정가'])

        n = 0
        for item in data:
            # print(item)
            idItem = QTableWidgetItem(str(item['bookid']))
            idItem.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            priceItem = QTableWidgetItem(str(item['price']))
            priceItem.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

            self.tblBooks.setItem(n, 0, idItem)   # set(row, column, text)
            self.tblBooks.setItem(n, 1, QTableWidgetItem(item['bookname'])) 
            self.tblBooks.setItem(n, 2, QTableWidgetItem(item['publisher'])) 
            self.tblBooks.setItem(n, 3, priceItem) 
            n += 1
        
        self.tblBooks.setColumnWidth(0,65)  # 책번호 컬럼 넓이
        self.tblBooks.setColumnWidth(1,230)
        self.tblBooks.setColumnWidth(2,130)
        self.tblBooks.setColumnWidth(3,80)
        # 컬럼 더블클릭은 금지 시켜야함!! -- 변경 방지
        self.tblBooks.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def tblBooksSelected(self): # 조회버튼 클릭1
        rowIndex = self.tblBooks.currentRow() # 현재 마우스로 선택된 행의 인덱스
 
        bookId = self.tblBooks.item(rowIndex, 0).text() # 책 번호
        bookName = self.tblBooks.item(rowIndex, 1).text() # 책 제목
        publisher = self.tblBooks.item(rowIndex, 2).text() # 출판사
        price = self.tblBooks.item(rowIndex, 3).text().replace(',','')  # 가격
        # print(bookId, bookName, publisher, price)
        # 지정된 lineEdit(TextBox)에 할당 
        self.txtBookid.setText(bookId)
        self.txtBookName.setText(bookName)
        self.txtPublisher.setText(publisher)
        self.txtPrice.setText(price)

        # 모드를 UPDATE로 변경
        global mode # 전역변수를 내부에서 사용하겠다.
        mode = 'U'
        #t txtBookid를 사용하지 못하게 설정
        self.txtBookid.setEnabled(False)

    # pyqt에 있는 함수 오버라이드 하기!!
    def closeEvent(self, event) -> None:
        re = QMessageBox.question(self,'종료 여부', '종료하시겠습니까',QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = qtApp()
    sys.exit(app.exec_())

        