from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QMainWindow,QHBoxLayout, QPushButton ,  QApplication, QWidget
from test_case_gen import *
import sys
from factory import *



class my_window(QMainWindow,Ui_MainWindow):#这里我们继承了test_case_gen.py中的Ui_MainWindow类来使用我们设计的UI

    def forge_link(self):
        self.confirm_btn.clicked.connect(self.onButtonClick)
        self.descriptions=""
        self.i=0


    def __init__(self,parent=None):

        super(my_window, self).__init__(parent)
        self.setupUi(self)
        self.forge_link()  # 连接槽函数

    def onButtonClick(self):

        print(' 开始读取要求')
        global element_type
        gn = int(self.gn_edit.text())
        # 测试样例生成文件路径（待测函数.txt)
        fn = self.functionname_edit.text()
        fn += ".txt"

        type = ''
        if (self.list_choose.isChecked()):
            type = "l"
        if (self.element_choose.isChecked()):
            type = ''

        #判断传参个数
        para_count=int(self.paracount.currentText())
        if self.i==para_count-1:
            self.confirm_btn.setText("OK")
        if self.i==para_count:
            self.confirm_btn.setEnabled(False)
            #参数输入完毕，开始输出
            gw = open("all.txt", "w", encoding="utf-8")
            gw.write("start:\n")
            gen(gn, gw, fn, self.descriptions)


        # 读取元素要求-------------------
        element_type=''
        if (self.int_choose.isChecked()):
            element_type = 'i'
        if (self.str_choose.isChecked()):
            element_type = "str"
        datalow = self.data_request_low.text()
        datahigh = self.data_request_high.text()

        element_request = []
        element_request.append(self.odd_choose.currentText())
        element_request.append(self.positive_choose.currentText())
        element_request.append(self.prime_choose.currentText())

        # 读取列表要求---------------------
        listlow = self.list_num_request_low.text()
        listhigh = self.list_num_request_high.text()
        listrequest=[]
        listrequest.append(self.list_extra_request.currentText())
        listrequest.append(self.dec_inc_choose.currentText())
        #print(listlow)

        # 合成总的description---------------
        description = ""
        description += type
        if type=='l':
            description += '#'
        # 合成元素要求-----------
        if (element_type == 'i'):
            description += 'i'
            if(datalow!=''):
                description+=':'
                description += str(datalow)
            if(datahigh!=''):
                description+=':'
                description += str(datahigh)
        else:
            description += "str"

        # 合成列表要求------------
        if (element_request != ['','','']):
            description += ':'
            for i in element_request:
                if(i!=''):
                    description += i
                    description += '|'
            description = description[0:-1]
        if listlow!='':
            description+='#'
            description += str(listlow)
        if listhigh!='':
            description+='#'
            description += str(listhigh)
        if listrequest!=['','']:
            for i in listrequest:
                description += '#'
                description += str(i)


        self.descriptions+=str(description)
        self.i+=1
        if(self.i+1<=para_count):
            self.Request_of_who.setText("第" + str(self.i+1) + "个参数要求")
        if self.i!=para_count:
            self.descriptions += ','
        #print(self.descriptions)


def main():

    app = QApplication(sys.argv)  # 初始化界面
    window = my_window()  # 窗体类型 主窗体
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./background.jpeg")))
    window.setPalette(palette)
    window.show()  # 显示窗体
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()


