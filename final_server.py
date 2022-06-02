import uvicorn
from fastapi import File, UploadFile, FastAPI
from typing import List
import find_dot
import encryptor
import elogger

app = FastAPI()

@app.post("/")
async def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            contents = await file.read()
            dot = find_dot.find(file.filename)
            with open(f"{file.filename[:dot-2]}.jpg", 'ab') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            await file.close()
    elogger.write("wrote")
    encryptor.encrypt(f"{file.filename[:dot-2]}.jpg")
    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    intro = "/home/tzur/getters/"

