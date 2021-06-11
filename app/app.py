from fastapi import FastAPI
from mangum import Mangum
import uvicorn


###############################################################################
#   Application object                                                        #
###############################################################################

app = FastAPI(title="Test Lambda Function API with Docker Container", version=0.1, root_path="/dev/")

###############################################################################
#   Routers configuration                                                     #
###############################################################################
@app.get('/')
def index():
    return {"message": "Welcome to Test Lambda Function with Docker Container"} 

@app.get("/hello")
async def hello():
    return {"message": "Hello Test Lambda Function with Docker Container"}

###############################################################################
#   Handler for AWS Lambda                                                    #
###############################################################################

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)