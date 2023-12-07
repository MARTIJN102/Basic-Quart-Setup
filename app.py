from quart import Quart, render_template

app = Quart(__name__)

@app.route('/')
async def root():
    return await render_template('index.html')

@app.route('/about')
async def about():
    return await render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)