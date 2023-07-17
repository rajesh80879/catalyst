# Catalyst_count

This is a project that have user creation and data upload operations.

## Installation

1. Clone the repository: `git clone https://github.com/rajesh80879/catalyst.git`
2. Install dependencies: `pip install -r requirements.txt`
3. make migration:  `django mm user record`
4. migrate:  `django m`
5. create superuser: `django csu`
6. run the project:  `django r`

## Database and env setup

-Create an .env in catalyst_count folder

-Add the following configuration variables to the `.env` file:

    SECRET_KEY='your-secret-key'
    DEBUG=True
    ALLOWED_HOSTS=*
    DATABASE_ENGINE=django.db.backends.postgresql

    DATABASE_NAME='your-database-name'
    DATABASE_USER='db-user'
    DATABASE_PASSWORD='db-password'
    DATABASE_HOST=localhost
    DATABASE_PORT=5432