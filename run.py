from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Tablas creadas correctamente")
    print("🚀 Servidor iniciado en http://localhost:5000")
    print("📄 Documentacion Swagger: http://localhost:5000/docs/")

if __name__ == "__main__":
    app.run(debug=True)