#!/usr/bin/env python

from hgt import HGTFile
from silx.gui import qt
from silx.gui.data.ArrayTableWidget import ArrayTableWidget
import numpy as np
import sys
import time

if __name__ == "__main__":

    app = qt.QApplication(sys.argv)

    newdata = np.arange(12967201,dtype='>i2')
    array = np.arange(12967201,dtype='>i2')

    h = HGTFile(unicode(app.arguments()[1]))

    data = h.read()

    print("data length = " + str(len(data)))

    if len(data) != 12967201:
        print("File length error")
        sys.exit()

    for x in range(0,12967201):
        row = x / 3601
        col = x % 3601 
        array[x] = data[x]

    array.shape = (3601, 3601)

    w = ArrayTableWidget()
    w.setArrayData(array, labels=True, editable=True)
    w.show()
    app.exec_()

    newdata = w.getData(copy=False)
    w.setArrayData(newdata,editable=True)

    for x in range(0,12967201):
        row = x / 3601
        col = x % 3601 
        array[row][col] = int(newdata[row][col])

    print("Saving...")
    f = open("test.hgt", "wb")
    f.write(array)
    f.close()

