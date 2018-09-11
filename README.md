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

Once the project is setup, go to [http://localhost:8080](http://localhost:8080) to see the Twitter Clone.

## Notes

Since I can assume the users have a modern browser, I've replaced jQuery AJAX call
with `fetch`.
