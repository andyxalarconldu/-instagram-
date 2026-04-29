# 📸 Instagram Scraper con Flask

Este proyecto es una aplicación web que permite obtener información pública de perfiles de Instagram usando web scraping.

## 🚀 ¿Qué hace?

Permite ingresar:
- Un username (ej: instagram)
- O un enlace de perfil

Y muestra:
- Nombre
- Biografía
- Seguidores
- Seguidos
- Foto de perfil
- Últimas publicaciones

---

## 🛠️ Tecnologías usadas

- Python
- Flask
- Requests
- HTML + Bootstrap

---

## 📂 Estructura del proyecto
instagram/
│
├── app.py
├── scraper.py
├── requirements.txt
├── .gitignore
└── templates/
└── index.html

---

## ⚙️ ¿Cómo funciona?

1. El usuario ingresa un username o link
2. Flask recibe el dato
3. Se llama a la función `get_instagram_data()`
4. Se hace una petición a Instagram
5. Se obtiene un JSON con datos
6. Se muestran en pantalla

---

## ▶️ Cómo ejecutar el proyecto

### 1. Instalar dependencias

### 2. Ejecutar la aplicación

### 3. Abrir en el navegador

---

## ⚠️ Importante

- Solo funciona con perfiles públicos
- Instagram puede bloquear si se hacen muchas peticiones
- Se usan cookies del navegador

---

## 👨‍💻 Autor

Andy Alarcón