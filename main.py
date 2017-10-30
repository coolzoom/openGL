# Basic obj file viewer
#Loading and displaying *.obj 3d object
#

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4 import QtGui,QtCore
from PyQt4.QtOpenGL import *


from obj_loader import *
from gnomon import *


class oglWidget(QGLWidget):

    def __init__(self, parent = None):
        #draw gnomon in viewport before any model loaded
        self.model = Gnomon()
        super(oglWidget, self).__init__(parent)
        self.setMinimumSize(400, 400)

        #model transforms
        self.rotateModel = [0,0,0]
        self.shadingMode=1


    def paintGL(self):
        if self.shadingMode==1:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

        self.initializeGL()
        #print "paintGL"
        glColor3f(1.0, 1.0, 0.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0,0.0, -3)
        glRotatef(self.rotateModel[0],0, 1, 0)
        glRotatef(self.rotateModel[1], 1, 0, 0)
        glRotatef(self.rotateModel[2], 0, 0,1)
        self.model.draw()

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glViewport(0, 0, w, h)
        gluPerspective(45, w/h, 0.1, 100.0)
        self.model.draw()

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)


class Window(QtGui.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Open GL model viewer")
        self.oglwidget = oglWidget(self)
        self.helpLine = "slider or WASDQE keys - orient model\n1-wireframe, 2-solid shading"


        # Create layout
        #top level vertical
        self.layout_vbox_L0 = QtGui.QVBoxLayout(self)
        self.layout_vbox_L0.setContentsMargins(5, 0, 5, 5)
        #horisontal layout for OGL controls group and OGL window
        self.layout_hbox_L1 = QtGui.QHBoxLayout()

        #OGL controls group
        self.ogl_controls_group = QtGui.QGroupBox("OGL controls box")

        #vertical layout inside OGL controls group
        self.layout_vbox_L2 = QtGui.QVBoxLayout()
        self.ogl_controls_group.setLayout(self.layout_vbox_L2)

        #OGL controls
        ogl_contols_rotateLabel=QtGui.QLabel("Rotate x y z:")
        self.layout_vbox_L2.addWidget(ogl_contols_rotateLabel)
        self.ogl_contols_rotateX=QtGui.QSlider()
        self.ogl_contols_rotateX.setOrientation(QtCore.Qt.Horizontal)
        self.layout_vbox_L2.addWidget(self.ogl_contols_rotateX)
        self.ogl_contols_rotateX.valueChanged.connect(self.orientationChanged)
        self.ogl_contols_rotateY=QtGui.QSlider()
        self.ogl_contols_rotateY.setOrientation(QtCore.Qt.Horizontal)
        self.layout_vbox_L2.addWidget(self.ogl_contols_rotateY)
        self.ogl_contols_rotateY.valueChanged.connect(self.orientationChanged)
        self.ogl_contols_rotateZ=QtGui.QSlider()
        self.ogl_contols_rotateZ.setOrientation(QtCore.Qt.Horizontal)
        self.layout_vbox_L2.addWidget(self.ogl_contols_rotateZ)
        self.ogl_contols_rotateZ.valueChanged.connect(self.orientationChanged)
        self.ogl_controls_texturedCheckBox=QtGui.QCheckBox("Textured")
        self.layout_vbox_L2.addWidget(self.ogl_controls_texturedCheckBox)

        self.layout_hbox_L1.addWidget(self.ogl_controls_group)
        self.layout_hbox_L1.addWidget(self.oglwidget)

        # menu bar
        self.menuBar = QtGui.QMenuBar(self)


        self.fileOpenAction = QtGui.QAction('&Open', self)
        self.fileOpenAction.triggered.connect(self.openPyFile)
        self.exitAction = QtGui.QAction('&Exit', self)
        self.exitAction.triggered.connect(self.close_application)
        self.fileMenu = self.menuBar.addMenu('&File')
        self.fileMenu.addAction(self.fileOpenAction)
        self.fileMenu.addAction(self.exitAction)

        # status bar
        self.statusBarLabel=QtGui.QLabel()
        self.statusBarLabel.setText(self.helpLine)
        self.statusBar=QtGui.QStatusBar(self)
        self.statusBar.addWidget(self.statusBarLabel)
        self.statusBar.setMaximumHeight(100)
        self.statusBar.setMaximumWidth(600)

        #self.setCentralWidget(oglwidget)
        self.layout_vbox_L0.addWidget(self.menuBar)
        self.layout_vbox_L0.addLayout(self.layout_hbox_L1)
        self.layout_vbox_L0.addWidget(self.statusBar)

    def orientationChanged(self):
        self.oglwidget.rotateModel[0] = self.ogl_contols_rotateX.value()
        self.oglwidget.rotateModel[1] = self.ogl_contols_rotateY.value()
        self.oglwidget.rotateModel[2] = self.ogl_contols_rotateZ.value()
        self.oglwidget.glDraw()
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            print("Pressed ESC key")
        if e.key() == QtCore.Qt.Key_A:
            self.ogl_contols_rotateX.setValue(self.ogl_contols_rotateX.value()+15)
            self.oglwidget.rotateModel[0]=self.ogl_contols_rotateX.value()
            self.oglwidget.glDraw()
        if e.key() == QtCore.Qt.Key_D:
            self.ogl_contols_rotateX.setValue(self.ogl_contols_rotateX.value() - 15)
            self.oglwidget.rotateModel[0] = self.ogl_contols_rotateX.value()
            self.oglwidget.glDraw()
        if e.key() == QtCore.Qt.Key_W:
            self.ogl_contols_rotateY.setValue(self.ogl_contols_rotateY.value() + 15)
            self.oglwidget.rotateModel[1] = self.ogl_contols_rotateY.value()
            self.oglwidget.glDraw()
        if e.key() == QtCore.Qt.Key_S:
            self.ogl_contols_rotateY.setValue(self.ogl_contols_rotateY.value() - 15)
            self.oglwidget.rotateModel[1] = self.ogl_contols_rotateY.value()
            self.oglwidget.glDraw()
        if e.key() == QtCore.Qt.Key_Q:
            self.ogl_contols_rotateZ.setValue(self.ogl_contols_rotateZ.value() + 15)
            self.oglwidget.rotateModel[2] = self.ogl_contols_rotateZ.value()
            self.oglwidget.glDraw()
        if e.key() == QtCore.Qt.Key_E:
            self.ogl_contols_rotateZ.setValue(self.ogl_contols_rotateZ.value() - 15)
            self.oglwidget.rotateModel[2] = self.ogl_contols_rotateZ.value()
            self.oglwidget.glDraw()

        if e.key() == QtCore.Qt.Key_R:
            self.ogl_contols_rotateX.setValue(0)
            self.ogl_contols_rotateY.setValue(0)
            self.ogl_contols_rotateZ.setValue(0)
            self.oglwidget.rotateModel = [0,0,0]
            self.oglwidget.glDraw()
            #print("View reset")

        if e.key() == QtCore.Qt.Key_1:
            self.oglwidget.shadingMode=1
            self.oglwidget.glDraw()
        if e.key() == QtCore.Qt.Key_2:
            self.oglwidget.shadingMode=2
            self.oglwidget.glDraw()



    def openPyFile(self):
        self.fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.oglwidget.model = obj_loader(self.fileName)
        self.statusBarLabel.setText((self.helpLine+"\nmodel:"+self.fileName))
        self.oglwidget.glDraw()


    def close_application(self):
        exit()

if __name__== "__main__":
    app=QtGui.QApplication([])
    window=Window()
    window.show()

    exit(app.exec_())