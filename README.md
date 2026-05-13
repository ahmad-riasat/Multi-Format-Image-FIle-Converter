Multi-Format Image & File Converter
A Django-based web application that allows users to upload images and convert them between multiple formats. Built as an SDA (Software Design and Architecture) project with clean design patterns applied throughout the codebase.

✨ Features

Upload images via a simple web interface
Convert between multiple image formats (e.g., PNG, JPEG, BMP, WEBP, etc.)
Clean, modular architecture using software design patterns
Static file serving with WhiteNoise (production-ready)
Deployable to Heroku or any WSGI-compatible platform


🛠️ Tech Stack
LayerTechnologyBackendDjango 5.0.0Image ProcessingPillow 10.2.0Web ServerGunicorn 21.2.0Static FilesWhiteNoise 6.6.0Database URL Parsingdj-database-url 2.1.0FrontendHTML, CSS

📁 Project Structure
Multi-Format-Image-File-Converter/
├── converters/        # Converter classes (design pattern implementations)
├── core/              # Django app — views, models, URLs
├── main/              # Project settings and WSGI entry point
├── media/             # Uploaded and converted media files
├── static/css/        # Stylesheets
├── templates/         # HTML templates
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
├── Procfile           # Heroku deployment config
└── db.sqlite3         # SQLite database
