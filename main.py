from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome from FastAPI. Let's start from here!"}

@app.get("/about")
async def root():
    return {"message":"Hy! Thanks for trying.",
            "team": "MrNothing",
            "from": "Bangladesh"}

@app.get("/about/developer")
async def root():
    return {"message":"This is Md Hafizur Rahman",
            "Role": "Craftsman",
            "from":"Bangladesh",
            }

@app.get("/features")
async def root():
    features = [
        'Basic API Calls',
        'Basic Routing',
        'Advanced Routing',
        'Validation',
        'ORM',
        'Database - Connections (SQLite, Postgres, MongoDB)',
        'Authentication - Basic, OAuth',
        'Authorization',
        'Monitoring',
        'Cashing',
        'Deployment'
    ]
    return {"features":features}

#Routing Sequence