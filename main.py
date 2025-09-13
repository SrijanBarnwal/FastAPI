from fastapi import FastAPI
app=FastAPI()


@app.get('/')
def index():
    return {"message": {"name":"heyabc5"}}

@app.get('/about')
def about():
    return {"data":"about page1"}
