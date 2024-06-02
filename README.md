# Bookmarks

Bookmarks is a social website built with the python based Django framework and PostgreSQL database.

## Features

- **User authentication** - Custom authentication backend
- **Social authentication** - Facebook, Twitter, Google
- **Media file uploads**
- **Bookmarklet**
- **Image thumbnails**
- **Asynchronous HTTP requests**
- **Running the development server through HTTPS**
- **Infinite scroll pagination**
- **Follow system**
- **Activity Stream**
- **QuerySets optimization**
- **Counts denormalization with signals**
- **Counting image views with Redis**

## Installation

Clone the project and install the dependencies using [pip](https://pip.pypa.io/en/stable/)

```bash
git clone https://github.com/Eddy-123/bookmarks.git
cd bookmarks
python -m venv .bookmarks
source .bookmarks/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
