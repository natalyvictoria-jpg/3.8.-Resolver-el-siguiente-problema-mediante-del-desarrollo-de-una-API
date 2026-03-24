from flask import Blueprint, jsonify, request
from app import db
from app.models import Tarea
from datetime import datetime

tareas_bp = Blueprint("tareas", __name__, url_prefix="/api")


@tareas_bp.route("/tareas", methods=["POST"])
def crear_tarea():
    """
    Crear una nueva tarea
    ---
    tags:
      - Tareas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            titulo:
              type: string
              example: "Estudiar Flask"
            descripcion:
              type: string
              example: "Repasar endpoints REST"
            estado:
              type: string
              example: "pendiente"
    responses:
      201:
        description: Tarea creada exitosamente
      400:
        description: Datos incorrectos o faltantes
    """
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400

    if "titulo" not in datos:
        return jsonify({"error": "El campo 'titulo' es requerido"}), 400

    estado = datos.get("estado", "pendiente")
    if estado not in ["pendiente", "en progreso", "completada"]:
        return jsonify({"error": "Estado invalido. Use: pendiente, en progreso, completada"}), 400

    nueva = Tarea(
        titulo=datos["titulo"],
        descripcion=datos.get("descripcion", ""),
        estado=estado
    )
    db.session.add(nueva)
    db.session.commit()

    return jsonify({
        "mensaje": "Tarea creada exitosamente",
        "tarea": nueva.to_dict()
    }), 201


@tareas_bp.route("/tareas", methods=["GET"])
def obtener_tareas():
    """
    Obtener todas las tareas
    ---
    tags:
      - Tareas
    parameters:
      - in: query
        name: estado
        type: string
        description: Filtrar por estado (pendiente, en progreso, completada)
      - in: query
        name: titulo
        type: string
        description: Buscar por titulo
    responses:
      200:
        description: Lista de tareas
    """
    estado = request.args.get("estado")
    titulo = request.args.get("titulo")

    query = Tarea.query

    if estado:
        query = query.filter(Tarea.estado == estado)
    if titulo:
        query = query.filter(Tarea.titulo.ilike(f"%{titulo}%"))

    tareas = query.order_by(Tarea.fecha_creacion.desc()).all()

    return jsonify({
        "total": len(tareas),
        "tareas": [t.to_dict() for t in tareas]
    }), 200


@tareas_bp.route("/tareas/<int:id>", methods=["GET"])
def obtener_tarea(id):
    """
    Obtener una tarea por ID
    ---
    tags:
      - Tareas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Datos de la tarea
      404:
        description: Tarea no encontrada
    """
    tarea = Tarea.query.get_or_404(id)
    return jsonify(tarea.to_dict()), 200


@tareas_bp.route("/tareas/<int:id>", methods=["PUT"])
def actualizar_tarea(id):
    """
    Actualizar una tarea existente
    ---
    tags:
      - Tareas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          properties:
            titulo:
              type: string
              example: "Estudiar Flask avanzado"
            descripcion:
              type: string
              example: "Repasar blueprints y JWT"
            estado:
              type: string
              example: "en progreso"
    responses:
      200:
        description: Tarea actualizada exitosamente
      400:
        description: Estado invalido
      404:
        description: Tarea no encontrada
    """
    tarea = Tarea.query.get_or_404(id)
    datos = request.get_json()

    if "titulo" in datos:
        tarea.titulo = datos["titulo"]
    if "descripcion" in datos:
        tarea.descripcion = datos["descripcion"]
    if "estado" in datos:
        if datos["estado"] not in ["pendiente", "en progreso", "completada"]:
            return jsonify({"error": "Estado invalido. Use: pendiente, en progreso, completada"}), 400
        tarea.estado = datos["estado"]

    tarea.fecha_actualizacion = datetime.utcnow()
    db.session.commit()

    return jsonify({
        "mensaje": "Tarea actualizada exitosamente",
        "tarea": tarea.to_dict()
    }), 200


@tareas_bp.route("/tareas/<int:id>", methods=["DELETE"])
def eliminar_tarea(id):
    """
    Eliminar una tarea
    ---
    tags:
      - Tareas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Tarea eliminada exitosamente
      404:
        description: Tarea no encontrada
    """
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()

    return jsonify({
        "mensaje": f"Tarea '{tarea.titulo}' eliminada exitosamente"
    }), 200