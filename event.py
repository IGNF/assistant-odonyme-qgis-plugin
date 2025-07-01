from qgis.PyQt.QtCore import QObject,QEvent
from qgis.PyQt.QtWidgets import QLineEdit
# from .RenommeRue import *

# class personnalisé pour gerer les evenements dans la zone de texte des combobox
class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.isclicked = False

    def set_clic_in_zone_text(self,isclic):
        self.isclicked = isclic

    def clic_in_zone_text(self):
        if self.isclicked:
            return True
        else:
            return False

    def mousePressEvent(self, event):
        self.isclicked = True
        # Vous pouvez ajouter ici la logique que vous souhaitez pour le clic
        super().mousePressEvent(event)


# class Eventwidget(QObject):
#     def __init__(self, dlg):
#         super().__init__()
#         self.dlg = dlg
#         self.isclicked = False
#
#     def comboisclicked(self):
#         if self.isclicked:
#             print("comboisclicked = true")
#             return True
#         else:
#             print("comboisclicked = false")
#             return False
#
#     def eventFilter(self,  obj,  event):
#         if event.type() == QEvent.MouseButtonPress:
#             print("clic qqpart : ", obj.objectName())
#             if obj == self.dlg.line_edit:
#                 print("Clic DANS le combo ")
#                 self.isclicked = True
#                 self.comboisclicked()
#                 return True
#             else:
#                 print("Clic en dehors du combo ")
#                 self.isclicked = False
#                 self.comboisclicked()
#                 return False
#
#         return False




# class LineEditWithClick(QLineEdit):
#     def __init__(self,dlg):
#         super().__init__()
#         self.dlg = dlg
#         self._ismodifiefromclavier  = False
#
#     def islineditclicked(self):
#         if self.isclicked:
#             return True
#         else:
#             return False
#
#
#     def mousePressEvent(self, event: QMouseEvent):
#         # Capture l'événement de clic et affiche la position du clic
#         if event.button() == Qt.LeftButton:
#             self._ismodifiefromclavier = True
#             print(f"Clic détecté dans la zone de texte ")
#         super().mousePressEvent(event)
#
#
#     def textChanged(self,event):
#         # Ce signal est émis chaque fois que le texte change
#         if self._is_filled_by_keyboard:
#             print("Texte modifié par le clavier")
#         else:
#             print("Texte modifié par une autre méthode")
#         # Réinitialiser le flag
#         self._ismodifiefromclavier = False



