import os 
import dropbox 
import WriteMode
#
class TransferData:
    def __init_(self,access_token):
        self.access_token = access_token

    def upload_file(self, filefrom, fileto):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs , files in os.walk(filefrom):

            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, filefrom)
                dropbox_path = os.path.join(fileto ,relative_path)

                with open(local_path , 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = ''
    transferData = TransferData(access_token)

    filefrom = str(input("Enter the folder path to transfer : "))
    fileto = input("Enter the path to upload to dropbox : ")

    transferData.upload_file(filefrom,fileto)
    print("file has been moved")

main()