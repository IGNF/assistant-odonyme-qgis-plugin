from qgis.PyQt.QtWidgets import QLineEdit

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



