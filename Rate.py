import IO

import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import PyQt5.QtGui as qg

class rateWindow(qw.QWidget):
    def __init__(self, parent=None):
        super(rateWindow, self).__init__(parent)

        self.mainVerticalLayout = qw.QVBoxLayout()
        self.resize(850,500)
        self.setWindowTitle("BeeZr Beers")

        self.label = qw.QLabel(self)
        self.label.setText("Select a beer to rate:")
        self.label.move(50,20)
        self.mainVerticalLayout.addWidget(self.label)

        self.horizontalColumnsWidget = qw.QWidget()
        self.horizontalColumnsLayout = qw.QHBoxLayout(self.horizontalColumnsWidget)
        self.mainVerticalLayout.addWidget(self.horizontalColumnsWidget)

        self.ratingWidget = qw.QWidget()
        self.ratingWidgetLayout = qw.QVBoxLayout(self.ratingWidget)
        self.ratingWidget.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)

        self.beersWidget = self.getListOfBeers()
        self.horizontalColumnsLayout.addWidget(self.beersWidget)

        self.rateButton = qw.QPushButton("Submit Rating")
        self.ratingWidgetLayout.addWidget(self.rateButton)
        self.horizontalColumnsLayout.addWidget(self.ratingWidget)

        self.setLayout(self.mainVerticalLayout)

    def getListOfBeers(self):
        beersWidget = qw.QWidget()
        beerListLayout = qw.QVBoxLayout(beersWidget)
        self.beerList = []
        for beer in IO.beers:
            temp = qw.QLabel(beer)
            temp.setStyleSheet("border: 1px solid black;")
            self.beerList.append(temp)
            beerListLayout.addWidget(temp)
            clickable(temp).connect(lambda:rateBeer(beer))
        return beersWidget

def clickable(widget):
    class Filter(qc.QObject):
        clicked = qc.pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == qc.QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

def rateBeer(beer):
    pass

if __name__=="__main__":
    import sys
    app = qw.QApplication(sys.argv)
    ratingWindow = rateWindow()
    ratingWindow.show()
    sys.exit(app.exec_())