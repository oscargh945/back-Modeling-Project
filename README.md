# Back Modeling Project

Este proyecto es una aplicación backend que integra FastAPI con Octave para realizar modelamiento matemático.

## 🚀 Características

- API REST construida con FastAPI
- Integración con GNU Octave para cálculos matemáticos
- Configuración con Docker y Docker Compose
- Exposición de la API mediante ngrok para pruebas remotas

## 📋 Prerrequisitos

- Docker y Docker Compose
- Python 3.8+
- GNU Octave
- Cuenta de ngrok (gratuita o de pago)

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd back-Modeling-project
```

2. Configurar ngrok:
   - Crear una cuenta en [ngrok.com](https://ngrok.com)
   - Obtener tu token de autenticación desde el dashboard de ngrok
   - Crear un archivo `.env` en la raíz del proyecto con:
   ```
   NGROK_AUTHTOKEN=tu_token_de_ngrok
   ```

3. Construir y ejecutar los contenedores:
```bash
docker-compose up --build
```

## 🏃‍♂️ Uso

La aplicación estará disponible en:
- Local: http://localhost:8000
- Ngrok: La URL pública se mostrará en la consola cuando inicies los contenedores

### Configuración de ngrok
El proyecto está configurado para usar ngrok automáticamente a través de Docker Compose. El servicio de ngrok:
- Expone el puerto 8000 de la aplicación FastAPI
- Genera una URL pública temporal
- Permite acceder a tu API desde cualquier lugar de internet

Para ver la URL de ngrok:
```bash
docker-compose logs ngrok
```

## 📦 Estructura del Proyecto

```
.
├── app/               # Código fuente de la aplicación
├── nginx/            # Configuración de nginx
├── octave/           # Scripts y funciones de Octave
├── Dockerfile        # Configuración de Docker
├── docker-compose.yml # Configuración de Docker Compose
└── requirements.txt  # Dependencias de Python
```

## 🛠 Tecnologías Utilizadas

- FastAPI
- GNU Octave
- Docker
- Nginx
- ngrok

## 📝 Dependencias Principales

- fastapi[all]
- uvicorn
- numpy
- ngrok

## 🤝 Contribución

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.
