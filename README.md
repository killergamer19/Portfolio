# 🎨 Modern Portfolio Website

A beautiful, fully functional portfolio website built with Flask, Tailwind CSS, and SQLite3.

## 🚀 Features

✅ **Responsive Design** - Mobile-friendly layout using Tailwind CSS  
✅ **Dynamic Projects** - Project data stored in SQLite database  
✅ **Contact Form** - Submit messages directly from the website  
✅ **Modern Aesthetics** - Dark mode design with cyan accents  
✅ **Smooth Animations** - Hover effects and transitions  
✅ **REST API** - Backend API endpoints for projects and contact submissions  

## 📋 Project Structure

```
portfolio/
├── app.py                  # Flask application with routes
├── database.py            # SQLite database setup and initialization
├── requirements.txt       # Python dependencies
├── portfolio.db          # SQLite database (created on first run)
├── templates/
│   └── index.html        # Main HTML template with Tailwind CSS
└── static/               # For future static assets
```

## 📦 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone or Download
Navigate to the project directory in your terminal.

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Initialize the Database
```bash
python database.py
```

This will create `portfolio.db` with sample projects and messages tables.

### Step 4: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

**Note:** Use `Ctrl+C` to stop the Flask development server.

## 🌐 Access the Website

Open your browser and navigate to:
```
http://localhost:5000
```

## 📱 Sections

### Hero Section
- Eye-catching headline
- Professional summary
- Call-to-action buttons

### About Section
- Professional photo
- Experience overview
- Key skills displayed as badges

### Projects Section
- Dynamically loaded from SQLite database
- Project cards with images, descriptions, and technology tags
- Hover effects and interactive design

### Contact Section
- Form validation
- Real-time error/success messages
- Data stored in SQLite database

### Footer
- Copyright notice
- Social media links

## 🛠️ Customization

### Edit Your Information
1. Update the hero section in `templates/index.html` (lines ~72-88)
2. Change the "About Me" section (lines ~104-135)
3. Modify profile photo URL in the about section

### Add or Edit Projects
You can manage projects in two ways:

**Method 1: Direct Database Edit**
- Modify the sample projects in `database.py` before running it
- Add new tuples to the `sample_projects` list with format:
  ```python
  ('Project Title', 'Description', 'image_url', 'Tech1, Tech2, Tech3', '#')
  ```

**Method 2: Add via API**
- Use the contact form endpoint to add projects programmatically
- Or edit the `portfolio.db` file using a SQLite browser

### Customize Colors
The accent color is cyan (`#06b6d4`). To change it:
1. Search for `#06b6d4` in `templates/index.html`
2. Replace with your preferred hex color
3. Also update the CSS class references for accent colors

### Change Social Media Links
Update the footer section (lines ~300-315) with your actual social media URLs.

## 📡 API Endpoints

### GET `/`
Returns the main portfolio page.

### POST `/api/contact`
Submit a contact message.

**Request:**
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Your message here"
}
```

**Response:**
```json
{
    "success": true,
    "message": "Thank you! Your message has been sent successfully."
}
```

### GET `/api/projects`
Fetch all projects as JSON.

**Response:**
```json
{
    "success": true,
    "projects": [
        {
            "id": 1,
            "title": "Project Title",
            "description": "Project description",
            "image_url": "https://...",
            "tech_stack": "Python, Flask, SQLite",
            "link": "#"
        }
    ]
}
```

## 🗄️ Database Schema

### Projects Table
```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    image_url TEXT,
    tech_stack TEXT NOT NULL,
    link TEXT
)
```

### Messages Table
```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

## ⚙️ Configuration

### Development Mode
The app runs in debug mode by default, which enables:
- Automatic reloading on code changes
- Detailed error messages
- Interactive debugger

### Production Deployment
For production, modify `app.py` line at the bottom:
```python
# Change from:
app.run(debug=True, host='0.0.0.0', port=5000)

# To:
app.run(debug=False, host='0.0.0.0', port=5000)
```

## 🎯 Tech Stack

- **Frontend:** HTML5, Tailwind CSS, JavaScript
- **Backend:** Flask (Python)
- **Database:** SQLite3
- **Styling:** Utility-first CSS with Tailwind

## 📝 Notes

- Contact form messages are validated on both client and server side
- All form inputs have character limits for security
- The database is created automatically on first run if it doesn't exist
- Images use placeholder URLs from placeholder.com (replace with your own)

## 🔒 Security Notes

This is a development version. For production use:
1. Add CSRF protection with Flask-WTF
2. Implement rate limiting on contact endpoint
3. Add email verification for contact submissions
4. Use environment variables for sensitive data
5. Enable HTTPS
6. Add database connection pooling

## 📄 License

Free to use and modify for personal projects.

## 🤝 Support

For issues or questions, ensure:
1. Python 3.7+ is installed
2. All dependencies are installed via `pip install -r requirements.txt`
3. The database is initialized with `python database.py`
4. No other service is using port 5000

---

**Happy coding! 🎉**
