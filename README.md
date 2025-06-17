# Windebify 🚀

**Windebify** is a web-based tool that simplifies the process of converting `.exe` (Windows executable) files into `.deb` (Debian package) files using Wine. It’s designed with simplicity and style in mind — letting Linux users run or package `.exe` files in a user-friendly, one-click interface.

![Screenshot](https://github.com/user-attachments/assets/485179ba-1a17-4b52-9ed4-6656f23a46b8)
 <!-- Replace with actual screenshot URL -->

---

## ✨ Features

- 🔁 Convert `.exe` files to `.deb` packages easily
- 🎨 Beautiful, modern UI with light & dark mode support
- 👤 User authentication: Sign up, login, logout
- 🧠 Dashboard to track your uploaded builds
- 📁 Secure file uploads and conversion
- 🎉 Confetti celebration on successful build (optional)
- 🧑‍💻 Built with Django & fully open-source

---

## 🛠 Tech Stack

| Layer     | Tech                 |
|-----------|----------------------|
| Backend   | Django (Python)      |
| Frontend  | HTML/CSS, Vanilla JS |
| Styling   | Custom CSS, Google Fonts |
| Database  | SQLite (default)     |
| Packaging | Wine, Shell scripts  |

---

## 🚀 Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/windebify.git
cd windebify
```

### 2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run migrations:
```bash
python manage.py migrate
```

### 5. Start the development server:
```bash
python manage.py runserver
```

### 6. Visit in browser:
```cpp
http://127.0.0.1:8000
```

## 🔒 .env Example (Optional)
### Create a .env file for secrets:

```ini
DEBUG=True
SECRET_KEY=your-secret-key
```

## 📁 Folder Structure
```csharp
windebify/
├── templates/
├── static/
├── core/             # Main Django app
├── media/            # Uploaded .exe files
├── build/            # Output .deb files
├── manage.py
└── requirements.txt
```
## 📜 License
This project is licensed under the MIT License. See LICENSE for more info.

## 🙋‍♂️ Contributing
Contributions, suggestions and bug reports are welcome!
Feel free to open issues or submit PRs to improve this tool.

## 📬 Contact
Made with ❤️ by @priyanshu_raj

Have a question? DM or create an issue on GitHub.
