# St. Joseph Careers Website

## Overview
This is a careers website for St. Joseph, built with Flask. The project was imported from a minimal GitHub repository and transformed into a fully functional careers website with multiple pages and professional styling.

## Recent Changes
- **2025-09-10**: Initial project setup and complete Flask application development
  - Created Flask web application with career-focused content
  - Implemented responsive design with Bootstrap
  - Set up production-ready configuration with gunicorn
  - Configured deployment settings for Replit environment

## User Preferences
- Professional, clean design suitable for a careers website
- Bootstrap-based responsive layout
- Production-ready configuration for deployment

## Project Architecture

### Structure
- `app.py` - Main Flask application with routes for home, careers, and about pages
- `templates/` - HTML templates using Jinja2
  - `base.html` - Base template with navigation and footer
  - `index.html` - Homepage with hero section and feature cards
  - `careers.html` - Careers page with job listings
  - `about.html` - About page with company information
- `static/css/style.css` - Custom CSS for styling and animations
- `requirements.txt` - Python dependencies (Flask, gunicorn)
- `gunicorn_config.py` - Production server configuration

### Key Technical Decisions
- **Flask Framework**: Chosen for simplicity and rapid development
- **Bootstrap 5**: Used for responsive design and professional appearance
- **Gunicorn**: Production WSGI server for better performance and security
- **Environment-based Configuration**: Supports both development and production environments
- **Health Monitoring**: `/health` endpoint for deployment monitoring

### Deployment Configuration
- **Development**: Uses Flask dev server with debug mode (optional)
- **Production**: Uses gunicorn with 4 workers on port 5000
- **Host Configuration**: Binds to 0.0.0.0 for Replit proxy compatibility
- **Deployment Target**: Autoscale (suitable for websites)

## Current State
The application is fully functional and production-ready:
- ✅ Flask server running on gunicorn
- ✅ All pages (home, careers, about) working correctly  
- ✅ Responsive design with Bootstrap
- ✅ Production security configuration
- ✅ Health monitoring endpoint
- ✅ Deployment configuration completed