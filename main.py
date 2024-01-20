import uvicorn


def serve():
    uvicorn.run("interface.backend.server:app", host="127.0.0.1", port=5006, access_log=False)

    
        
    
if __name__ == '__main__':
    serve()
