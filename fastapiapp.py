from fileinput import filename
import fastapi as fapi
import uvicorn
import subprocess
import uuid

app = fapi.FastAPI()

@app.get('/')
def info():
    return {
        'message': 'Hello World!'
    }


@app.post('/defaultAutoEditor')
def autoEditor(videoUpload: fapi.UploadFile = fapi.File(...), Commands=None):
    file_location = f'{str(uuid.uuid4())[:5]}_{videoUpload.filename}' #f'Videos/{videoUpload.filename}'
    with open(file_location, "wb+") as file_object:
        file_object.write(videoUpload.file.read())
    # run bash command autoeditor 
    new_filename = f'Altered_{file_location}' #{videoUpload.filename}'
    bashCommand = f"auto-editor {file_location} {Commands if Commands else ''} --output_file {new_filename}"
    print(bashCommand)
    p = subprocess.call(bashCommand, shell=True )
    # p.wait() #communicate()
    return fapi.responses.FileResponse(new_filename, filename=new_filename) #send response of output back to client

if __name__ == '__main__':
    uvicorn.run(app)