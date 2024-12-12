from config import db

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {

                'id': self.id,
                'nombre': self.nombre,
                'descripcion': self.descripcion,
            }




