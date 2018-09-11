# Twitter Clone with Vue + Django

## Setup

In the project root, run:

```
python manage.py migrate
python manage.py runserver
```

In a separate terminal, move to the `frontend` directory and run:

```
npm install
npm run dev
```

## Notes

Since I can assume the users have a modern browser, I've replaced jQuery AJAX call
with `fetch`.
