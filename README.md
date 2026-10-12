# Shoppers Store

Shoppers Store is a Django-based online marketplace where users can browse items listed by other users, publish their own products, and contact sellers through an inbox-style messaging system. The project uses Django templates and Tailwind CSS for its interface, with SQLite as the default database.

## Features

- **Browse listings:** View available items and filter them by category or search by name and description.
- **Item details:** Open a listing to see its details and related items from the same category.
- **User accounts:** Sign up, log in, and log out using Django's authentication system.
- **Create and manage listings:** Authenticated users can add items with a description, price, category, and image; edit or delete their own listings.
- **Mark items as sold:** Listing owners can update an item's sold status.
- **User dashboard:** View the items you have listed.
- **Messaging:** Start a conversation with a listing's owner and exchange messages through the inbox.
- **Admin interface:** Manage application data through Django's built-in admin site.
- **Responsive styling:** Uses Tailwind CSS via its CDN.

## Tech Stack

- **Language:** Python
- **Web framework:** Django 6.0.1
- **Frontend:** Django Templates, HTML, Tailwind CSS (CDN)
- **Database:** SQLite by default
- **Image handling:** Pillow
- **Deployment server dependency:** Gunicorn (included in `requirements.txt`)

## Project Structure

```text
Shoppers/
├── Shoppers/                 # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/                     # Home page, authentication, contact page
│   ├── templates/core/
│   └── ...
├── item/                     # Categories, listings, item forms and views
│   ├── templates/item/
│   ├── migrations/
│   └── ...
├── dashboard/                # Dashboard for the signed-in user
├── conversation/             # Inbox, conversations and messages
│   ├── templates/conversation/
│   └── ...
├── media/                    # Uploaded listing images (sample images included)
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Prerequisites

- Python compatible with Django 6.0.1 (Python 3.12 or newer is recommended; Django 6.0 requires Python 3.12+).
- `pip`
- Git, if cloning the repository

### 2. Clone the repository

```bash
git clone https://github.com/KarthikSRao34/ShoppersStore.git
cd ShoppersStore/Shoppers
```

If you downloaded the source as a ZIP, extract it and change into the `Shoppers` directory that contains `manage.py`.

### 3. Create and activate a virtual environment

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. (Optional) Create an admin account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## Main Routes

| Route | Description |
|---|---|
| `/` | Home page with recent available listings and categories |
| `/signup/` | Create an account |
| `/login/` | Log in |
| `/items/` | Browse and search available listings |
| `/items/new/` | Create a listing (login required) |
| `/items/<id>/` | View a listing and related items |
| `/items/<id>/edit/` | Edit your own listing (login required) |
| `/items/<id>/delete/` | Delete your own listing (login required) |
| `/dashboard/` | View your listings (login required) |
| `/inbox/` | View conversations (login required) |
| `/inbox/new/<item_id>/` | Start a conversation about a listing (login required) |
| `/admin/` | Django administration |
| `/contact/` | Contact page |

Replace `<id>` and `<item_id>` with the relevant numeric database IDs.

## How It Works

1. A visitor browses available listings or searches by keyword and category.
2. A user creates an account to publish a listing or contact a seller.
3. Listing owners can edit their listings, mark them as sold, or remove them.
4. Interested users can start a conversation with the listing owner and continue messaging from their inbox.

## Media and Static Assets

Listing images are stored under `media/item_images/` in the current configuration. The project serves uploaded media through Django during development. For production, configure persistent media storage and a suitable static-file serving setup.

## Configuration and Security Notes

The repository's current settings are configured for local development and use SQLite. Before deploying publicly:

- Move `SECRET_KEY` into an environment variable and replace the exposed development key.
- Set `DEBUG = False`.
- Configure `ALLOWED_HOSTS` for the deployment domain.
- Configure HTTPS, secure cookies, and production static/media hosting.
- Use a production-ready database and persistent storage if required by the deployment platform.
- Review the login/logout redirect settings and test the full authentication flow.

Do not reuse the repository's development secret key in a production deployment.

## Tests

Run the Django test suite with:

```bash
python manage.py test
```



