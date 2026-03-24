from app import db
from datetime import datetime

class Tarea(db.Model):
    __tablename__ = "tareas"

    id          = db.Column(db.Integer, primary_key=True)
    titulo      = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    estado      = db.Column(db.String(50), default="pendiente")
    fecha_creacion    = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id":          self.id,
            "titulo":      self.titulo,
            "descripcion": self.descripcion,
            "estado":      self.estado,
            "fecha_creacion":     self.fecha_creacion.isoformat(),
            "fecha_actualizacion": self.fecha_actualizacion.isoformat()
        }