from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit,QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests
from currency_loader import load_currencies_list


def get_currency(in_curr,out_curr):
    url = f"https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find("span",class_ = "ccOutputRslt").getText()
    rate = float(rate[0:-4])
    return (rate,in_curr,out_curr)

def show_currency():
    input_text = text.text()
    if input_text=="":
        output_label.setText("")
    in_select = in_combo.currentText()
    out_select = out_combo.currentText()
    rate = get_currency(in_select,out_select)
    try:
        input_text = float(input_text)
        message = f"{input_text} {rate[1]} is {str(round(float(input_text) * rate[0],3))} {rate[2]}\n "
        output_label.setText(message)
    except:
        output_label.setText("Please input a valid number")

def switch():
    curr_in_select = in_combo.currentText()
    curr_out_select = out_combo.currentText()
    in_combo.setCurrentText(curr_out_select)
    out_combo.setCurrentText(curr_in_select)



app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()

switch_btn = QPushButton('Switch\n<-->')
switch_btn.clicked.connect(switch)
layout1 = QHBoxLayout()
layout.addLayout(layout1)
layout1.addWidget(switch_btn)

output_label = QLabel('')
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)


layout3 = QVBoxLayout()
layout1.addLayout(layout3)
dftable = load_currencies_list()
currencies = dftable['Currency']
in_combo = QComboBox()
in_combo.addItems(currencies)

out_combo = QComboBox()
out_combo.addItems(currencies)

layout2.addWidget(in_combo)
layout2.addWidget(out_combo)

text = QLineEdit()
layout3.addWidget(text)

btn = QPushButton('Convert')
layout3.addWidget(btn,alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_currency)

window.setLayout(layout)
window.show()
app.exec()
