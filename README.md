## Setup Quart using venv
1. Setup venv:

       $ python3 -m venv myenv
       $ source myenv/bin/activate

       To deactivate just simply type:
       
       $ deactivate

       install required libraries

       $ pip install quart

1. Open code editor
    - Open your project folder.
    - Create the following files:
        - Files:
            1. app.py
        - Directories
            1. templates
               * index.html

1. In the templates folder put a file named __index.html__
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

1. Basic __app.py__ setup:
    ```python
    from quart import Quart, render_template

    app = Quart(__name__)

    @app.route('/')
    async def root():
        return await render_template('index.html')
    
    if __name__ == '__main__':
        app.run(debug=True)
    ```

1. Run the __app.py__ and navigate to http://127.0.0.1:5000

## To make new route:
1. Make new file inside __templates__ folder called: __about.html__
   - Inside the __about.html__ add the following:
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

1. Inside the __app.py__:
    ```python
    @app.route('/about')
    async def about():
        return await render_template('about.html')
    ```
1. To view the newly created route please restart the __app.py__ and navigate to: http://127.0.0.1:5000/about
