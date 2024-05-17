import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QLinearGradient, QBrush, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QInputDialog, QGridLayout

class InventoryManagementSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ICT Inventory Management System')
        self.setGeometry(100, 100, 600, 400)

        # Widgets
        self.item_name_label = QLabel('Item Name:')
        self.item_name_edit = QLineEdit()
        self.quantity_label = QLabel('Quantity:')
        self.quantity_edit = QLineEdit()
        self.add_button = QPushButton('Add')
        self.view_button = QPushButton('View')
        self.update_button = QPushButton('Update')
        self.delete_button = QPushButton('Delete')
        self.item_list = QListWidget()

        # Layout
        layout = QVBoxLayout()
        form_layout = QGridLayout()
        form_layout.addWidget(self.item_name_label, 0, 0)
        form_layout.addWidget(self.item_name_edit, 0, 1)
        form_layout.addWidget(self.quantity_label, 1, 0)
        form_layout.addWidget(self.quantity_edit, 1, 1)
        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.view_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

        layout.addWidget(self.item_list)
        self.setLayout(layout)

          # Set gradient background color for the item_list widget
        gradient = QLinearGradient(0, 0, 0, self.item_list.height())
        gradient.setColorAt(0, Qt.lightpink1)
        gradient.setColorAt(1, Qt.lightcoral)
        self.item_list.setStyleSheet("background-color: qlineargradient(x1:0 y1:0, x2:0 y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 0, 255, 255));")

        # Connect buttons to functions
        self.add_button.clicked.connect(self.add_item)
        self.view_button.clicked.connect(self.view_items)
        self.update_button.clicked.connect(self.update_item)
        self.delete_button.clicked.connect(self.delete_item)

    def add_item(self):
        item_name = self.item_name_edit.text()
        quantity = self.quantity_edit.text()
        if item_name and quantity:
            item_text = f'{item_name} - {quantity}'
            self.item_list.addItem(item_text)
            self.item_name_edit.clear()
            self.quantity_edit.clear()
        else:
            QMessageBox.Oops(self, 'Oops', 'Please enter item name and quantity.')

    def view_items(self):
        selected_item = self.item_list.currentItem()
        if selected_item:
            QMessageBox.information(self, 'View Item', f'Selected Item: {selected_item.text()}')
        else:
            QMessageBox.warning(self, 'Oops', 'Please select an item.')

    def update_item(self):
        selected_item = self.item_list.currentItem()
        if selected_item:
            new_item_name, ok1 = QInputDialog.getText(self, 'Update Item Name', 'Enter new item name:', QLineEdit.Normal, selected_item.text().split('-')[0])
            new_quantity, ok2 = QInputDialog.getInt(self, 'Update Quantity', 'Enter new quantity:', int(selected_item.text().split('-')[1]))
            if ok1 and ok2:
                selected_item.setText(f'{new_item_name.strip()} - {new_quantity}')
        else:
            QMessageBox.warning(self, 'Oops', 'Please select an item.')

    def delete_item(self):
        selected_item = self.item_list.currentItem()
        if selected_item:
            self.item_list.takeItem(self.item_list.row(selected_item))
        else:
            QMessageBox.warning(self, 'Oops', 'Please select an item to delete.')


app = QApplication(sys.argv)
window = InventoryManagementSystem()
window.show()
sys.exit(app.exec_())