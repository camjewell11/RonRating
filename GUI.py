import Graph, IO, Rate, sys

from matplotlib.pyplot import hlines
import matplotlib
matplotlib.use('Qt5Agg')

import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg
# import PyQt5.QtCore as qc

def displayBeers():
    if len(IO.beerData) > 0:
        ax = Graph.createRadar()
        Graph.plotRadar(ax, IO.beers, IO.beersToGraph)
    else:
        print ("No beers to display.")

class displayWindow(qw.QWidget):
    def __init__(self, parent = None):
        super(displayWindow, self).__init__(parent)

        self.mainVerticalLayout = qw.QVBoxLayout()
        self.resize(850,500)
        self.setWindowTitle("BeeZr Beers")

        self.label = qw.QLabel(self)
        self.label.setText("Select beers to display:")
        self.label.move(50,20)
        self.mainVerticalLayout.addWidget(self.label)

        self.initializeBoxColumns()
        self.createCheckBoxes()
        self.addColumnSpacers()

        mainButtonsWidget = qw.QWidget()
        mainButtonsLayout = qw.QHBoxLayout(mainButtonsWidget)

        self.plotButton = qw.QPushButton("View Selected Beers")
        mainButtonsLayout.addWidget(self.plotButton)
        self.plotButton.clicked.connect(displayBeers)

        self.ratingWindow = None
        self.rateButton = qw.QPushButton("Leave a Beer Rating")
        mainButtonsLayout.addWidget(self.rateButton)
        self.rateButton.clicked.connect(self.leaveARating)

        self.mainVerticalLayout.addWidget(mainButtonsWidget)
        self.setLayout(self.mainVerticalLayout)

    def initializeBoxColumns(self):
        boxesWidget = qw.QWidget()
        self.beerBoxesLayout = qw.QHBoxLayout()

        ipaWidget = qw.QWidget()
        self.ipaLayout = qw.QVBoxLayout(ipaWidget)
        self.ipaCheckBox = qw.QCheckBox("IPAs")
        self.ipaCheckBox.setChecked(True)
        self.ipaCheckBox.setFont(qg.QFont('Arial', 12))
        self.ipaCheckBox.stateChanged.connect(lambda:self.toggleBeerType("ipa"))

        lagerWidget = qw.QWidget()
        self.lagerLayout = qw.QVBoxLayout(lagerWidget)
        self.lagerCheckBox = qw.QCheckBox("Lagers")
        self.lagerCheckBox.setChecked(True)
        self.lagerCheckBox.setFont(qg.QFont('Arial', 12))
        self.lagerCheckBox.stateChanged.connect(lambda:self.toggleBeerType("lager"))

        aleWidget = qw.QWidget()
        self.aleLayout = qw.QVBoxLayout(aleWidget)
        self.aleCheckBox = qw.QCheckBox("Ales")
        self.aleCheckBox.setChecked(True)
        self.aleCheckBox.setFont(qg.QFont('Arial', 12))
        self.aleCheckBox.stateChanged.connect(lambda:self.toggleBeerType("ale"))

        stoutWidget = qw.QWidget()
        self.stoutLayout = qw.QVBoxLayout(stoutWidget)
        self.stoutCheckBox = qw.QCheckBox("Stouts")
        self.stoutCheckBox.setChecked(True)
        self.stoutCheckBox.setFont(qg.QFont('Arial', 12))
        self.stoutCheckBox.stateChanged.connect(lambda:self.toggleBeerType("stout"))

        sourWidget = qw.QWidget()
        self.sourLayout = qw.QVBoxLayout(sourWidget)
        self.sourCheckBox = qw.QCheckBox("Sours")
        self.sourCheckBox.setChecked(True)
        self.sourCheckBox.setFont(qg.QFont('Arial', 12))
        self.sourCheckBox.stateChanged.connect(lambda:self.toggleBeerType("sour"))

        otherWidget = qw.QWidget()
        self.otherLayout = qw.QVBoxLayout(otherWidget)
        self.otherCheckBox = qw.QCheckBox("Others")
        self.otherCheckBox.setChecked(True)
        self.otherCheckBox.setFont(qg.QFont('Arial', 12))
        self.otherCheckBox.stateChanged.connect(lambda:self.toggleBeerType("other"))

        # horizontal line spacers
        hLine1 = qw.QFrame()
        hLine1.setFrameShape(qw.QFrame.HLine)
        hLine2 = qw.QFrame()
        hLine2.setFrameShape(qw.QFrame.HLine)
        hLine3 = qw.QFrame()
        hLine3.setFrameShape(qw.QFrame.HLine)
        hLine4 = qw.QFrame()
        hLine4.setFrameShape(qw.QFrame.HLine)
        hLine5 = qw.QFrame()
        hLine5.setFrameShape(qw.QFrame.HLine)
        hLine6 = qw.QFrame()
        hLine6.setFrameShape(qw.QFrame.HLine)

        self.ipaLayout.addWidget(self.ipaCheckBox)
        self.ipaLayout.addWidget(hLine1)
        self.lagerLayout.addWidget(self.lagerCheckBox)
        self.lagerLayout.addWidget(hLine2)
        self.aleLayout.addWidget(self.aleCheckBox)
        self.aleLayout.addWidget(hLine3)
        self.stoutLayout.addWidget(self.stoutCheckBox)
        self.stoutLayout.addWidget(hLine4)
        self.sourLayout.addWidget(self.sourCheckBox)
        self.sourLayout.addWidget(hLine5)
        self.otherLayout.addWidget(self.otherCheckBox)
        self.otherLayout.addWidget(hLine6)

        # vertical spacer lines
        vLine1 = qw.QFrame()
        vLine1.setFrameShape(qw.QFrame.VLine)
        vLine2 = qw.QFrame()
        vLine2.setFrameShape(qw.QFrame.VLine)
        vLine3 = qw.QFrame()
        vLine3.setFrameShape(qw.QFrame.VLine)
        vLine4 = qw.QFrame()
        vLine4.setFrameShape(qw.QFrame.VLine)
        vLine5 = qw.QFrame()
        vLine5.setFrameShape(qw.QFrame.VLine)

        self.beerBoxesLayout.addWidget(ipaWidget)
        self.beerBoxesLayout.addWidget(vLine1)
        self.beerBoxesLayout.addWidget(lagerWidget)
        self.beerBoxesLayout.addWidget(vLine2)
        self.beerBoxesLayout.addWidget(aleWidget)
        self.beerBoxesLayout.addWidget(vLine3)
        self.beerBoxesLayout.addWidget(stoutWidget)
        self.beerBoxesLayout.addWidget(vLine4)
        self.beerBoxesLayout.addWidget(sourWidget)
        self.beerBoxesLayout.addWidget(vLine5)
        self.beerBoxesLayout.addWidget(otherWidget)

        boxesWidget.setLayout(self.beerBoxesLayout)
        self.mainVerticalLayout.addWidget(boxesWidget)

    def createCheckBoxes(self):
        self.beerCheckBoxes = []

        for beer in IO.beers:
            temp = qw.QCheckBox(beer)
            temp.setChecked(True)
            temp.stateChanged.connect(self.updateGraphsList)
            temp.setStyleSheet("color: " + IO.beerData[beer]["plot_color"])
            self.beerCheckBoxes.append(temp)

            if IO.getBeerType(IO.beerData, beer) == "ipa":
                self.ipaLayout.addWidget(temp)
            elif IO.getBeerType(IO.beerData, beer) == "lager":
                self.lagerLayout.addWidget(temp)
            elif IO.getBeerType(IO.beerData, beer) == "ale":
                self.aleLayout.addWidget(temp)
            elif IO.getBeerType(IO.beerData, beer) == "stout":
                self.stoutLayout.addWidget(temp)
            elif IO.getBeerType(IO.beerData, beer) == "sour":
                self.sourLayout.addWidget(temp)
            elif IO.getBeerType(IO.beerData, beer) == "other":
                self.otherLayout.addWidget(temp)

    def addColumnSpacers(self):
        self.ipaLayout.addStretch()
        self.lagerLayout.addStretch()
        self.aleLayout.addStretch()
        self.stoutLayout.addStretch()
        self.sourLayout.addStretch()
        self.otherLayout.addStretch()

    def toggleBeerType(self, beerType):
        if beerType == "ipa":
            boxInQuestion = self.ipaCheckBox
        elif beerType == "lager":
            boxInQuestion = self.lagerCheckBox
        elif beerType == "ale":
            boxInQuestion = self.aleCheckBox
        elif beerType == "stout":
            boxInQuestion = self.stoutCheckBox
        elif beerType == "sour":
            boxInQuestion = self.sourCheckBox
        elif beerType == "other":
            boxInQuestion = self.otherCheckBox
        toggledOn = boxInQuestion.isChecked()

        for box in self.beerCheckBoxes:
            beerName = box.text()
            if not toggledOn and box.isChecked():
                if beerName in IO.beersToGraph.keys() and IO.beerData[beerName]["type"] == beerType:
                    IO.beersToGraph.pop(beerName)
                    box.setChecked(False)
            elif toggledOn and not box.isChecked() and IO.beerData[beerName]["type"] == beerType:
                if beerName not in IO.beersToGraph.keys():
                    IO.beersToGraph[beerName] = IO.beerData[beerName]["plot_color"]
                    box.setChecked(True)

    def updateGraphsList(self):
        for box in self.beerCheckBoxes:
            beerName = box.text()
            if not box.isChecked(): # just unchecked
                if beerName in IO.beersToGraph.keys():
                    IO.beersToGraph.pop(beerName)
            if box.isChecked(): # just checked
                if beerName not in IO.beersToGraph.keys():
                    IO.beersToGraph[beerName] = IO.beerData[beerName]["plot_color"]

    def leaveARating(self):
        self.ratingWindow = Rate.rateWindow()
        self.ratingWindow.show()

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = displayWindow()
    w.show()
    sys.exit(app.exec_())