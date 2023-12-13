## Setup Quart using venv || Linux
#### Install Python (if not already installed):
```
python3 --version
```
#### If it's not installed, you can install it using:
```
sudo apt update
sudo apt install python3
```

#### Install the Python3-venv Package (if not already installed):
```
sudo apt install python3-venv
```
#### Create a Virtual Environment:
- Navigate to the directory where you want to create your virtual environment and run:
    ```
    python3 -m venv myenv
    ```
#### Activate the Virtual Environment:
- To activate the virtual environment, run:
    ```
    source myenv/bin/activate
    ```
- After activation, your command prompt will change to indicate that you are now working inside myenv.
#### Install Packages Inside the Virtual Environment:
- With the virtual environment activated, you can install Python packages using pip. For example:
    ```
    pip install quart
    ```
#### Deactivate the Virtual Environment:
- When you are done working in the virtual environment, you can deactivate it by running:

#### Open code editor
- Open your project folder.
- Create the following files:
    - Files:
        * `app.py`
    - Directories
        * `templates/index.html`

#### In the templates folder put a file named `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Quart Page</title>
</head>
<body>
    <h1>Index Page!</h1>
</body>
</html>
```

#### Basic `app.py` setup:
```python
from quart import Quart, render_template

app = Quart(__name__)

@app.route('/')
async def root():
    return await render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

#### Run the `app.py` and navigate to http://127.0.0.1:5000

## To make new route:
#### Make new file inside `templates` folder called: `about.html`
   - Inside the `about.html` add the following:
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Basic Quart Page</title>
        </head>
        <body>
            <h1>About Page!</h1>
        </body>
        </html>
        ```

#### Inside the `app.py`:
```python
@app.route('/about')
async def about():
    return await render_template('about.html')
```
#### To view the newly created route please restart the `app.py` and navigate to: http://127.0.0.1:5000/about
