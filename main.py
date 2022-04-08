import datetime
from googleapiclient.http import MediaFileUpload
from googl import Create_Service

CLIENT_SECRET_FILE = '<client file.json>'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


request_body = {
    'snippet': {
        'categoryI': 19,
        'title': 'TittleName', #where you put tittle
        'description': 'Hello World Description', #Sets the description
        'tags': ['Testing', 'video test', 'Test'] #sets the tags
    },
    'status': {
        'privacyStatus': 'public',
        'selfDeclaredMadeForKids': False, #made for kids
    },
    'notifySubscribers': False #notify subs
}

for i in range(1,4000):
    mediaFile = MediaFileUpload('HelloWorld.MP4') #enter the file you want to upload here

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()


    service.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload('thumbnail.png')
    ).execute()