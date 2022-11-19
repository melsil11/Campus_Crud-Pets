## Pets App

**OverView**

This app has has an overarching database that has multiple models. Both cat and dog models have full CRUD capabilites. 

**Routes**
| Verb   | Path            | Action             |
|--------|-----------------|--------------------|
| GET    | `/cats/`        | `index`            |
| GET    | `/cats/:pk`     | `show`             |
| POST   | `/cats/`        | `create`           |
| PATCH  | `/cats/`        | `update`           |
| DELETE | `/cats/:pk`     | `destroy`          |

| Verb   | Path            | Action             |
|--------|-----------------|--------------------|
| GET    | `/dogs/`        | `index`            |
| GET    | `/dogs/:pk`     | `show`             |
| POST   | `/dogs/`        | `create`           |
| PATCH  | `/dogs/`        | `update`           |
| DELETE | `/dogs/:pk`     | `destroy`          |

| Verb   | Path            | Action             |
|--------|-----------------|--------------------|
| GET    | `/dog/owners`   | `index`            |
| GET    | `/dog/owners:pk | `show`             |
| POST   | `/dog/owners`   | `create`           |
| PATCH  | `/dog/owners`   | `update`           |
| DELETE | `/dog/owners:pk | `destroy`          |
**Install Instructions**
Installs:

pip,
pipenv,
pipenv shell,
Python,
Django,
Django Frameworks,
psycopg2-binary,